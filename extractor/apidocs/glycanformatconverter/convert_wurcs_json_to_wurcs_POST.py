import requests, json
from urllib.parse import quote

def convert_wurcs_json_to_wurcs(wurcsjson=None):
    """
    Convert WURCS-JSON format to WURCS format.
    
    Args:
        wurcsjson (str): WURCS-JSON format text.
        
    Returns:
        requests.Response: Response object containing the conversion result.
        
    Example:
        >>> wurcsjson = '''{"Composition":{},"WURCS":"","Aglycone":"","Fragments":{},"Repeat":{},"Edges":{"e0":{"Acceptor":{"Position":[4],"Node":"m0","LinkageType":"H_AT_OH"},"Donor":{"Position":[1],"Node":"m1","LinkageType":"DEOXY"},"Probability":{"High":1,"Low":1}},"e1":{"Acceptor":{"Position":[4],"Node":"m1","LinkageType":"H_AT_OH"},"Donor":{"Position":[1],"Node":"m2","LinkageType":"DEOXY"},"Probability":{"High":1,"Low":1}},"e2":{"Acceptor":{"Position":[3],"Node":"m2","LinkageType":"H_AT_OH"},"Donor":{"Position":[1],"Node":"m3","LinkageType":"DEOXY"},"Probability":{"High":1,"Low":1}},"e3":{"Acceptor":{"Position":[6],"Node":"m2","LinkageType":"H_AT_OH"},"Donor":{"Position":[1],"Node":"m4","LinkageType":"DEOXY"},"Probability":{"High":1,"Low":1}}},"AN":"","Bridge":{},"Monosaccharides":{"m0":{"Modifications":[],"TrivialName":["glc"],"Substituents":[{"Status":"simple","Acceptor":{"Position":[2],"LinkageType":"DEOXY"},"Donor":{"Position":[0],"LinkageType":"NONMONOSACCHARIDE"},"Probability":{"High":1,"Low":1},"Notation":"NAc"}],"Configuration":["d"],"SuperClass":"HEX","RingSize":"p","AnomState":"x","AnomPosition":1,"Notation":"GlcNAc"},"m1":{"Modifications":[],"TrivialName":["glc"],"Substituents":[{"Status":"simple","Acceptor":{"Position":[2],"LinkageType":"DEOXY"},"Donor":{"Position":[0],"LinkageType":"NONMONOSACCHARIDE"},"Probability":{"High":1,"Low":1},"Notation":"NAc"}],"Configuration":["d"],"SuperClass":"HEX","RingSize":"p","AnomState":"b","AnomPosition":1,"Notation":"GlcNAc"},"m2":{"Modifications":[],"TrivialName":["man"],"Substituents":[],"Configuration":["d"],"SuperClass":"HEX","RingSize":"p","AnomState":"b","AnomPosition":1,"Notation":"Man"},"m3":{"Modifications":[],"TrivialName":["man"],"Substituents":[],"Configuration":["d"],"SuperClass":"HEX","RingSize":"p","AnomState":"a","AnomPosition":1,"Notation":"Man"},"m4":{"Modifications":[],"TrivialName":["man"],"Substituents":[],"Configuration":["d"],"SuperClass":"HEX","RingSize":"p","AnomState":"a","AnomPosition":1,"Notation":"Man"}}}'''
        >>> response = convert_wurcs_json_to_wurcs(wurcsjson)
    """
    api_url = "https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcsjson2wurcs"
    assert wurcsjson is not None, 'Missing required parameter: wurcsjson'
    
    # The API expects an array of strings, not a JSON object with a wurcsjson key
    payload = [wurcsjson]
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = convert_wurcs_json_to_wurcs(wurcsjson='''{"Composition":{},"WURCS":"","Aglycone":"","Fragments":{},"Repeat":{},"Edges":{"e0":{"Acceptor":{"Position":[4],"Node":"m0","LinkageType":"H_AT_OH"},"Donor":{"Position":[1],"Node":"m1","LinkageType":"DEOXY"},"Probability":{"High":1,"Low":1}},"e1":{"Acceptor":{"Position":[4],"Node":"m1","LinkageType":"H_AT_OH"},"Donor":{"Position":[1],"Node":"m2","LinkageType":"DEOXY"},"Probability":{"High":1,"Low":1}},"e2":{"Acceptor":{"Position":[3],"Node":"m2","LinkageType":"H_AT_OH"},"Donor":{"Position":[1],"Node":"m3","LinkageType":"DEOXY"},"Probability":{"High":1,"Low":1}},"e3":{"Acceptor":{"Position":[6],"Node":"m2","LinkageType":"H_AT_OH"},"Donor":{"Position":[1],"Node":"m4","LinkageType":"DEOXY"},"Probability":{"High":1,"Low":1}}},"AN":"","Bridge":{},"Monosaccharides":{"m0":{"Modifications":[],"TrivialName":["glc"],"Substituents":[{"Status":"simple","Acceptor":{"Position":[2],"LinkageType":"DEOXY"},"Donor":{"Position":[0],"LinkageType":"NONMONOSACCHARIDE"},"Probability":{"High":1,"Low":1},"Notation":"NAc"}],"Configuration":["d"],"SuperClass":"HEX","RingSize":"p","AnomState":"x","AnomPosition":1,"Notation":"GlcNAc"},"m1":{"Modifications":[],"TrivialName":["glc"],"Substituents":[{"Status":"simple","Acceptor":{"Position":[2],"LinkageType":"DEOXY"},"Donor":{"Position":[0],"LinkageType":"NONMONOSACCHARIDE"},"Probability":{"High":1,"Low":1},"Notation":"NAc"}],"Configuration":["d"],"SuperClass":"HEX","RingSize":"p","AnomState":"b","AnomPosition":1,"Notation":"GlcNAc"},"m2":{"Modifications":[],"TrivialName":["man"],"Substituents":[],"Configuration":["d"],"SuperClass":"HEX","RingSize":"p","AnomState":"b","AnomPosition":1,"Notation":"Man"},"m3":{"Modifications":[],"TrivialName":["man"],"Substituents":[],"Configuration":["d"],"SuperClass":"HEX","RingSize":"p","AnomState":"a","AnomPosition":1,"Notation":"Man"},"m4":{"Modifications":[],"TrivialName":["man"],"Substituents":[],"Configuration":["d"],"SuperClass":"HEX","RingSize":"p","AnomState":"a","AnomPosition":1,"Notation":"Man"}}}''')
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))