from abc import ABC, abstractmethod

class loginfeature(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
class webapp(loginfeature):
    def login(self):
        print("You are logged in Successfully")
    def logout(self):
        print("You are logged out Successfully")
s1=webapp()
s1.login()

