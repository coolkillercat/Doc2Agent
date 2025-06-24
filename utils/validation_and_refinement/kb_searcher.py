"""
Utilities for semantic search of KB.
"""

from sentence_transformers import SentenceTransformer, util


def initialize_model(model_name="flax-sentence-embeddings/st-codesearch-distilroberta-base"):
    """
    Initialize the sentence transformer model for embeddings.

    Args:
        model_name: Name of the pretrained model to use

    Returns:
        model: Initialized SentenceTransformer model
    """
    return SentenceTransformer(model_name)


def encode_keys(model, keys_dict):
    """
    Encode dictionary keys using the sentence transformer model.

    Args:
        model: SentenceTransformer model
        keys_dict: Dictionary of keys to encode

    Returns:
        keys: List of keys
        keys_emb: Tensor of encoded keys
    """
    keys = list(keys_dict.keys())
    keys_emb = model.encode(keys, convert_to_tensor=True)
    return keys, keys_emb


def search_kb(query, param_keys, param_keys_emb, parameter_dict, response_keys, response_keys_emb, response_dict, description_keys, description_to_param_dict, description_keys_emb, model, use_response_only=False, max_candidates=3):
    """
    Search the knowledge base for the most relevant keys to the query.

    Args:
        query: param name or description
        param_keys: List of parameter keys
        param_keys_emb: Tensor of encoded parameter keys
        parameter_dict: Dictionary of parameter keys to examples
        response_keys: List of response keys
        response_keys_emb: Tensor of encoded response keys
        response_dict: Dictionary of response keys to examples
        description_keys: List of description keys
        description_to_param_dict: Dictionary mapping descriptions to parameter names
        description_keys_emb: Tensor of encoded description keys
        model: SentenceTransformer model
        use_response_only: If True, only use response_dict for parameter inference
        max_candidates: Maximum number of candidate results to return

    Returns:
        results: List of candidate values (up to max_candidates), or None if no match found
    """
    query_emb = model.encode(query, convert_to_tensor=True)
    
    if use_response_only:
        # Only search in response_dict
        hits_response = util.semantic_search(query_emb, response_keys_emb)[0]
        
        # Filter out results below a certain threshold
        threshold = 0
        hits_response = [hit for hit in hits_response if hit['score'] > threshold]
        
        try:
            if not hits_response:
                return None
            
            # Return up to max_candidates results from response_dict
            candidates = []
            for hit in hits_response[:max_candidates]:
                candidate_values = response_dict[response_keys[hit['corpus_id']]]
                candidates.append(candidate_values)
            
            return candidates if candidates else None
        except Exception as e:
            print(f"Error in search_kb (response_only mode): {e}")
            return None
    
    # Search across all knowledge bases and collect candidates
    hits_param = util.semantic_search(query_emb, param_keys_emb)[0] if param_keys_emb.size(0) > 0 else []
    hits_description = util.semantic_search(query_emb, description_keys_emb)[0] if len(description_keys) > 0 else []
    hits_response = util.semantic_search(query_emb, response_keys_emb)[0] if response_keys_emb.size(0) > 0 else []

    # Filter out results below a certain threshold
    threshold = 0
    hits_param = [hit for hit in hits_param if hit['score'] > threshold]
    hits_description = [hit for hit in hits_description if hit['score'] > threshold]
    hits_response = [hit for hit in hits_response if hit['score'] > threshold]

    try:
        # Collect all candidates with their scores
        all_candidates = []
        
        # Add parameter dictionary candidates
        for hit in hits_param:
            candidate_values = parameter_dict[param_keys[hit['corpus_id']]]
            all_candidates.append((hit['score'], candidate_values, 'param'))
        
        # Add description-based candidates
        for hit in hits_description:
            try:
                param_key = '[' + description_to_param_dict[description_keys[hit['corpus_id']]] + ']'
                if param_key in parameter_dict:
                    candidate_values = parameter_dict[param_key]
                    all_candidates.append((hit['score'], candidate_values, 'description'))
            except KeyError:
                continue
        
        # Add response dictionary candidates
        for hit in hits_response:
            candidate_values = response_dict[response_keys[hit['corpus_id']]]
            all_candidates.append((hit['score'], candidate_values, 'response'))
        
        # Sort by score (descending) and return top candidates
        if not all_candidates:
            return None
        
        all_candidates.sort(key=lambda x: x[0], reverse=True)
        
        # Extract unique candidate values (avoid duplicates)
        unique_candidates = []
        seen_candidates = set()
        
        for score, candidate_values, source in all_candidates[:max_candidates * 2]:  # Get more to filter duplicates
            # Convert set to frozenset for hashability
            candidate_key = frozenset(candidate_values) if isinstance(candidate_values, set) else frozenset([candidate_values])
            
            if candidate_key not in seen_candidates:
                seen_candidates.add(candidate_key)
                unique_candidates.append(candidate_values)
                
                if len(unique_candidates) >= max_candidates:
                    break
        
        return unique_candidates if unique_candidates else None
        
    except Exception as e:
        print(f"Error in search_kb: {e}")
        return None
