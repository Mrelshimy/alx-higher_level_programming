#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda i: i if i != search else replace,
                        my_list))
    return(new_list)
