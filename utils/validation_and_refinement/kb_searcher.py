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


def search_kb(query, param_keys, param_keys_emb, parameter_dict, response_keys, response_keys_emb, response_dict, description_keys, description_to_param_dict, description_keys_emb, model):
    """
    Search the knowledge base for the most relevant keys to the query.

    Args:
        query: param name or description
        keys_emb: Tensor of encoded keys
        keys_dict: Dictionary of keys
        model: SentenceTransformer model
        top_k: Number of top results to return

    Returns:
        results: List of tuples containing the key and its similarity score
    """
    query_emb = model.encode(query, convert_to_tensor=True)
    hits_param = util.semantic_search(query_emb, param_keys_emb)[0]
    hits_description = util.semantic_search(query_emb, description_keys_emb)[0]
    hits_response = util.semantic_search(query_emb, response_keys_emb)[0]

    # Filter out results below a certain threshold
    threshold = 0.85
    hits_param = [hit for hit in hits_param if hit['score'] > threshold]
    hits_description = [hit for hit in hits_description if hit['score'] > threshold]
    hits_response = [hit for hit in hits_response if hit['score'] > threshold]

    try:

        if not hits_param and not hits_description and not hits_response:
            return None
        elif not hits_param and not hits_response:
            return parameter_dict['['+description_to_param_dict[description_keys[hits_description[0]['corpus_id']]]+']']
        elif not hits_description and not hits_response:
            return parameter_dict[param_keys[hits_param[0]['corpus_id']]]
        elif not hits_param and not hits_description:
            return response_dict[response_keys[hits_response[0]['corpus_id']]]

        if not hits_description:
            if hits_param[0]['score'] > hits_response[0]['score']:
                return parameter_dict[param_keys[hits_param[0]['corpus_id']]]
            else:
                return response_dict[response_keys[hits_response[0]['corpus_id']]]
        elif not hits_param:
            if hits_description[0]['score'] > hits_response[0]['score']:
                return parameter_dict['['+description_to_param_dict[description_keys[hits_description[0]['corpus_id']]]+']']
            else:
                return response_dict[response_keys[hits_response[0]['corpus_id']]]
        elif not hits_response:
            if hits_param[0]['score'] > hits_description[0]['score']:
                return parameter_dict[param_keys[hits_param[0]['corpus_id']]]
            else:
                return response_dict[response_keys[hits_response[0]['corpus_id']]]

        # Return the one with the highest score
        if hits_param[0]['score'] > hits_description[0]['score'] and hits_param[0]['score'] > hits_response[0]['score']:
            return parameter_dict[param_keys[hits_param[0]['corpus_id']]]
        elif hits_description[0]['score'] > hits_param[0]['score'] and hits_description[0]['score'] > hits_response[0]['score']:
            return parameter_dict['['+description_to_param_dict[description_keys[hits_description[0]['corpus_id']]]+']']
        elif hits_response[0]['score'] > hits_param[0]['score'] and hits_response[0]['score'] > hits_description[0]['score']:
            return response_dict[response_keys[hits_response[0]['corpus_id']]]
        
    except Exception as e:
        print(f"Error in search_kb: {e}")
        return None
