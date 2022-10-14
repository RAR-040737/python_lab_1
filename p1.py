l = ["This", "is", "very", "fantastic"]


def create_string(str_list):
    result_string = ""
    for word in str_list:
        result_string += word + " "
    return result_string


print(create_string(l))
