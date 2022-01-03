from Newton import *

def main():
    while True:
        data = input("Enter a positive number or press Enter exit:) ")

        if data == "":
            print("Have a nice day! :)")
            break

        sqRoot = newton(data)
        print("The square root of your number is:", sqRoot)

main()