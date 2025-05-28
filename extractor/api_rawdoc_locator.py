import os
import json
import re
from typing import Dict, List, Tuple, Optional
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup
from markdownify import markdownify as md


class APIRawDocLocator:
    """
    Links Python endpoint code to original API documentation using embeddings.
    Converts HTML documentation to Markdown, then searches through text chunks.
    If raw doc is small enough, skips retrieval and returns all chunks.
    """
    
    def __init__(self, apidocs_dir: str = "extractor/apidocs", 
                 model_name: str = "all-MiniLM-L6-v2",
                 small_doc_threshold: int = 5000,
                 base_chunk_size: int = 1500,
                 base_chunk_overlap: int = 200,
                 dynamic_chunking: bool = True):
        """
        Initialize the API documentation locator.
        
        Args:
            apidocs_dir: Directory containing API documentation
            model_name: Sentence transformer model for embeddings
            small_doc_threshold: Character threshold for considering doc "small"
            base_chunk_size: Base size of Markdown text chunks (will be adjusted dynamically)
            base_chunk_overlap: Base overlap between consecutive chunks (will be adjusted dynamically)
            dynamic_chunking: Whether to adjust chunk size based on number of endpoints
        """
        self.apidocs_dir = apidocs_dir
        self.model = SentenceTransformer(model_name)
        self.small_doc_threshold = small_doc_threshold
        self.base_chunk_size = base_chunk_size
        self.base_chunk_overlap = base_chunk_overlap
        self.dynamic_chunking = dynamic_chunking
        self.api_cache = {}
        
        # Dynamic chunking will be calculated per API
        self.chunk_size = base_chunk_size
        self.chunk_overlap = base_chunk_overlap
        
    def _calculate_dynamic_chunk_params(self, api_name: str, doc_size: int = None) -> tuple[int, int]:
        """
        Calculate dynamic chunk size and overlap based on documentation size per endpoint.
        
        Args:
            api_name: Name of the API
            doc_size: Total documentation size in characters (if known)
            
        Returns:
            Tuple of (chunk_size, chunk_overlap)
        """
        if not self.dynamic_chunking:
            return self.base_chunk_size, self.base_chunk_overlap
            
        # Count Python endpoint files for this API
        python_files = self._get_python_files(api_name)
        num_endpoints = len(python_files)
        
        if num_endpoints == 0:
            return self.base_chunk_size, self.base_chunk_overlap
        
        # If doc_size not provided, we need to load the documentation to get it
        if doc_size is None:
            # This is a bit circular, but we need the doc size to calculate chunk params
            # We'll use a temporary load to get the raw text size
            api_dir = os.path.join(self.apidocs_dir, api_name)
            html_file = None
            try:
                files_in_dir = os.listdir(api_dir)
                html_files = [f for f in files_in_dir if f.endswith('.html')]
                if html_files:
                    html_file = os.path.join(api_dir, html_files[0])
            except:
                pass
            
            if html_file and os.path.exists(html_file):
                raw_text = self._convert_html_to_markdown(html_file)
                doc_size = len(raw_text)
            else:
                doc_size = 0
        
        if doc_size == 0:
            return self.base_chunk_size, self.base_chunk_overlap
        
        # Calculate chunk size based on documentation size per endpoint
        chars_per_endpoint = doc_size / num_endpoints
        
        # Dynamic scaling logic: chunk size should be AT LEAST chars_per_endpoint
        # to ensure each endpoint gets complete documentation coverage
        
        # Base chunk size is at least the chars per endpoint
        chunk_size = int(chars_per_endpoint)
        
        # Add some buffer for better context and overlap
        if chars_per_endpoint <= 2000:
            # Small docs: add 50% buffer
            chunk_size = int(chars_per_endpoint * 1.5)
            overlap_ratio = 0.20  # 20% overlap
        elif chars_per_endpoint <= 5000:
            # Medium docs: add 30% buffer  
            chunk_size = int(chars_per_endpoint * 1.3)
            overlap_ratio = 0.25  # 25% overlap
        elif chars_per_endpoint <= 10000:
            # Large docs: add 20% buffer
            chunk_size = int(chars_per_endpoint * 1.2)
            overlap_ratio = 0.30  # 30% overlap
        else:
            # Very large docs: add 10% buffer but cap at reasonable size
            chunk_size = min(8000, int(chars_per_endpoint * 1.1))
            overlap_ratio = 0.35  # 35% overlap
        
        # Ensure minimum chunk size for very small docs
        chunk_size = max(1000, chunk_size)
        
        # Calculate overlap based on chunk size
        chunk_overlap = int(chunk_size * overlap_ratio)
        
        # Ensure minimum overlap
        chunk_overlap = max(chunk_overlap, self.base_chunk_overlap)
        
        return chunk_size, chunk_overlap
        
    def _extract_endpoint_name_from_file(self, filepath: str) -> str:
        """Extract endpoint name from Python file path."""
        filename = os.path.basename(filepath)
        # Remove .py extension and method suffix
        endpoint_name = filename.replace('.py', '')
        # Remove HTTP method suffixes like _GET, _POST, etc.
        endpoint_name = re.sub(r'_[A-Z]+$', '', endpoint_name)
        return endpoint_name
    
    def _extract_function_name_from_code(self, code_content: str) -> str:
        """Extract the main function name from Python code."""
        # Look for function definition
        match = re.search(r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code_content)
        if match:
            return match.group(1)
        return ""
    
    def _convert_html_to_markdown(self, html_file: str) -> str:
        """Convert HTML file to clean Markdown text using minimal filtering."""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Pre-process HTML to remove script content more thoroughly
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Remove script and style elements completely
            for script in soup(["script", "style", "noscript"]):
                script.decompose()
            
            # Look for data-title elements specifically (works for React-based docs)
            elements = soup.select('[data-title]')
            
            if elements:
                # For OSRM and similar React docs, get ALL data-title elements, not just one
                all_content_parts = []
                for element in elements:
                    content_text = element.get_text().strip()
                    if len(content_text) > 50:  # Only include elements with substantial content
                        all_content_parts.append(str(element))
                
                if all_content_parts:
                    # Combine all content parts
                    cleaned_html = '\n'.join(all_content_parts)
                else:
                    cleaned_html = str(soup)
            else:
                # Fallback: remove navigation elements and use full content
                for element in soup(["nav", "footer", "header", "aside"]):
                    element.decompose()
                
                # Remove elements with common non-content classes/ids
                for element in soup.find_all(attrs={"class": re.compile(r"(nav|menu|sidebar|footer|header|ad|advertisement|translate|loading)", re.I)}):
                    element.decompose()
                
                cleaned_html = str(soup)
            
            # Convert HTML to Markdown
            markdown_text = md(
                cleaned_html,
                heading_style="ATX",  # Use # style headings
                bullets="-",          # Use - for bullet points
                strip=['meta', 'link']  # Remove remaining unwanted tags
            )
            
            # Post-process to clean up the markdown (minimal filtering)
            lines = []
            for line in markdown_text.splitlines():
                line = line.strip()
                
                # Skip empty lines but preserve paragraph breaks
                if not line:
                    if lines and lines[-1] != '':
                        lines.append('')
                    continue
                
                # Always keep headings
                if line.startswith('#'):
                    lines.append(line)
                    continue
                
                # Only skip very obvious JavaScript patterns (minimal filtering)
                if any(pattern in line.lower() for pattern in [
                    'function()', 'class ', 'data-reactid=', 'data-reactroot'
                ]) and len(line) < 100:  # Only skip short lines with these patterns
                    continue
                
                # Keep everything else
                lines.append(line)
            
            # Join lines and clean up excessive whitespace
            cleaned_markdown = '\n'.join(lines)
            
            # Remove excessive newlines (more than 2 consecutive)
            cleaned_markdown = re.sub(r'\n{3,}', '\n\n', cleaned_markdown)
            
            # Remove any remaining data attributes or React artifacts
            cleaned_markdown = re.sub(r'data-[a-zA-Z-]+="[^"]*"', '', cleaned_markdown)
            cleaned_markdown = re.sub(r'class="[^"]*"', '', cleaned_markdown)
            
            return cleaned_markdown
            
        except Exception as e:
            print(f"Error converting HTML to Markdown {html_file}: {e}")
            return ""
    
    def _create_text_chunks(self, markdown_text: str) -> List[Dict]:
        """Split Markdown text into overlapping chunks with metadata, preserving semantic boundaries."""
        if not markdown_text:
            return []
        
        chunks = []
        start = 0
        chunk_id = 0
        
        # First, identify major sections by headings for better chunking
        lines = markdown_text.split('\n')
        section_boundaries = []
        
        for i, line in enumerate(lines):
            if line.strip().startswith('#'):
                section_boundaries.append(i)
        
        while start < len(markdown_text):
            end = start + self.chunk_size
            chunk_text = markdown_text[start:end]
            
            # Try to break at better semantic boundaries for Markdown
            if end < len(markdown_text):
                # Only look for boundaries in the last 20% of the chunk to avoid cutting too short
                min_chunk_size = int(self.chunk_size * 0.8)  # Don't cut shorter than 80% of target
                search_start = max(min_chunk_size, len(chunk_text) - 300)
                
                # Only break at boundaries if we're close to the target size
                if len(chunk_text) >= min_chunk_size:
                    # Priority order for Markdown: headings, paragraphs, lists, sentences
                    boundary_markers = [
                        ('\n# ', 10),     # H1 headings (highest priority)
                        ('\n## ', 9),     # H2 headings
                        ('\n### ', 8),    # H3 headings
                        ('\n#### ', 7),   # H4 headings
                        ('\n##### ', 6),  # H5 headings
                        ('\n###### ', 5), # H6 headings
                        ('\n\n', 4),      # Paragraph breaks (high priority)
                        ('\n- ', 3),      # List items
                        ('\n* ', 3),      # List items (alternative)
                        ('\n1. ', 3),     # Numbered lists
                        ('\n> ', 2.5),    # Blockquotes
                        ('\n```', 2.5),   # Code blocks
                        ('\n| ', 2),      # Table rows
                        ('. ', 1.5),      # Sentence endings with space
                        ('! ', 1.5),      # Exclamation with space
                        ('? ', 1.5),      # Question with space
                    ]
                    
                    best_boundary = -1
                    best_priority = -1
                    
                    for marker, priority in boundary_markers:
                        pos = chunk_text.rfind(marker, search_start)
                        if pos > search_start and priority > best_priority:
                            best_boundary = pos + len(marker)
                            best_priority = priority
                    
                    # Only use boundary if it's a high-priority one (headings or paragraphs)
                    if best_boundary > 0 and best_priority >= 4:
                        chunk_text = chunk_text[:best_boundary]
                        end = start + len(chunk_text)
                    
                    # Fallback: try to break at word boundaries only in the last 100 chars
                    elif ' ' in chunk_text[-100:]:
                        last_space = chunk_text.rfind(' ', len(chunk_text) - 100)
                        if last_space > search_start:
                            chunk_text = chunk_text[:last_space]
                            end = start + len(chunk_text)
            
            chunk_text = chunk_text.strip()
            
            # Only create chunk if it has substantial content
            if len(chunk_text) > 200:  # Increased minimum chunk size for better content
                # Extract headings from this chunk for better metadata
                chunk_headings = []
                for line in chunk_text.split('\n'):
                    if line.strip().startswith('#'):
                        chunk_headings.append(line.strip())
                
                chunk = {
                    'id': chunk_id,
                    'text': chunk_text,
                    'start_pos': start,
                    'end_pos': start + len(chunk_text),
                    'length': len(chunk_text),
                    'type': 'markdown_chunk',
                    'headings': chunk_headings,  # Add heading metadata
                    'word_count': len(chunk_text.split()),
                    'line_count': len(chunk_text.split('\n'))
                }
                chunks.append(chunk)
                chunk_id += 1
            
            # Move start position with overlap
            start = end - self.chunk_overlap
            
            # Ensure we don't go backwards
            if start <= chunks[-1]['start_pos'] if chunks else False:
                start = (chunks[-1]['end_pos'] if chunks else 0) + 1
            
            if start >= len(markdown_text):
                break
        
        return chunks
    
    def _load_api_documentation(self, api_name: str) -> Dict:
        """Load and parse API documentation for a given API."""
        if api_name in self.api_cache:
            return self.api_cache[api_name]
            
        api_dir = os.path.join(self.apidocs_dir, api_name)
        
        if not os.path.exists(api_dir):
            return {}
            
        # Find HTML file first to get document size
        html_file = None
        try:
            files_in_dir = os.listdir(api_dir)
            html_files = [f for f in files_in_dir if f.endswith('.html')]
            
            if html_files:
                # Take the first HTML file found
                html_file = os.path.join(api_dir, html_files[0])
        except Exception as e:
            print(f"Error listing directory {api_dir}: {e}")  # Keep error messages
        
        # Get document size first for dynamic chunk calculation
        raw_text = ""
        doc_size = 0
        if html_file and os.path.exists(html_file):
            raw_text = self._convert_html_to_markdown(html_file)
            doc_size = len(raw_text)
        
        # Calculate dynamic chunking parameters based on doc size and endpoints
        dynamic_chunk_size, dynamic_chunk_overlap = self._calculate_dynamic_chunk_params(api_name, doc_size)
        
        # Temporarily set the dynamic parameters
        original_chunk_size = self.chunk_size
        original_chunk_overlap = self.chunk_overlap
        self.chunk_size = dynamic_chunk_size
        self.chunk_overlap = dynamic_chunk_overlap
        
        api_data = {
            'text_chunks': [],
            'endpoint_sections': [],
            'raw_doc_size': doc_size,
            'html_file': html_file,
            'raw_text': raw_text,
            'chunk_size_used': dynamic_chunk_size,
            'chunk_overlap_used': dynamic_chunk_overlap,
            'num_endpoints': len(self._get_python_files(api_name)),
            'chars_per_endpoint': doc_size / max(1, len(self._get_python_files(api_name)))
        }
        
        # Create chunks if we have content
        if raw_text:
            # Create general text chunks with dynamic parameters
            api_data['text_chunks'] = self._create_text_chunks(raw_text)
            
            # Also detect structured endpoint sections
            api_data['endpoint_sections'] = self._detect_endpoint_sections(raw_text)
        
        # Restore original parameters
        self.chunk_size = original_chunk_size
        self.chunk_overlap = original_chunk_overlap
        
        self.api_cache[api_name] = api_data
        return api_data
    
    def _get_python_files(self, api_name: str) -> List[str]:
        """Get all Python endpoint files for an API."""
        api_dir = os.path.join(self.apidocs_dir, api_name)
        if not os.path.exists(api_dir):
            return []
            
        python_files = []
        for file in os.listdir(api_dir):
            if file.endswith('.py') and not file.startswith('__'):
                python_files.append(os.path.join(api_dir, file))
                
        return python_files
    
    def _create_embeddings(self, texts: List[str]) -> np.ndarray:
        """Create embeddings for a list of texts."""
        if not texts:
            return np.array([])
        return self.model.encode(texts)
    
    def _find_best_matches(self, query_embedding: np.ndarray, 
                          candidate_embeddings: np.ndarray, 
                          candidates: List[Dict],
                          top_k: int = 5) -> List[Tuple[Dict, float]]:
        """Find best matching text chunks based on embedding similarity."""
        if len(candidate_embeddings) == 0:
            return []
            
        # Calculate cosine similarities
        similarities = cosine_similarity([query_embedding], candidate_embeddings)[0]
        
        # Get top k matches with lower threshold for more results
        top_indices = np.argsort(similarities)[::-1][:top_k * 2]  # Get more candidates initially
        
        matches = []
        for idx in top_indices:
            if similarities[idx] > 0.15:  # Lower threshold for more inclusive results
                candidate = candidates[idx]
                score = float(similarities[idx])
                
                # Add additional metadata for better understanding
                enhanced_candidate = candidate.copy()
                enhanced_candidate['similarity_score'] = score
                enhanced_candidate['match_quality'] = self._assess_match_quality(candidate, score)
                
                matches.append((enhanced_candidate, score))
                
                # Stop when we have enough high-quality matches
                if len(matches) >= top_k:
                    break
        
        return matches
    
    def _assess_match_quality(self, candidate: Dict, score: float) -> str:
        """Assess the quality of a match based on score and content characteristics."""
        if score > 0.7:
            return "excellent"
        elif score > 0.5:
            return "good"
        elif score > 0.3:
            return "fair"
        else:
            return "poor"
    
    def locate_documentation_for_endpoint(self, api_name: str, endpoint_file: str) -> Dict:
        """
        Locate relevant documentation chunks for a specific endpoint file.
        
        Args:
            api_name: Name of the API
            endpoint_file: Path to the Python endpoint file
            
        Returns:
            Dictionary containing matched documentation chunks and metadata
        """
        # Load API documentation
        api_data = self._load_api_documentation(api_name)
        
        if not api_data:
            return {
                'endpoint_file': endpoint_file,
                'api_name': api_name,
                'matches': [],
                'html_file': None,
                'is_small_doc': False,
                'raw_doc_size': 0,
                'total_chunks': 0,
                'total_sections': 0,
                'query_info': {},
                'error': 'API documentation not found'
            }
        
        # Check if raw doc is small enough to skip retrieval
        is_small_doc = api_data['raw_doc_size'] < self.small_doc_threshold
        result = {
            'endpoint_file': endpoint_file,
            'api_name': api_name,
            'html_file': api_data['html_file'],
            'is_small_doc': is_small_doc,
            'raw_doc_size': api_data['raw_doc_size'],
            'total_chunks': len(api_data['text_chunks']),
            'total_sections': len(api_data['endpoint_sections']),
            'matches': [],
            'query_info': {}
        }
        
        if is_small_doc:
            # Return all chunks for small docs
            all_content = []
            # Add endpoint sections first (higher priority)
            for section in api_data['endpoint_sections']:
                all_content.append((section, 1.0))
            # Add text chunks
            for chunk in api_data['text_chunks']:
                all_content.append((chunk, 1.0))
            
            result['matches'] = all_content
            result['message'] = f'Raw doc is small ({api_data["raw_doc_size"]} chars) - returning all {len(api_data["endpoint_sections"])} sections and {len(api_data["text_chunks"])} chunks'
            return result
        
        # Extract endpoint information from the Python file
        try:
            with open(endpoint_file, 'r', encoding='utf-8') as f:
                code_content = f.read()
        except Exception as e:
            result['error'] = f'Error reading endpoint file: {e}'
            return result
        
        # Extract endpoint name from file path
        endpoint_name = self._extract_endpoint_name_from_file(endpoint_file)
        
        # Load JSON descriptions for this API
        json_descriptions = self._load_json_descriptions(api_name)
        
        # Try to find the description for this endpoint
        endpoint_description = ""
        endpoint_info = None
        
        # Try different variations of the endpoint name
        possible_keys = [
            endpoint_name,
            endpoint_name.replace('_service', ''),
            endpoint_name.replace('service', ''),
            endpoint_name.split('_')[0] if '_' in endpoint_name else endpoint_name
        ]
        
        for key in possible_keys:
            if key in json_descriptions:
                endpoint_info = json_descriptions[key]
                endpoint_description = endpoint_info['description']
                break
        
        if not endpoint_description:
            # Fallback to extracting from code if no JSON description found
            function_name = self._extract_function_name_from_code(code_content)
            code_context = self._extract_code_context(code_content)
            query_text = ' '.join(filter(None, [endpoint_name, function_name, code_context]))
            query_source = "code_extraction"
        else:
            # Use the JSON description as the primary query
            query_text = f"{endpoint_name} {endpoint_description}"
            if endpoint_info and 'full_info' in endpoint_info:
                # Add parameter descriptions for richer context
                full_info = endpoint_info['full_info']
                param_descriptions = []
                
                for param_list in ['required_parameters', 'optional_parameters']:
                    if param_list in full_info:
                        for param in full_info[param_list]:
                            if 'description' in param:
                                param_descriptions.append(param['description'])
                
                if param_descriptions:
                    query_text += " " + " ".join(param_descriptions[:3])  # Add first 3 param descriptions
            
            query_source = "json_description"
        
        if not query_text:
            result['error'] = 'Could not extract endpoint information'
            return result
        
        # Store query information for debugging/reporting
        result['query_info'] = {
            'endpoint_name': endpoint_name,
            'query_source': query_source,
            'description': endpoint_description if endpoint_description else "Not found in JSON",
            'full_query': query_text[:300] + "..." if len(query_text) > 300 else query_text,
            'query_length': len(query_text)
        }
        
        # Create embeddings
        query_embedding = self._create_embeddings([query_text])[0]
        
        # Prepare candidates from both endpoint sections and text chunks
        all_candidates = []
        candidate_texts = []
        
        # When using dynamic chunking, prioritize larger text chunks over structured sections
        # to ensure complete documentation coverage per endpoint
        if self.dynamic_chunking and api_data.get('chunk_size_used', 0) > self.base_chunk_size:
            # First, add general text chunks (higher priority for dynamic chunking)
            for chunk in api_data['text_chunks']:
                all_candidates.append(chunk)
                candidate_texts.append(chunk['text'])
            
            # Then add structured endpoint sections as fallback
            for section in api_data['endpoint_sections']:
                all_candidates.append(section)
                candidate_texts.append(f"{section['title']} {section['content']}")
        else:
            # Default behavior: structured sections first
            for section in api_data['endpoint_sections']:
                all_candidates.append(section)
                candidate_texts.append(f"{section['title']} {section['content']}")
            
            # Then add general text chunks
            for chunk in api_data['text_chunks']:
                all_candidates.append(chunk)
                candidate_texts.append(chunk['text'])
        
        if not all_candidates:
            result['message'] = 'No content found in documentation'
            return result
        
        candidate_embeddings = self._create_embeddings(candidate_texts)
        
        # Find best matches
        matches = self._find_best_matches(query_embedding, candidate_embeddings, all_candidates, top_k=8)
        result['matches'] = matches
        
        return result
    
    def _extract_code_context(self, code_content: str) -> str:
        """Extract additional context from code like comments and docstrings."""
        context_parts = []
        
        # Extract docstrings
        docstring_pattern = r'"""(.*?)"""'
        docstrings = re.findall(docstring_pattern, code_content, re.DOTALL)
        context_parts.extend(docstrings)
        
        # Extract single-line comments
        comment_pattern = r'#\s*(.+)'
        comments = re.findall(comment_pattern, code_content)
        context_parts.extend(comments)
        
        # Extract URL patterns that might indicate endpoint paths
        url_pattern = r'["\']([^"\']*(?:api|endpoint|service|route)[^"\']*)["\']'
        urls = re.findall(url_pattern, code_content, re.IGNORECASE)
        context_parts.extend(urls)
        
        return ' '.join(context_parts)
    
    def locate_documentation_for_api(self, api_name: str) -> Dict:
        """
        Locate documentation for all endpoints in an API.
        
        Args:
            api_name: Name of the API
            
        Returns:
            Dictionary containing all endpoint mappings
        """
        python_files = self._get_python_files(api_name)
        
        results = {
            'api_name': api_name,
            'total_endpoints': len(python_files),
            'endpoint_mappings': []
        }
        
        for py_file in python_files:
            mapping = self.locate_documentation_for_endpoint(api_name, py_file)
            results['endpoint_mappings'].append(mapping)
        
        return results
    
    def locate_all_apis(self) -> Dict:
        """Locate documentation for all APIs in the apidocs directory."""
        if not os.path.exists(self.apidocs_dir):
            return {'error': f'API docs directory not found: {self.apidocs_dir}'}
        
        api_names = [d for d in os.listdir(self.apidocs_dir) 
                    if os.path.isdir(os.path.join(self.apidocs_dir, d))]
        
        results = {
            'total_apis': len(api_names),
            'api_results': []
        }
        
        for api_name in api_names:
            api_result = self.locate_documentation_for_api(api_name)
            results['api_results'].append(api_result)
        
        return results
    
    def generate_mapping_report(self, output_file: str = None) -> str:
        """Generate a detailed report of all endpoint-documentation mappings."""
        all_results = self.locate_all_apis()
        
        report_lines = []
        report_lines.append("API Documentation Mapping Report")
        report_lines.append("=" * 50)
        # report_lines.append(f"Total APIs processed: {all_results['total_apis']}")
        report_lines.append("")
        
        for api_result in all_results['api_results']:
            api_name = api_result['api_name']
            report_lines.append(f"API: {api_name}")
            report_lines.append("-" * 30)
            report_lines.append(f"Total endpoints: {api_result['total_endpoints']}")
            
            for mapping in api_result['endpoint_mappings']:
                endpoint_file = os.path.basename(mapping['endpoint_file'])
                report_lines.append(f"\nEndpoint: {endpoint_file}")
                
                # Show query information if available
                if 'query_info' in mapping:
                    query_info = mapping['query_info']
                    report_lines.append(f"  Query: {query_info.get('endpoint_name', 'N/A')} | Source: {query_info.get('query_source', 'N/A')}")
                    if query_info.get('description') and query_info.get('description') != "Not found in JSON":
                        report_lines.append(f"  Description: {query_info['description']}")
                    if query_info.get('full_query'):
                        report_lines.append(f"  Full Query: {query_info['full_query'][:150]}...")  # Shorter preview
                
                if mapping.get('is_small_doc'):
                    report_lines.append(f"  Status: Small doc ({mapping['raw_doc_size']} chars) - all content returned")
                elif mapping.get('error'):
                    report_lines.append(f"  Error: {mapping['error']}")
                else:
                    report_lines.append(f"  Total chunks in doc: {mapping['total_chunks']}")
                    if 'total_sections' in mapping:
                        report_lines.append(f"  Structured sections: {mapping['total_sections']}")
                    report_lines.append(f"  Relevant matches found: {len(mapping['matches'])}")
                    
                    for i, (content, score) in enumerate(mapping['matches'][:5]):  # Top 5 matches
                        content_type = "Section" if 'title' in content else "Chunk"
                        
                        # Enhanced content identification
                        if 'title' in content:
                            content_id = content['title']
                        elif 'headings' in content and content['headings']:
                            content_id = f"Chunk {content.get('id', 'Unknown')} ({content['headings'][0]})"
                        else:
                            content_id = f"Chunk {content.get('id', 'Unknown')}"
                        
                        # Show match quality if available
                        quality_info = ""
                        if 'match_quality' in content:
                            quality_info = f" [{content['match_quality']}]"
                        
                        report_lines.append(f"    {i+1}. {content_type}: {content_id} (score: {score:.3f}){quality_info}")
                        
                        # Show preview of content
                        if 'title' in content:
                            # This is a structured section
                            preview = content['content'][:200] + "..." if len(content['content']) > 200 else content['content']
                        else:
                            # This is a text chunk
                            preview = content['text'][:200] + "..." if len(content['text']) > 200 else content['text']
                        
                        report_lines.append(f"       Preview: {preview}")
                        
                        # Enhanced metadata display
                        if 'start_pos' in content:
                            metadata_parts = [f"{content['start_pos']}-{content['end_pos']} ({content['length']} chars)"]
                            if 'word_count' in content:
                                metadata_parts.append(f"{content['word_count']} words")
                            if 'headings' in content and len(content['headings']) > 1:
                                metadata_parts.append(f"{len(content['headings'])} headings")
                            report_lines.append(f"       Position: {', '.join(metadata_parts)}")
                        elif 'level' in content:
                            report_lines.append(f"       Section level: h{content['level']}")
            
            report_lines.append("\n" + "=" * 50 + "\n")
        
        report = "\n".join(report_lines)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"Report saved to: {output_file}")
        
        return report
    
    def get_chunk_context(self, api_name: str, chunk_id: int, context_size: int = 200) -> str:
        """Get additional context around a specific chunk."""
        api_data = self._load_api_documentation(api_name)
        if not api_data or not api_data['text_chunks']:
            return ""
        
        # Find the chunk
        target_chunk = None
        for chunk in api_data['text_chunks']:
            if chunk['id'] == chunk_id:
                target_chunk = chunk
                break
        
        if not target_chunk:
            return ""
        
        # Get context from markdown text
        markdown_text = api_data['raw_text']
        start = max(0, target_chunk['start_pos'] - context_size)
        end = min(len(markdown_text), target_chunk['end_pos'] + context_size)
        
        return markdown_text[start:end]
    
    def _detect_endpoint_sections(self, markdown_text: str) -> List[Dict]:
        """Detect and extract endpoint sections from Markdown text based on headings."""
        try:
            sections = []
            
            # Look for common API documentation patterns in headings
            endpoint_indicators = [
                'endpoint', 'api', 'service', 'method', 'route', 'path',
                'GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'request', 'response'
            ]
            
            # Split by lines to process headings
            lines = markdown_text.split('\n')
            
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                
                # Check if this is a heading line
                heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
                if heading_match:
                    heading_level = len(heading_match.group(1))
                    heading_text = heading_match.group(2).strip()
                    
                    # Check if heading contains endpoint indicators
                    if any(indicator.lower() in heading_text.lower() for indicator in endpoint_indicators):
                        section_content = [line]  # Start with the heading
                        
                        # Collect content until next heading of same or higher level
                        j = i + 1
                        while j < len(lines):
                            next_line = lines[j].strip()
                            
                            # Check if this is a heading of same or higher level
                            next_heading_match = re.match(r'^(#{1,6})\s+(.+)$', next_line)
                            if next_heading_match:
                                next_level = len(next_heading_match.group(1))
                                if next_level <= heading_level:
                                    break
                            
                            section_content.append(lines[j])
                            j += 1
                        
                        if len(section_content) > 1:  # Only add if there's content beyond the heading
                            section_text = '\n'.join(section_content).strip()
                            sections.append({
                                'title': heading_text,
                                'content': section_text,
                                'level': heading_level,
                                'type': 'markdown_section',
                                'start_line': i,
                                'end_line': j - 1
                            })
                        
                        i = j - 1  # Skip to where we left off
                
                i += 1
            
            return sections
            
        except Exception as e:
            print(f"Error detecting endpoint sections from Markdown: {e}")
            return []
    
    def _load_json_descriptions(self, api_name: str) -> Dict[str, str]:
        """Load endpoint descriptions from the JSON file."""
        api_dir = os.path.join(self.apidocs_dir, api_name)
        json_file = os.path.join(api_dir, f"{api_name}.txt")
        
        descriptions = {}
        
        if os.path.exists(json_file):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                if 'endpoints' in data:
                    for endpoint in data['endpoints']:
                        name = endpoint.get('name', '')
                        description = endpoint.get('description', '')
                        
                        # Create multiple possible keys for matching
                        # Convert "Route Service" -> "route_service"
                        service_key = name.lower().replace(' ', '_')
                        
                        # Also try variations
                        service_variations = [
                            service_key,
                            service_key.replace('_service', ''),
                            name.lower().replace(' ', ''),
                            name.lower()
                        ]
                        
                        # Store description for all variations
                        for key in service_variations:
                            if key:
                                descriptions[key] = {
                                    'description': description,
                                    'name': name,
                                    'full_info': endpoint
                                }
                
                print(f"Loaded {len(descriptions)} endpoint descriptions from {json_file}")
                
            except Exception as e:
                print(f"Error loading JSON descriptions from {json_file}: {e}")
        
        return descriptions


