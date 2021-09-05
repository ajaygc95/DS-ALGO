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



def merge_k_lists(lists):
    final_list = []

    for i,j in enumerate(lists):
        while j:
            print(f"{j.data}", end = "-->")
            j = j.next
        print()
        
        



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