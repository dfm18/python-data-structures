from dfm18.collections import Array, Grid, Node, Stack
from dfm18.collections.lists import SinglyLinkedList, DoublyLinkedList
from dfm18.collections.queues import ListBasedQueue

import random


def print_separator():
    print("-" * 60)


def main():
    print_separator()
    # Array
    array = Array(5, 0) # Array of five ints
    for i in range(len(array)):
        array[i] = i * 2
    
    print(array)
    print("Length:", len(array))
    print("Item at index 4:", array[4])
    print("Iterator:", iter(array))
    
    print_separator()
    # Grid
    grid = Grid(4, 5)
    grid.random_fill(10, 200)
    
    print("Grid dimensions:", grid.get_dimensions())
    print(grid)
    
    print_separator()
    # Node
    head: Node[int] = None
    for count in range(5):
        head = Node(count, head)
    
    while head != None:
        print(head.data)
        head = head.next
    
    print_separator()
    # Singly Linked List
    singly_linked_list = SinglyLinkedList()
    
    for i in range(10):
        singly_linked_list.append(i)
    
    print(singly_linked_list)
    singly_linked_list.search(2)
    singly_linked_list.search(5)
    singly_linked_list.delete(5)
    singly_linked_list.search(5)
    print(singly_linked_list)
    singly_linked_list.append_to_start(143)
    print("'143' append to start:", singly_linked_list)
    singly_linked_list.insert(2, 2232134234)
    print("'2232134234' append to index '2':", singly_linked_list)
    singly_linked_list.replace_index(2, 347812)
    print("'2' index element replaced to '347812':", singly_linked_list)
    singly_linked_list.delete_end()
    print('deleted end:', singly_linked_list)
    
    print_separator()
    # Doubly Linked Lists
    doubly_linked_list = DoublyLinkedList()
    
    for _ in range(20):
        doubly_linked_list.append(random.randint(0, 100))
    
    print(doubly_linked_list)
    doubly_linked_list.search(20)
    doubly_linked_list.search(11)
    doubly_linked_list.delete(5)
    doubly_linked_list.delete(20)
    doubly_linked_list.search(20)
    print(doubly_linked_list)
    doubly_linked_list.append_to_start(222)
    print("'222' append to start:", doubly_linked_list)
    doubly_linked_list.delete_end()
    print('deleted end:', doubly_linked_list)
    
    print_separator()
    # Stack
    stack = Stack[str]()
    
    stack.push("asedad")
    stack.push("dadd")
    stack.search("dadd")
    stack.search("c")
    print("Last in, first out: ", stack.pop())
    print("Top data: ", stack.peek())
    stack.clear()
    print("Stack cleared")
    
    print_separator()
    # List Based Queue
    lb_queue = ListBasedQueue[str]()
    
    for c in ['a', 'b', 'c']:
        lb_queue.enqueue(c)
    
    lb_queue.traverse()
    
    print("First letter in the queue: ", lb_queue.unqueue())
    
    lb_queue.traverse()
    
    print_separator()


if __name__ == "__main__":
    main()