def main():
    """Example usage of the API documentation locator with minimal filtering."""
    locator = APIRawDocLocator()
    
    # Example 1: Locate documentation for a specific endpoint
    print("Example 1: Locating Markdown documentation chunks for OSRM route service...")
    print("Using minimal filtering HTML to Markdown conversion...")
    result = locator.locate_documentation_for_endpoint(
        'OSRM', 
        'extractor/apidocs/OSRM/route_service_GET.py'
    )
    
    print(f"API: {result['api_name']}")
    print(f"HTML file: {result['html_file']}")
    print(f"Markdown doc size: {result['raw_doc_size']} characters")
    print(f"Total chunks: {result['total_chunks']}")
    print(f"Total sections: {result['total_sections']}")
    print(f"Is small doc: {result['is_small_doc']}")
    
    # Show query information
    if 'query_info' in result:
        query_info = result['query_info']
        print(f"Query endpoint: {query_info.get('endpoint_name', 'N/A')}")
        print(f"Query source: {query_info.get('query_source', 'N/A')}")
        if query_info.get('description') and query_info.get('description') != "Not found in JSON":
            print(f"Description: {query_info['description']}")
        print(f"Query length: {query_info.get('query_length', 0)} characters")
    
    print(f"Found {len(result['matches'])} relevant chunks")
    
    for i, (chunk, score) in enumerate(result['matches'][:3]):
        print(f"\n  Match {i+1} (score: {score:.3f}):")
        
        # Show chunk type and metadata
        chunk_type = "Section" if 'title' in chunk else "Chunk"
        print(f"    Type: {chunk_type}")
        
        if 'match_quality' in chunk:
            print(f"    Quality: {chunk['match_quality']}")
        
        if 'headings' in chunk and chunk['headings']:
            print(f"    Headings: {chunk['headings'][:2]}")  # Show first 2 headings
        
        if 'word_count' in chunk:
            print(f"    Words: {chunk['word_count']}")
        
        # Show content preview
        if 'title' in chunk:
            content_preview = chunk['content'][:300] + "..." if len(chunk['content']) > 300 else chunk['content']
        else:
            content_preview = chunk['text'][:300] + "..." if len(chunk['text']) > 300 else chunk['text']
        
        print(f"    Preview: {content_preview}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: Generate full mapping report
    print("Example 2: Generating full Markdown-based mapping report with minimal filtering...")
    report = locator.generate_mapping_report('api_markdown_mapping_report.txt')
    print("Report preview:")
    print(report[:1000] + "..." if len(report) > 1000 else report)


if __name__ == "__main__":
    main()
