def main():
    #write your code below this line
    names = []
    while True:
        name = input()
        if (name == ""):
            break
        else:
            names.append(name)
    search = input("Search for?")
    if search in names:
        print(search + " was found!")
    else:
        print(search + " was not found!")

if __name__ == '__main__':
    main()
