def find_key(source_dictionary, target_string):
    if target_string in source_dictionary:
        return True
    for key in source_dictionary:
        if isinstance(source_dictionary[key], dict):
            if find_key(source_dictionary[key], target_string):
                return True
    return False





# def find_key(source_dictionary, target_string):
#     match = False
#     if target_string in source_dictionary:
#         match = True
#     for key in source_dictionary:
#         if isinstance(source_dictionary[key], dict):


#             if target_string in source_dictionary[key]:
#                 match = True
#             for nested_key in source_dictionary[key]:
#                 if isinstance(source_dictionary[key][nested_key], dict):
#                     if target_string in source_dictionary[key][nested_key]:
#                         match = True
#                     for nested_nested_key in source_dictionary[key][nested_key]:
#                         if isinstance(source_dictionary[key][nested_key][nested_nested_key], dict):
#                             if target_string in source_dictionary[key][nested_key][nested_nested_key]:
#                                 match = True


#     return match
