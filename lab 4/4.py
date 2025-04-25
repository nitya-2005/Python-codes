def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_divisors == n

def is_armstrong(n):
    digits = list(map(int, str(n)))
    power = len(digits)
    return n == sum(digit ** power for digit in digits)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    return str(n) == str(n * n)[-len(str(n)):]


number = 153

prime_status = is_prime(number)
perfect_status = is_perfect(number)
armstrong_status = is_armstrong(number)
palindrome_status = is_palindrome(number)
automorphic_status = is_automorphic(number)

print(f"Number: {number}")
print(f"Is Prime? {'Yes' if prime_status else 'No'}")
print(f"Is Perfect? {'Yes' if perfect_status else 'No'}")
print(f"Is Armstrong? {'Yes' if armstrong_status else 'No'}")
print(f"Is Palindrome? {'Yes' if palindrome_status else 'No'}")
print(f"Is Automorphic? {'Yes' if automorphic_status else 'No'}")


