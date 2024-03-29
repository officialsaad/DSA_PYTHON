
class fibonacci:
    def __init__(self):
        self.fib_list = []

    def __init__(self, prev1: int, prev2: int, n: int):
        self.fib_list = []
        self.prev1 = prev1
        self.prev2 = prev2
        new_fib = 0
        for i in range(1, n):
            new_fib = self.fibo(self.prev1, self.prev2)
            self.prev2 = self.prev1
            self.prev1 = new_fib
            self.fib_list.append(new_fib)
            print(new_fib)
        print(self.fib_list)

    def fibo(self, prev_1: int, prev_2: int):
        return prev_1 + prev_2


# Testing the Fibonacci Class

print("Testing the Fibonacci Class",)
fib = fibonacci(1, 0, 18)
