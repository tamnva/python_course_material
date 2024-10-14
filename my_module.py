
# Function to sum two numbers
def sum_two_numbers(a:float, b:float) -> float:
    result = a + b
    return result

# Function to count from 1 to n or n to 1
def count_n(n:int, count_down:bool=True) -> None:
    if count_down:
        for i in reversed(range(1, n + 1, 1)):
            print(i)
    else:
        for i in range(1, n + 1, 1):
            print(i)
            
    return


# Call the function
# count_n(10, False)
# count_n(count_down=False, n=10)

if __name__ == "__main__":
    import sys
    count_n(int(sys.argv[1]))
    
    
    