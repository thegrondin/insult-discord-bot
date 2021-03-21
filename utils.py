def format_dict_to_display(names_dict):

    string_result = ""

    for key in names_dict:
        string_result += key + " : " + names_dict[key] + "\n"

    return string_result


def remove_prefix(prefix, string):
    return string.replace(prefix + "_", '')

def bold(text):
  return "**" + text + "**" 