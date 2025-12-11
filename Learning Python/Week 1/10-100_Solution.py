#1_Print"Hello, World!"
print("Hello, Wordl! \n I'm Learning the Python Universe,too! ")

#2_Swap two variables
print("This code is made swap variables:D ")
x=str(input("Enter a variable: "))
y=str(input("Enter other variable: "))
print(f"You enter ({x},{y}) respectively. And when it is swaped,they become ({y},{x})")

#2.1
print("Other variation: at the swap variables ")
a=input("Enter a variable: ")
b=input("Enter b variable: ")
print("a,b:",a,",",b)
a, b=b,a

print("The swap: (",a,",",b,")")

#3_Check even or odd
print("This code is checked if the number is even or odd. ")
num=int(input("Enter the number: "))
if num%2==0:
    result="It's even. "
else:
    result="It's odd. "
print(result)

#3.1
number="02468"
print("Does it even or odd? ")
n=input("Enter a the number: ")
if n[-1] in number:
    print("It's even. ")
else:
    print("It's odd. ")

#3.2
print("Does it even or odd? ")
num=int(input("Enter a number: "))
if num&1==0: #if its first bite is 0, it's even.
    print("It's even. ")
else:
    print("It's odd. ")
    
#3.3
print("Does it even or odd? ")
num=int(input("Enter the number: "))
if (num/2).is_integer(): #by using math
    print("It's the even. ")
else:
    print("It's the odd. ")

   
#3.3.4
print("How many even/old numbers until n? ")
cod=input("Choose even or odd: ")
while cod!="even" and cod!="odd":
    cod=input("Choose just even or odd: ")
    
n=int(input("Enter the n : "))
if cod=="even":
    count=0
    for i in range (n+1):
        if i%2==0:
            count+=1
    print(count,"times even")
else:
    c=0
    for k in range (n+1):
        if k%2!=0:
            c+=1 
    print(c,"times odd")

#4_Find factorial(loop)
n=int(input("Enter the n for n!: " ))
fact=1
for i in range (1,n+1):
    fact*=i 
print(fact)

#5_Sum of first N natural numbers 
n=int(input("Enter the n number for sum all of untill n: "))
summ=0
for i in range (n+1):
    summ+=i
print(summ)

#5.1
n=int(input("Enter the n number for sum all of untill n: "))
summ=n*(n+1)/2 #by using guess theorem
print(summ)    
        

#5.2
n=int(input("Enter the n number for sum all of untill n: "))
k=0
total=0
while k!=(n+1):
    total+=k
    k+=1
print(total)

#6_Reverse a string
word=input("Enter a word for reverse: ")
result=word[::-1]
print(result)

#7_Polindrome Check
word=input("Enter a word for cheching whether polindrom: ")
rev=word[::-1]
if word==rev:
    print("True")
else:
    print("False")
    
#7.1
word=input("Enter a word for cheching whether polindrom: ")
for i in range ((len(word)//2)+1):
    if word[0]==word[-1]:
        word=word[1:-1]
        print(word)
   
if len(word)<=1:
    print("True")
else:
    print("False")

#7.2
word=input("Enter a word for cheching whether polindrom: ")
for i in range ((len(word)//2)):
    if word[i]!=word[-i-1]:
        result=False
        break
    else:
        result=True
print(result)
        
#7.3
def is_polindrome(s):
    if len(s)<=1:
        return True
    else:
        return s[0]==s[-1] and is_polindrome(s[1:-1])
    
is_polindrome("abccba")
    
#8_Fibonacchi Series
num=int(input("Which F number do you want?: "))
f=[]
a=1
b=2
while len(f)!=num:
   f.append(a) 
   a,b=b,a+b
    
print(f)

#8.1
def fibo(n):
    a,b=1,2
    f=[]
    for i in range(n):
        f.append(a)
        a,b=b,a+b
    return f
fibo(5)

#8-1
def fibo_recursive(z):
    n=z+1
    if n <= 1:
        return n  
    else:
        return fibo_recursive(z - 1) + fibo_recursive(z - 2)

print(fibo_recursive(5))

#9_Find max of three numbers
def maxx(a,b,c):
    return max(a,b,c)

#9.1
print("Which one is the biggest? ")
n_1=float(input("Enter the first number: "))
n_2=float(input("Enter the second number: "))
n_3=float(input("Enter the third number: "))
big=n_1
if n_2>n_1:
    big=n_2 
if n_3>n_2:
    big=n_3 
print("The biggest is ",big)
    
#9.9.1
numbers=input("Enter numbers with , (for exp: 1,2,3,4): ")
def max_find(numbers):
    index=(float(s.strip()) for s in numbers.split(','))
    maxi= max(index) 
    return maxi

def min_find(numbers):
    index=(float(s.strip()) for s in numbers.split(','))
    mini= min(index)
    return mini
    
def avr_find(numbers):
    index_list=[float(s.strip()) for s in numbers.split(',')]
    # index_list=[]
    # index_list.append(float(index))
    return sum(index_list)/len(index_list)
    
print("The max number: ",max_find(numbers))
print("The min number: ",min_find(numbers))
print("Their average: ",avr_find(numbers))


#10_Check prime number
x=int(input("Enter a number for checking whether prime: "))
c=0
for i in range (1,x+1):
    if x%i==0:
        c+=1

if c==2:
    print("It's prime. ")
else:
    print("It's not prime. ")









































































































