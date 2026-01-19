def primeCheck(num):
    if num == 1:
        print("1 is neither prime nor composite")
    elif num == 2:
        print("Prime")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")

n = int(input("Enter a number: "))
primeCheck(n)
