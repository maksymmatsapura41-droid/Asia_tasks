class User:
    def __init__(self, username, password):
        self.username = username # public attribute
        self.__password = password # private attribute
        self._protected_field = False # protected attribute

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = new_password
            print("password changed successfully")
        else:
            print("password doesn't match")


user = User("max", "12345")
print(user.__password)