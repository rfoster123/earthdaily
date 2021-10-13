# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:55:05 2021

@author: richi
"""
import argparse

def create_main_list(org, add, delete):
    org.extend(add)
    org = set(org)
    delete = set(delete)
    new_org = org - delete
    new_org = list(new_org)
    
    return new_org


def order(main_list):
    main_list.sort(reverse= True)
    sorted_list = list(sorted(main_list, key = len, reverse=True))
    
    return tuple(sorted_list)


def str_to_list(string):
    new_str = string.replace("[", "").replace("]", "").replace("'", "").replace(" ", "").split(',')
    
    return new_str


def main():
    parser = argparse.ArgumentParser(description='add and delete values from a list, then get the unique values from that list, and finally rearrange the list')
    parser.add_argument("--original", required=True, help='the base/original list to start with')    
    parser.add_argument("--add", required=True, help='the list of values to add to the base/original list')
    parser.add_argument("--delete", required=True, help='the list of values to delete from the base/original list')
    
    args = parser.parse_args()
    original = args.original
    add = args.add
    delete = args.delete
    
    new_org = str_to_list(original)
    new_add = str_to_list(add)
    new_del = str_to_list(delete)
        
    return_val = order(create_main_list(new_org, new_add, new_del))
    
    return return_val


if __name__ == '__main__':
    print(main())