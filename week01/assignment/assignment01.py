# TODO import the appropriate threading and thread modules
from cse251 import Log
import threading


# TODO create a global counter
count_global = 0
# TODO create a summing function that to target using the threading module.
def sum_numbers(count_global, number):
    for x in range(1, number):
        sum = count_global + number
        return sum

def get_thread_name():
    thread_name = threading.get_ident()
    return thread_name

def print_module(sum, count_global, thread_name):
    print(f"{thread_name}{sum_numbers}, x = {count_global}, sum = {sum}")
    pass

# TODO create a class that extends the Thread class (make sure you use a constructor and have a run function)
class MyThread(threading.Thread):

    def __init__(self, number):
        threading.Thread.__init__(self)
        print(f"{self.name} is being created")
        self.count_local = 0
        self.number = number

    def print_message(self):
        self.count_local = self.count_local + 1
        print(f"{self.name}, x = {self.count_local}, sum = {self.sum}")
        
    def run(self, number):
        print(f"{self.name} starting")
        for x in range(1, number):
            self.sum = self.count_local + number
        print(f"{self.name} ending")
        return self.sum

# Note: don't change the name of this function or the unit test won't work
def create_threads(number, log):
    ''' number = the range to sum over, so if numbers equals 10, 
        then the sum will be 1 + 2 + ... + 9 + 10 = 45 
    '''
    log.write(f'number={number}')

    # Two ways to create a thread:
    # 1) Create a class that extends Thread and then instantiate that class
    # 2) Instantiate Thread and give it a target and arguments
    t1 = MyThread(number)
    t1.start()
    t1.join()

    t2 = threading.Thread(target = sum , args=(number, ))
    t2.start()
    t2.join()

    # LEAVE THIS so that your code can be tested against the unit test
    # (you can change the name of these variables)
    return t1, t2

# Leave this so that you can run your code without needed to run the unit test.
# Once you believe it is working, run the unit test (challenge01_test.py) to 
# verify that it works against more numbers than 10.
if __name__ == '__main__':
    log = Log(show_terminal=True)
    create_threads(10, log)
