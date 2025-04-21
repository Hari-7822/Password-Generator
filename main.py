import random

upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ['!', '@', '#', '$', "%", '^', '&', "*", '(', ')', "_", '-', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"', "'", '<', '>', "?", '.', '/' ]

def generate(length) -> str:
    passkey =  upper + lower + numbers + symbols
    password = random.sample(passkey,length)
    return "".join(password)  

def OTPGenerate(length) -> str:
    password = random.sample(numbers,length)
    return "".join(password)  
    