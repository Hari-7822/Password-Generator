
import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lower = "abcdefghijklmnopqrstuvwxyz"

numbers = "1234567890"

passkey =  upper + lower + numbers

length = int(input("Enter the length : "))

password = random.sample(passkey,length)

print("Your Password is :  ", password)
