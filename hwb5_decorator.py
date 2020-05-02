import time

def func_timer(num_runs):
    num_runs = num_runs
    def timer_inner(function):
        def to_be_measured( *args, **kwargs):
            total_time = 0
            for i in range(num_runs):
                start = time.time()
                measured_func = function(*args, **kwargs)
                end = time.time()
                total_time +=(end-start)
            avg_time = total_time/num_runs
            print(f"Функция завершил работу в среднем за {round(avg_time, 4)} секунд")
            return measured_func
        return to_be_measured
    return timer_inner

@func_timer(50)
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

fibonacci()
