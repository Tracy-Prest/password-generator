
import random
import string
# ask user if they want to create a new password
question = input("Do you want to proceed with password generation? (yes/no) \n")
# create a function for generate password
def create_password(length = 12):
    pool = string.ascii_letters + string.digits + string.punctuation # add all possible figures and numbers
    for e in range(length):
       return "".join(random.choice(pool)) 
# loop through till you get the password you want
while True:
   your_password = create_password()
   print(f"Password {your_password}")
# ask user if they are satisfied with that password
   ask = input("\nAre you okay with that password? (yes or no) \n").lower()
   if ask == "yes":
    break
# finalised password
print(f"Your password is {your_password}")

