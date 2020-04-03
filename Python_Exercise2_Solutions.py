#!/usr/bin/env python
# coding: utf-8

# In[2]:


###################################################################################################################
#Function Name : identifyNumber
#Function Desc : This helps in Identifying a number which is divisble by 7 and multiple of 5
###################################################################################################################
def identifyNumber(start,end):
    for element in range(start,end):
        if element%7==0 and element%5==0:
            print(element)


# GETTING THE INPUTS AT RUNTIME
start = int(input("Enter the Start Number:"))
end = int(input("Enter the End Number:"))


# FUNCTION CALLING BY PASSING 2 ARGUMENTS
identifyNumber(start,end)

    


# In[11]:


###################################################################################################################
#Function Name : starPrinting
#Function Desc : This prints star in a particular pattern
###################################################################################################################
def starPrinting(max_value):
    for i in range (0, max_value):
        for j in range(0, i + 1):
            print("*", end=' ')
        print("\r")

    for i in range (max_value, 0, -1):
        for j in range(0, i -1):
            print("*", end=' ')
        print("\r")
    
    
# FUNCTION CALLING BY PASSING the maximum star to be printed
maximum_star = int(input("Enter max star to be display on single line"))
starPrinting(maximum_star)


# In[1]:


###################################################################################################################
#Function Name : findEvenOdd
#Function Desc : This helps in finding even and odd numbers between given range of numbers
###################################################################################################################
def findEvenOdd(startRange,endRange):
    # INITIALIZING VARIABLES WITH VALUES AS 0
    even = 0
    odd = 0
    
    for element in range(startRange,endRange):
        if(element%2==0):
            even=even+1 # INCREMENTING THE EVEN VARIABLE
        else:
            odd=odd+1 # INCREMENTING THE ODD VARIABLE
    print("Total Even Numbers =>",even)
    print("Total Odd Numbers =>",odd)



# GETTING INPUTS AT RUNTIME
start = int(input("Enter the Start Number:"))
end = int(input("Enter the End Number:"))

# FUNCTION CALLING
findEvenOdd(start,end)


# In[2]:


###################################################################################################################
#Function Name : isAllEvenDigits
#Function Desc : This helps in finding whether all the digits of a number is even or not
###################################################################################################################
def isAllEvenDigits(number):
    temp_storage = number
    flag = True
    while number>0:
        digit = int(number%10)
        if digit%2!=0:
            flag = False
        number = int(number/10)
        
    if flag == True:
        return True



# GETTING INPUTS AT RUNTIME
start = int(input("Enter the Start Number:"))
end = int(input("Enter the End Number:"))


# ITERATING FROM START RANGE TO END RANGE
for element in range(start,end):
    result = isAllEvenDigits(int(element))
    if result == True:
        print(element)
    


# In[3]:


###################################################################################################################
#Function Name : calculateDogsAge
#Function Desc : This helps in calculating Dog's Age
###################################################################################################################
def calculateDogsAge(age):
    output = 0
    for element in range(1,age+1):
        if element==1 or element==2:
            output = output+10.5
        else:
            output = output+4
        
    return output


# FETCHING AGE AS RUNTIME INPUT
input_age = int(input("Enter the Age : "))

# CALLING THE FUNCTION
result = calculateDogsAge(input_age)

# PRINTING THE RESULT
print(int(result))


# In[4]:


###################################################################################################################
#Function Name : maxNumber
#Function Desc : This helps in finding maximum of 3 numbers
###################################################################################################################
def maxNumber(num1,num2,num3):
    if(num1==num2 and num1==num3 and num2==num3):
        return "nothing"
    elif(num1>num2 and num1>num3):
        return num1
    elif(num2>num1 and num2>num3):
        return num2
    else:
        return num3
    
# FETCHING 3 NUMBERS AS RUNTIME INPUT
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

# CALLING THE MAX FUNCTION
max_number = findMax(num1,num2,num3)
if max_number == "nothing":
    print("All are equal")
else:
    print("The Max Number is : ",max_number)


# In[5]:


###################################################################################################################
#Function Name : isPrime
#Function Desc : This helps in finding whether a given number is prime or not
###################################################################################################################
def isPrime(num):
    flag = True
    for element in range(2,num):
        remainder = num%element
        if remainder==0:
            flag = False
        
    if flag==True:
        print("Its a prime number")
    else:
        print("Its not a prime number")


    
# FETCHING THE INPUT AT RUNTIME AND CALLING THE FUNCTION
number = int(input("Enter a Number : "))
if number==0 or number==1:
    print("It is neither prime nor composite")
else:
    isPrime(number)


# In[1]:


###################################################################################################################
#Function Name : upperAndLowerCaseCalculation
#Function Desc : This helps in finding the number of upper and lower case letters in a given String
###################################################################################################################
def upperAndLowerCaseCalculation(word):
    lcase = 0
    ucase = 0
    others = 0
    for element in range(0,len(word)):
        if int(ord(str(word[element])))>96 and int(ord(str(word[element])))<123:
            lcase = lcase+1
        elif int(ord(str(word[element])))>64 and int(ord(str(word[element])))<91:
            ucase = ucase+1
        else:
            others = others+1
            
    print("Number of Lower case Letters :- ",lcase)
    print("Number of Upper case Letters :- ",ucase)
    print("Number of Other Characters :- ",others)
    
    
# FETCHING INPUT AT RUNTIME
input_string = str(input("Enter a String : "))

# CALLING THE FUNCTION
upperAndLowerCaseCalculation(input_string)


# In[2]:


###################################################################################################################
#Function Name : reverse
#Function Desc : This helps in reversing the given String
###################################################################################################################
def reverse(input_string):
    rev = ""
    for element in range(len(input_string)-1,-1,-1):
         rev = rev+input_string[element]
    
    print(rev)
    
    
# FETCHING INPUT AT RUNTIME
input_value = str(input("Enter the String : "))

# CALLING THE FUNCTION
reverse(input_value)


# In[3]:


###################################################################################################################
#Function Name : findGCD
#Function Desc : This helps in finding the GCD of 2 numbers
###################################################################################################################
def findGCD(num1,num2):
    temp=1
    while(temp<=num1 and temp<=num2):
        if num1%temp==0 and num2%temp==0:
            result=temp
        temp=temp+1
    
    return result


# FETCHING INPUTS AT RUNTIME
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

# CALLING FUNCTION
result = findGCD(num1,num2)
print(result)


# ##### 
