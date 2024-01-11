import json

'''
    NOTE: The only issue I see with this is that lists are of the form [item1]. So a list like [1, 2, 3, 4] will be shortened
    to [1]. This makes it seem like it's a list of one element, when it's actually not. We should make a way to indicate that 
    the list continues, or that the element is an example element.
    
    One idea is to make the list shorten to [1, "..."]
'''

def extract_JSON_structure(json_file, max_chars, max_str_len):
    '''
        json_obj: string of JSON data
        max_chars: max characters we can read in
    '''

    json_obj = json.load(json_file)
    json_string = json.dumps(json_obj)

    if len(json_string) > max_chars: # TODO: this should be checked *after* shortening
        return False
    
    return extract_dict_structure(json_obj, max_str_len)
    

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

    new_list = []
    for item in lst:
        new_list.append(get_repr(item, max_str_len))
    return new_list

def get_str_repr(str, max_str_len):
    return str[:max_str_len] + "..."