# Example of catching a built in ValueError.
# ValueError occurs when an incompatible type is provided as
# as an argument for a function/method.


def do_calc():
    global x, y, z  # Makes x, y and z global variables
    while True:
        try:
            x = int(input("Please enter first number: "))
            y = int(input("Please enter second number: "))
            if x < 0 or y < 0:
                raise(ValueError())
            z = x / y
        except ValueError:
            print("Oops! Invalid inputs. Try again...")
        except ZeroDivisionError:
            print("Cannot divide by zero. Try again...")
        except:
            print("Something went wrong! :( Try again...")
        else:
            print("Well done - no exceptions raised!")
            break
        finally:
            print("Thank you for using this function today!")

def main():
    do_calc()
    print(f'{x} divided by {y} is {z}')

if __name__ == '__main__':
    main()
