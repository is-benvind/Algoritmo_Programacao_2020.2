def main():
    n = int(input(": "))
    i = 1

    while i <= n:
        print(str(int(i)) + " " +str(int(i*i)) + " " + str(int(i*i*i)))
        print(str(int(i)) + " " + str(int(i*i+1)) + " " + str(int(i*i*i+1)))
        i += 1

main()