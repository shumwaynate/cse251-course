import threading 

class Add_Two(threading.Thread):

    #constructor
    def __init__(self, number):
        threading.Thread().__init__(self)
        self.number = number

    def run(self):
        self.result = self.number + 2

    
if __name__ == "__main__":
    test1 = Add_Two(1)
    test2 = Add_Two(5)

    test1.start()
    test2.start()

    test1.join()
    test2.join()

    print(f" test1 = {test1} , test 2 = {test2}")