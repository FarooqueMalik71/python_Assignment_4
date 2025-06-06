import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """Generate and print 10 random numbers using a loop."""
    for _ in range(N_NUMBERS):
        num = random.randint(MIN_VALUE, MAX_VALUE)
        print(num)  # Print numbers in one line with space
    
    print()  # New line after all numbers

if __name__ == '__main__':
    main()