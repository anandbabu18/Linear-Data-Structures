#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Write a program to find all pairs of an integer array whose sum is equal to a given number?

A = [8,5,9,3,7]
target = 15
findpair(A,target)
def findpair(A, target):
    for i in range(len(A) - 1):
        for j in range (i+1,len(A)):
            if A[i]+A[j] == target:
                print('pair found',(A[i],A[j]))
                return
    print('pair not found')


# In[12]:


#Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

A= [1,2,3,4,5,6]
def reverseList(A, start, end):
    while start < end:
        A[start],A[end] = A[end],A[start]
        start +=1
        end -=1
print(A)
reverseList(A,0,5)
print('Reverse List is',A)


# In[20]:


#Write a program to check if two strings are a rotation of each other?

s1 ='AACD'
s2 ='ACDA'
def areRotations(s1,s2):
    size1 = len(s1)
    size2 = len(s2)
    temp = ''
    if size1 != size2:
        return 0
    temp = s1+s2
    if (temp.count(s2)>0):
        return 1
    else:
        return 0
if areRotations(s1,s2):
    print('Strings are rotations to each other')
else:
    print('Strings are not rotations to each other')


# In[57]:


#Write a program to print the first non-repeated character from a string?

no_of_chars = 256
def getCharCountArray(string):
    count = [0] * no_of_chars
    for i in string:
        count[ord(i)]+=1
    return count
def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k=0
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k +=1
    return index
string = 'ANAND BABU'
index = firstNonRepeating(string)
if index == 1:
    print('Either all characters are repeating or string is empty')
else:
    print('First non-repeating character is',string[index])


# In[37]:


#Read about the Tower of Hanoi algorithm. Write a program to implement it.

def TowerOfHanoi(n,from_rod,to_rod,aux_rod):
    if n == 1:
        print('Move disk 1 from rod',from_rod,'to_rod',to_rod)
        return
    TowerOfHanoi(n-1,aux_rod,to_rod,from_rod)
    print('Move disk',n,'from_rod',from_rod,'to_rod',to_rod)
    TowerOfHanoi(n-1,aux_rod,to_rod,from_rod)
n=2
TowerOfHanoi(n,'A','C','B')


# In[40]:


#Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
def postToPre(post_exp):
    s = []
    length = len(post_exp)
    for i in range(length):
        if (isOperator(post_exp[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1
            s.append(temp)
        else:
            s.append(post_exp[i])
 
    
    ans = ""
    for i in s:
        ans += i
    return ans

if __name__ == '__main__':
    post_exp = "AB+CD-"
    print("Prefix : ", postToPre(post_exp))


# In[54]:


#Write a program to convert prefix expression to infix expression.

def prefixToInfix(prefix):
    stack = []
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False

if __name__ == "__main__":
    str = "*-A/BC-/AKL"
    print('Infix:',prefixToInfix(str))


# In[56]:


#Write a program to reverse a stack.

class Stack:
    def __init__(self):
        self.Elements = []
    def push(self, value):
        self.Elements.append(value)
    def pop(self):
        return self.Elements.pop()
    def empty(self):
        return self.Elements == []
    def show(self):
        for value in reversed(self.Elements):
            print(value)
def BottomInsert(s, value):
    if s.empty():
        s.push(value)
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)
def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)
stk = Stack()
 
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
 
print("Original Stack")
stk.show()
 
print("\nStack after Reversing")
Reverse(stk)
stk.show()


# In[ ]:




