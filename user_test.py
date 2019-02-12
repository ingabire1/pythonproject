import unittest # Importing the unittest module
from user import user# Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("details","username","password") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_details.names,"Muriuki James")
        self.assertEqual(self.new_username,"0712345678")
        self.assertEqual(self.new_password,"james@ms.com")


if __name__ == '__main__':
    unittest.main()


 def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_details.save_details()
            test_username = Username("Test","user","0712345678","test@user.com") # new user
            test_passowrd.save_password()

#             self.new_details.delete_details()# Deleting a user object
#             self.assertEqual(len(username.username_list),1)
# if __name__ == '__main__':
#     unittest.main()
