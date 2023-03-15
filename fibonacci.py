num = int(input())

{}

def fibonacci(n):
	#complete the recursive function

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(num):
    print(fibonacci(i))

fibonacci(num)
