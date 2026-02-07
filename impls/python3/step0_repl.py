def READ(param):
    return param


def EVAL(param):
    return param


def PRINT(param):
    return param


def rep(param):
    return PRINT(EVAL(READ(param)))


def main():
    while True:
        try:
            input_ = input("user> ")
            print(rep(input_))
        except EOFError:
            print("Exiting!")
            break


if __name__ == "__main__":
    main()
