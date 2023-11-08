#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
   new_dict = a_dictionary.keys()
   for okey in new_dict:
       if okey == key:
           a_dictionary[okey] = value
           break
   else:
       a_dictionary.update({key : value})
  return (a_dictionary)
