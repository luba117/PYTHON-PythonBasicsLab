import sys

def list_vs_generator_demo():
    print("\n-- LIST COMPREHENSIONS & GENERATORS --")
    
    # List Comprehension
    square_list =[x**2 for x in range(20) if x % 2 == 0]
    print(f"List Compreesion: {square_list}")

    # Generator Expression
    squares_gen = (x**2 for x in range(20) if x%2 == 0)
    print(f"Generator Object:{squares_gen}")

    # Consuming the generator
    print("Consuming Generator: ", end="")
    for val in squares_gen:
        print(val, end=" ")
    print("\n")

    #Memory Perfomance Demo: Create Large Dataset
    large_range =range(1000000)

    l_comp = [i * 2 for i in large_range]
    g_exp = (i * 2 for i in large_range)

    print(f"Memory (List): {sys.getsizeof(l_comp)} bytes")
    print(f"Memory (Generator): {sys.getsizeof(g_exp)} bytes")
    print("Note: Generators use significantly less memory for large datasets!")

if __name__ == "__main__":
    list_vs_generator_demo()

