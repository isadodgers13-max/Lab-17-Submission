# Client code to create triangles and handle exceptions
def get_triangle_two_sides():
    while True:
        try:
            a = input("Enter first side: ")
            b = input("Enter second side: ")
            triangle = RightTriangle(a, b)
            print("Triangle created successfully!")
            print(triangle)
            return triangle
        except Exception as e:
            print(e)
            print("Please try again.\n")

def get_triangle_three_sides():
    while True:
        try:
            a = input("Enter first side: ")
            b = input("Enter second side: ")
            c = input("Enter hypotenuse: ")
            triangle = RightTriangle(a, b, c)
            print("Triangle created successfully!")
            print(triangle)
            return triangle
        except Exception as e:
            print(e)
            print("Please try again.\n")

# Main program flow
if __name__ == "__main__":
    print("=== Right Triangle Creator ===")
    print("\nCreating triangle with two sides...")
    t1 = get_triangle_two_sides()

    print("\nCreating triangle with three sides...")
    t2 = get_triangle_three_sides()

    print("\nAll triangles created successfully!")
