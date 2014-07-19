"""
stacks.py

Description:

stacks related problems from Miller & Ranum.

Author: Mahesh Venkitachalam
Website: electronut.in
"""

class Stack:
    """
    A Stack implementation using a Python list.
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]
    
    def isEmpty(self):
        return len(self.items) == 0

    def print(self):
        print(self.items)


# reverse a string using a stack
def reverseStr(str1):
    stk = Stack()
    for a in str1:
        stk.push(a)
    str2 = ''
    while not stk.isEmpty():
        str2 += stk.pop()
    return str2

# main() function
def main():
    print('learning stacks...')

    # testing reverseStr
    print(reverseStr('yomamma'))

# call main
if __name__ == '__main__':
    main()
