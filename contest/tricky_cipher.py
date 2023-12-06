import re
import string


def cipher(arr: list[str]) -> hex:
    fio = ''.join(arr[:3])
    first_letter = string.ascii_uppercase.index(fio[0].upper()) + 1
    len_uniq_simbols = len(set(fio))
    day_month = arr[3] + arr[4]
    sum_day_month = sum([int(i) for i in day_month])
    int_ciper = len_uniq_simbols + (sum_day_month * 64) + (first_letter * 256)
    return f'{int_ciper:03X}'[-3:]


def read_file():
    with open('input.txt', 'r') as file:
        length = int(file.readline().strip())
        arr = []
        for line in range(length):
            arr.append(file.readline().strip().split(','))
    return length, arr


def main():
    length, arr = read_file()
    for i in arr:
        print(cipher(i))#, end=' ')


if __name__ == '__main__':
    main()
