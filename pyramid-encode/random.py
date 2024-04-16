import sys


def get_row_idx(idx_list, row):
    last_elem = -1
    last_elem_idx = int(((row * (row + 1)) / 2) - 1)
    if len(idx_list) >= last_elem_idx:
        last_elem = idx_list[last_elem_idx]
    return int(last_elem)


def decode():
    all_words = {}

    with open('encode.txt', 'r') as fd:
        line = fd.readline()
        while len(line) > 0:
            kv = line.split()
            all_words[kv[0]] = kv[1]
            line = fd.readline()

    idx_list = sorted(all_words.keys())

    decoded_msg = ""
    curr_row = 1
    next_idx = 0
    while len(idx_list) >= next_idx and next_idx != -1:
        decoded_msg = decoded_msg + all_words[idx_list[next_idx]] + " "
        curr_row += 1
        next_idx = get_row_idx(idx_list, curr_row)

    return decoded_msg


def main():
    print(decode())
    return 0


if __name__ == '__main__':
    sys.exit(main())
