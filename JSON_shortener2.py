import json

'''
    NOTE: The only issue I see with this is that lists are of the form [item1]. So a list like [1, 2, 3, 4] will be shortened
    to [1]. This makes it seem like it's a list of one element, when it's actually not. We should make a way to indicate that 
    the list continues, or that the element is an example element.
    
    One idea is to make the list shorten to [1, "..."]
'''

def extract_JSON_structure(json_obj, max_chars, max_str_len):
    '''
        json_obj: string of JSON data
        max_chars: max characters we can read in
    '''

    if len(json_obj) > max_chars:
        return False
    
    obj = json.loads(json_obj)
    return extract_dict_structure(obj, max_str_len)
    

def extract_dict_structure(obj, max_str_len):
    '''
        obj: dict of data
        max_chars: max characters we can read in
    '''
    for key, value in obj.items():
        obj[key] = get_repr(value, max_str_len)
    return obj


def get_repr(value, max_str_len):

    repr = value
    if isinstance(value, str) and len(value) > max_str_len:
        repr = get_str_repr(value, max_str_len)
    elif isinstance(value, list):
        repr = get_list_repr(value, max_str_len)
    elif isinstance(value, dict):
        repr = extract_dict_structure(value, max_str_len)
    
    return repr
        

def get_list_repr(lst, max_str_len):
    if len(lst) == 0:
        return []
    return [get_repr(lst[0], max_str_len)]

def get_str_repr(str, max_str_len):
    return str[:max_str_len] + "..."