#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print("{}".format("0 arguments."))
    elif argc == 1:
        print("{}".format("1 argument:"))
        print("1: {}".format(argv[1]))
    else:
        print("{:d} {}".format(argc, "arguments"))
        for i in range(1, argc + 1):
            print("{:d}: {}".format(i, argv[i]))
