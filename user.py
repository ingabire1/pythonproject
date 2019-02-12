
class User:
    """
    Class that generates new instances of user.
    """

    def __init__(names,phone_number,email):

      # docstring removed for simplicity
    
#         self.last_name = username
#         self.phone_number =login
#         self.email = password

# from hashlib import md5
# from getpass import getpass
# import sys

print("Hello!") 

attempts = 0
check_username ="A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z"
check_password = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,"
# These hashes have been generated earlier on.
# This is not how you would go about storing usernames and passwords,
# but for the sake of simplicity, we'll do it like this.
attempts=0
while attempts<3:
    username = input("Username: ")
    password = getpass("Password: ")
    # Getpass will not echo input to the screen, so your password remains 
    # invisible
    print()

username=input('username?')
password=input('password?')
if username=='correctusername'and password=='correctpassword':
    print('you are in!')
else:
    attempts+=1
    print('incorrect!')
if attempts==3:
    print('too many attempts')

    print("Username and password entered correctly.")
         # Username and password match - do something here

else:
    print("Username entered incorrectly.")
    attempts += 1


