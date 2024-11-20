# Example of catching a built in ValueError.
# ValueError occurs when an incompatible type is provided as
# as an argument for a function/method.


def fetch_value():
    global x  # Makes x global
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops! That was not a valid number. Try again...")

def main():
    fetch_value()
    print(f'Value of x: {x}')

if __name__ == '__main__':
    main()
