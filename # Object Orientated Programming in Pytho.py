# Object Orientated Programming in Python

from _typeshed import Self
from typing import NewType, NoReturn, Text
from typing_extensions import NotRequired


def hallo():
    print('hallo')


x = 1
print(type(hallo))


y = 'hallo'

print(x+y)

x = 1
y = 3
x+y

# .method
string = 'hallo'
print(string.upper())


class Dog:

    def meow(self, x):
        return x+1

    def bark(self):  # method in the class
        print('bark')

    def __init__(self, name):
        self.name = name
        print(name)


d = Dog()

print(type(d))

d.bark()

print(d.meow(5))


d = Dog("Tim")

d2 = Dog('Bill')

print(d.name)
print(d2.name)


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


d = Dog("Tim", 34)
print(d.get_name())
print(d.get_age())
d2 = Dog('Bill', 12)
print(d2.get_name())
print(d2.get_age())


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Tim", 34)
d.set_age(23)
print(d.get_age())


dogs_name = ["Tim", "Bill"]
dogs_age = [32, 14]


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)


s1 = Student('Tim', 19, 95)
s2 = Student('Bill', 19, 75)
s3 = Student('Jill', 19, 65)


course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)

print(course.get_average_grade())

course.add_student(s3)
print(course.get_average_grade())


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Bark")


# we can change as below
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Cat(Pet):
    def speak(self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Bark")


p = Pet("Tim", 19)
p.show()

c = Cat('Bill', 34)
c.show()

k = Cat('Krating', 15)
k.show()

d = Dog('Jill', 25)
d.show()

k.speak()
d.speak()

# super class inheriten


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Cat(Pet):
    def __init__(self, name, age, color):  # add information from main
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(
            f"I am {self.name} and I am {self.age} years old abd I am {self.color}")


class Dog(Pet):
    def speak(self):
        print("Bark")


c = Cat('Bill', 34, 'Brown')
c.show()


class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name


p1 = Person("tim")
p2 = Person("jill")

Person.number_of_people = 8
print(p2.number_of_people)
Person.number_of_people = 9
print(p1.number_of_people)


class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1


p1 = Person("tim")
print(Person.number_of_people)
p2 = Person("jill")
print(Person.number_of_people)


class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("tim")
p2 = Person("jill")
print(Person.number_of_people_())


def add1():
    pass


def add2():
    pass


class Math:

    @staticmethod
    def add5(x):
        return x + 5


print(Math.add5(5))


# LinkedList
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


my_limked_list = LinkedList(4)
print(my_limked_list.head.value)
print(my_limked_list.tail.value)

# print liked list


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


my_limked_list = LinkedList(4)
my_limked_list.append(2)

print(my_limked_list.head.value)
print(my_limked_list.tail.value)
my_limked_list.print_list()


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# append value
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

# pop to remove tail valure for the linklist
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

# prepend use for adding new varaible at the begining of the list
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

# get the value in linkedlist
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

# set value in specific index
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return True

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for i in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_limked_list = LinkedList(1)
my_limked_list.append(2)
my_limked_list.append(3)
my_limked_list.append(4)

# print(my_limked_list.get(2))


# my_limked_list.prepend(1)

my_limked_list.print_list()

my_limked_list.reverse()


my_limked_list.set_value(1, 4)


my_limked_list.print_list()

print(my_limked_list.remove(2), '\n')


my_limked_list.print_list()


class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxlen = 0
        self.start = 0

        for i in range(len(s)):
            self.expandFromCenter(s, i, i)
            self.expandFromCenter(s, i, i+1)
        return s[self.start:self.start+self.maxlen]

    def expandFromCenter(self, s, l, r):
        while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        if self.maxlen < r-l-1:
            self.maxlen = r-l-1
            self.start = l + 1


solution = Solution()


solution.longestPalindrome('cbbd')

# Doubly Linked List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index - 1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get((index - 1))
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first(value)
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp


my_doubly_linked_list = DoubleLinkedList(7)
my_doubly_linked_list.append(2)
my_doubly_linked_list.prepend(1)

my_doubly_linked_list.print_list()
my_doubly_linked_list.insert(1, 2)

my_doubly_linked_list.set_value(1, 4)

my_doubly_linked_list.remove(1)


print(my_doubly_linked_list.pop())
print(my_doubly_linked_list.pop())
print(my_doubly_linked_list.pop())

print(my_doubly_linked_list.pop_first())
print(my_doubly_linked_list.pop_first())
print(my_doubly_linked_list.pop_first())

print(my_doubly_linked_list.get(1))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_ndoe = Node(value)
        self.top = new_ndoe
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


my_stack = Stack(7)
my_stack.push(1)
my_stack.push(23)
my_stack.push(7)

my_stack.print_stack()

my_stack.pop()

# queue


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(5)

my_queue = Queue(4)

my_queue.print_queue()
my_queue.dequeue()

# HASH TABLE


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None]*size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
            return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


hash_table = HashTable()

hash_table.set_item('bolts', 14000)
hash_table.set_item('washers', 50)
hash_table.set_item('lamber', 70)

hash_table.print_table()

print(hash_table.get_item('bolts'))
print(hash_table.get_item('washers'))
print(hash_table.get_item('aaa'))

print(hash_table.keys())


# hash interview question
# naif approch ---> O(n^2)
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


list1 = [1, 2, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))


def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False


list1 = [1, 3, 8]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))


# Basic Sort
# bobble sort
def bobble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


print(bobble_sort([4, 2, 6, 5, 1, 3]))


# selection sort
def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


print(selection_sort([4, 2, 6, 5, 1, 3]))


# Insertion sort
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


print(insertion_sort([4, 2, 6, 5, 1, 3]))


def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

# Quick sort


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)


my_list = [4, 6, 1, 7, 3, 2, 5]
print(pivot(my_list, 0, 6))
print(my_list)
print(quick_sort([4, 6, 1, 7, 3, 2, 5]))

# Merge sort
# Merge


def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined


print(merge([1, 2, 7, 8], [3, 4, 5, 6]))


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list)/2)
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([3, 1, 4, 2, 8, 5, 4, 6, 7, 9, 1]))


# Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value


my_tree = BinarySearchTree()

print(my_tree.root)


my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)


my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(27))

print(my_tree.contains(17))


print(my_tree.min_value_node(my_tree.root))

print(my_tree.min_value_node(my_tree.root.right))


# Graph
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.print_graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1, 2)

my_graph.print_graph()


my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')

my_graph.remove_edge('A', 'D')


my_graph.remove_edge('A', 'B')


my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')

my_graph.remove_vertex('D')

my_graph.print_graph()


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(selt):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(selt.root)
        return results

    def dfs_post_order(selt):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(selt.root)
        return results

    def dfs_in_order(selt):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(selt.root)
        return results


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())

print(my_tree.dfs_pre_order())

print(my_tree.dfs_post_order())

print(my_tree.dfs_in_order())
