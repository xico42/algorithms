import sys
import random


def make_input(input_size, input_filename):
    file = open(input_filename, 'w+')

    for _ in range(input_size):
        number = random.randint(0, 99999999999999)
        file.write("%d\n" % number)

    file.close()


def parse_input(input_filename):
    return [int(number) for number in open(input_filename, 'r')]


def main():
    make_input(sys.argv[1], 'input.txt')


if __name__ == '__main__':
    main()
