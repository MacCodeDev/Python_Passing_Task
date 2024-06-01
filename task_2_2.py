class PowerGenerator:
    def __init__(self, a, n):
        self.a = a
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            result = self.a ** self.i
            self.i += 1
            return result
        else:
            raise StopIteration
        
gen = PowerGenerator(2, 10)
for power in gen:
    print(power) 