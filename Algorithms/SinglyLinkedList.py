#!/bin/python3


import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def merge(arr1, arr2):
    dummy = SinglyLinkedListNode(0)
    final = dummy #Final is just temp , this means that you can are just pointing l1 to different node by sorting

    if not arr1:
        return arr2
    if not arr2:
        return arr1
    while arr1 and arr2:
        if arr1.data <= arr2.data:
            # print(final.data, "-->", arr1.data)
            final.next = arr1
            arr1 = arr1.next
        else:
            # print(final.data, "-->", arr2.data)
            final.next = arr2
            arr2 = arr2.next
        final = final.next  # This one is moving Node(0) to arr1(whole thing)


    if arr1:
        # print(final.data, "-->", arr1.data)
        final.next = arr1

    else:
        # print(final.data, "-->", arr2.data)
        final.next = arr2

    while final :
        final = final.next
    return final


def merge_k_lists(lists):
    size = len(lists)-1
    if size <=1:
        return lists
    mid = size//2

    l,r = merge_k_lists(lists[:mid]), merge_k_lists(lists[mid:])

    return merge(l,r)


if __name__ == '__main__':
    fptr = sys.stdout

    lists_count = int(input().strip())

    lists = []
    for _ in range(lists_count):
        n = int(input().strip())
        if n == 0:
            lists.append(None)
            input()
            continue
        numbers = list(map(int, input().rstrip().split()))
        new_list = SinglyLinkedList()
        for i in range(n):
            new_list.insert_node(numbers[i])
        
        lists.append(new_list.head)

    result = merge_k_lists(lists)

    print_singly_linked_list(result, ' ', fptr)
    fptr.write('\n')

    fptr.close()