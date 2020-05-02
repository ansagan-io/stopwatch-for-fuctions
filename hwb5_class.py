import time 

class Stopwatch: 
    def __init__(self, timer = time.perf_counter): 
        self.measured = " "
        self.timer = timer
        self.start_time = None

    def start(self): 
        self.start_time = self.timer() 

    def end(self): 
        end = self.timer() 
        self.measured = f"Функция завершил работу всего за {round(end - self.start_time, 5)} секунд"
    
    def __enter__(self): 
        self.start() 
        return self
    
    def __exit__(self, *args, **kwargs): 
        self.end()

def fibonacci():
    mylist = [1, 2]
    total_even = 2
    while mylist[-1] + mylist[-2] < 4000000:
        a = mylist[-1] + mylist[-2]
        mylist.append(a)
        if (a % 2) == 0:
            total_even = total_even + a
    print(mylist[-1])
    print(total_even)

with Stopwatch() as first: 
    fibonacci() 
      
print(first.measured)