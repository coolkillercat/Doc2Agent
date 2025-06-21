import requests
import json
from urllib.parse import quote

def generate_glycan_image(format="png", type="html", wurcs=None, verify=True):
    """
    Generate a glycan image based on WURCS notation.
    
    Args:
        format (str): Image format, either 'png' or 'svg'. Default is 'png'.
        type (str): Response type, one of 'html', 'json', or 'binary'. Default is 'html'.
        wurcs (str): WURCS format text (required).
        verify (bool): Whether to verify SSL certificates. Default is True.
    
    Returns:
        Returns a glycan image generated from WURCS notation in the specified format (PNG or SVG) and response type.
    Example:
        >>> response = generate_glycan_image(
        ...     format="png",
        ...     type="html",
        ...     wurcs="WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
        ... )
    """
    api_url = "https://api.glycosmos.org/wurcs2image/1.25.0"
    
    # Validate required parameters
    assert wurcs is not None, 'Missing required parameter: wurcs'
    assert format in ['png', 'svg'], 'Format must be either "png" or "svg"'
    assert type in ['html', 'json', 'binary'], 'Type must be one of "html", "json", or "binary"'
    
    payload = {
        'format': format,
        'type': type,
        'wurcs': wurcs
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(
        url=api_url,
        json=payload,
        headers=headers,
        timeout=50,
        verify=verify
    )
    
    return response

if __name__ == '__main__':
    r = generate_glycan_image(
        format="png",
        type="html",
        wurcs="WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
    )
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))