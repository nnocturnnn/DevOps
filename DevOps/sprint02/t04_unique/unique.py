

def make_unique(arg_dict):
    for key in arg_dict:
        arg_dict[key] = sorted(list(set(arg_dict[key])))
    return arg_dict
