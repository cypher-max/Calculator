nam= input ("What should we call you? ")
age= int(input ("How old are you? "))

if  age>=18 and age <=24:
    print (f"{nam}, you are eligible to vote")
elif age >= 25:
    print (f"{nam}, you are eligible to vote and run for parliament")
else :
    age = 18 - age
    print (f"{nam}, you are a minor and have to wait {age} years to vote")