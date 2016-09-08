import sys


if __name__ == '__main__':
    file = sys.argv[1]
    memory = [0 for i in range(30000)]

    with open(file) as f:
        pointer = 0
        index = 0
        begin_index = None
        end_index = None

        code = f.read().replace('\n', '')

        while index < len(code):
            if code[index] == '>':
                pointer += 1
                index += 1
            elif code[index] == '<':
                pointer -= 1
                index += 1
            elif code[index] == '+':
                memory[pointer] += 1
                index += 1
            elif code[index] == '-':
                memory[pointer] -= 1
                index += 1
            elif code[index] == '.':
                print(chr(memory[pointer]), end='')
                index += 1
            elif code[index] == '':
                memory[pointer] = input()
                index += 1
            elif code[index] == '[':
                if memory[pointer] > 0:
                    begin_index = index
                    index += 1
                else:
                    index = end_index + 1
            elif code[index] == ']' and begin_index:
                end_index = index
                index = begin_index
            else:
                index += 1
