import random
import string

print("welcome the password Generator")
def main():
 length=int(input("Enter the password length : "))
 lower0=string.ascii_lowercase
 upper1=string.ascii_uppercase
 digit=string.digits
 sym=string.punctuation
 combine=(lower0+upper1+digit+sym)
 x=random.sample(combine,length)
 password="".join(x)
 print(password)
 main()
main() 
