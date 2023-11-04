import json

x = '{"person1":{"name":"John","age":30,"city":"New York", "friends":["Jackson", "Jeremy", "Giang"], "children":[], "partner":null}}'

def extract_JSON_structure(json_obj, max_chars):
    '''
        json_obj: string of JSON data
        max_chars: max characters we can read in
    '''

    if len(json_obj) > max_chars:
        return False # TODO: should we be checking length this way? This include whitespace in the string
    
    obj = json.loads(json_obj)
    return extract_dict_structure(obj)
    

def extract_dict_structure(obj):
    '''
        obj: dict of data
        max_chars: max characters we can read in
    '''
    for key, value in obj.items():
        obj[key] = get_type(value)
    return obj


def get_type(value):

    if isinstance(value, int) or isinstance(value, float):
        return "num"
    elif isinstance(value, str):
        return "str"
    elif isinstance(value, bool):
        return "bool"
    elif value is None:
        return "null"
    elif isinstance(value, list):
        return get_type_of_list(value)
    elif isinstance(value, dict):
        return extract_dict_structure(value)
    
    return "TYPE NOT IMPLEMENTED YET"
        

def get_type_of_list(lst):
    if len(lst) == 0:
        return "list: empty"
    return "list: " + get_type(lst[0]) # TODO: does this handle lists of objects?

print(extract_JSON_structure(x, 1000))

'''
Issues:
- values can be part of format
    - dates are represented as strings...
    - ints and floats can be represented as strings


'''