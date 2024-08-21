#Task02

#
num=1
while num<=5:
    i=1
    while i<=10:
        n=i*num
        print(f"{i} * {num}={n}")
        if(num==i):
          break
        i+=1
    num+=1


#1 to 10 (multiplication)
num=1
while num<=5:
    i=1
    while i<=10:
        n=i*num
        print(f"{i} * {num}={n}")
        i+=1   
    num+=1 


#01-Write a program that calculates the factorial of a number using a while loop

num=int(input("Enter a number:"))
factorial=1
while num>0:
    factorial=factorial*num
    num-=1
print(factorial)


#02 Write a Python program that uses a while loop to print numbers from 1 to 10.
i=1
while i<=10:
    print(i)
    i+=1
print("Done")


#03) How would you modify the previous program to print only even numbers using a continue statement?
#print even numbers from 1 to 10 using continue statement
i=1
while i<=10:
    if (i%2!=0):
        i+=1
        continue
    print(i)
    i+=1
print("End")    


#04-Create a program that asks the user to enter a password using a while loop. The loop should continue until the correct password is entered and terminate if the user enters 'quit'.

while True:
    password=input("Enter your password")
    if (password=="abc123"):
        print("correct password")
    if (password=="quit"):
        break


#05) Write a program that calculates the sum of the digits of a positive integer the user enters.
i=int(input("Enter a positive integer:"))
sum=0
while i>0:
    sum=sum+i%10
    i=i//10
print(sum)       


#06) Implement a program that calculates the result of raising a base number to an exponent entered by the user. Use a while loop to perform repeated multiplication.
b=float(input("Enter the base:"))
e=int(input("Enter the exponent:"))
i=1
while e>0:
    i*=b
    e-=1
print("result:",i)

    
#07) Write a program to display factors of a positive integer entered by the user. Use a while loop to iterate over potential factors.
while True:
    num=int(input("Enter a number:"))
    i=0
    while i<num:
        i+=1
        if(num%i==0):
            print(i)    
      

