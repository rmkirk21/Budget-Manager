# class to modify and create accounts
# 9/1/2020


class Login():
    """ Log in """
    def __init__(self, username, password):
        self.user = username
        self.password = password
        self.test()

    def test(self):
        print(self.user)
        print(self.password)

    # create
    # modify
    # delete
    pass