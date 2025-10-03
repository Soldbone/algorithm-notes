n = int(input())

def prime_numbers(n):
    arr = [i for i in range(n+1)]
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] != 0:
            for j in range(i*i, n+1, i):
                arr[j] = 0
            
    return [i for i in arr[2:] if arr[i]]

if n != 1:
    prime_list = prime_numbers(n)
    if n in prime_list:
        print(n)
    else:
        i = 0
        while n > 1:
            if n % prime_list[i] == 0:
                n //= prime_list[i]
                print(prime_list[i])
            else:
                i += 1
            