#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = list(map(lambda i: i if i != search else replace,
                       my_list))
    return(my_list)
