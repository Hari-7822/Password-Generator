
import random

upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = [1,2,3,4,5,6,7,8,9,0]

symbols = []

passkey =  upper + lower + numbers + symbols

length = int(input("Enter the length : "))

password = random.sample(passkey,length)

print("Your Password is : ", password)
