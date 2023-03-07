import sys

def Word(filename):
    f = open(filename, 'rU')
    for line in f:
        print(line)


def main():
    Word(sys.argv[1])

if __name__ == __name__:
    main()
