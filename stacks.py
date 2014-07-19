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

# a paranthesis checker
def parChecker(symbolStr):
    stk = Stack()
    for a in symbolStr:
        if a is '(':
            stk.push(a)
        elif a is ')':
            if stk.isEmpty():
                stk.push(a)
            else:
                stk.pop()
    return stk.isEmpty()

# a more generic paranthesis checker
def parCheckerG(symbolStr):
    stk = Stack()
    # create a paren matching dict
    parDict = {'}': '{', ')': '(', ']': '['}
    for a in symbolStr:
        if a in '{[(':
            stk.push(a)
        elif a in '}])':
            if stk.isEmpty():
                stk.push(a)
            else:
                # get last saved left paren
                leftPar = stk.peek()
                # check it matches current right paren
                if leftPar is parDict[a]:
                    stk.pop()
    return stk.isEmpty()

# convert from decimal to binary
def decToBin(val):
    stk = Stack()
    # special case 0
    if val is 0:
        return 0
    # divide by 2 algorithm:
    # loop till div yields 0
    while val//2:
        stk.push(val % 2)
        val = val//2
    # last digit (MSB)
    stk.push(val % 2)
    # pop vals
    strBin = ''
    while not stk.isEmpty():
        strBin += str(stk.pop())
    return strBin

# main() function
def main():
    print('learning stacks...')

    # testing reverseStr
    # print(reverseStr('yomamma'))

    # test parenthesis
    """
    print(parChecker('(()wht))'))
    print(parChecker('( ()yo() (((mama))) )'))
    print(parChecker('(()'))
    print(parChecker(')('))
    """
    # test parenthesis (generic)
    """
    print(parCheckerG('](yo) ] {} ()'))
    print(parCheckerG('(yo) {[(test){0}] )}'))
    """

    # test decToBin
    print(decToBin(25))
    print(decToBin(256))

# call main
if __name__ == '__main__':
    main()
