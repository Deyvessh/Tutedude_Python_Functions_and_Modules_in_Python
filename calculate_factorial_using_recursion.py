
# Factorial

# 0! = 1
# 1! = 1 * 0! = 1 * 1 = 1
# 2! = 2 * 1! = 2 * 1 = 2
# 3! = 3 * 2! = 3 * 2 = 6
# 4! = 4 * 3! = 4 * 6 = 24
# 5! = 5 * 4! = 5 * 24 = 120

def factoraial(n):
    if n < 2:
        return 1
    else:
        return n * factoraial(n - 1)
    
sample_number = int(input('Enter a number: '))
output = factoraial(sample_number)
print(f'Factorial of {sample_number} is: {output}')
    