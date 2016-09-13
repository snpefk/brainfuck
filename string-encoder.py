import sys


def generate_init_loop(values):
    return '++++++++++[{body}{end}-]'.format(body=''.join('>' + '+' * value for value in values), end='<' * len(values))


if __name__ == '__main__':
    s = sys.argv[1]

    init_values = set([ord(c) // 10 for c in s])
    init_value_map = list(init_values)

    current_index = -1
    current_leftover = {}
    chars = []

    for c in s:
        buf = ''
        ascii_value = ord(c)
        index = init_value_map.index(ascii_value // 10)
        leftover = ascii_value % 10

        if index not in current_leftover:
            current_leftover[index] = 0

        if index != current_index:
            shift = '>' if index > current_index else '<'
            buf += shift * abs(index - current_index)

        if leftover != current_leftover[index]:
            shift = '+' if leftover > current_leftover[index] else '-'
            buf += shift * abs(leftover - current_leftover[index])

        buf += '.'
        current_index, current_leftover[index] = index, leftover
        chars.append(buf)

    print(generate_init_loop(init_values), ''.join(chars), sep='')
