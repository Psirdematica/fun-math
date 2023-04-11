# this script is to will find the sum of all even fibonacci values less than a given number

# function to generate the fibonacci values
def fibonacci(n):
    if (n < 0):
        print(f"Can't find the {n}th fibonacci sequence")
    elif (n == 0):
        return 0
    elif (n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


# function to generate the fibonacci sequence


def fibonacci_seq(n):
    fibonacci_list = []
    for i in range(1, n):
        fibonacci_list.append(fibonacci(i))
    return fibonacci_list

# function to generate and sum all even fibonacci values


def fibo_even_sum(fibo_list, limit):
    even_fibo_list = []
    for i in fibo_list:
        if (i < limit and i % 2 == 0):
            even_fibo_list.append(i)
    return even_fibo_list, sum(even_fibo_list)


limit = 4000000
fibo_list = fibonacci_seq(36)
fib_list, fib_sum = fibo_even_sum(fibo_list, limit)
print(
    f"The even fibonacci sequence less than {limit} is \n {fib_list} \n and the sum is {fib_sum}")
