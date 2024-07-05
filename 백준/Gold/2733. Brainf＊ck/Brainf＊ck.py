# acmicpc 2733

t = int(input())


def go(code):
    global pointer, memory, word_idx
    if code == '>':
        pointer = (pointer + 1) % 32768
    elif code == '<':
        pointer = (pointer - 1) % 32768
    elif code == '+':
        memory[pointer] = (memory[pointer] + 1) % 256
    elif code == '-':
        memory[pointer] = (memory[pointer] - 1) % 256
    elif code == '.':
        print(chr(memory[pointer]), end='')
    elif code == '[':
        if memory[pointer] == 0:
            word_idx = teleport[word_idx] - 1
    elif code == ']':
        if memory[pointer] != 0:
            word_idx = teleport[word_idx] - 1


def find_bracket(code):
    te = {}
    save = []
    for idx, c in enumerate(code):
        if c == '[':
            save.append(idx)
        elif c == ']':
            if not save:
                return None
            to = save.pop()
            te[to] = idx
            te[idx] = to
    if save:
        return None
    return te


for test_case in range(1, t+1):
    words = []
    while True:
        line = input()
        if line == 'end':
            break
        ins = list(line)
        comment = ins.index('%') if '%' in ins else len(ins)
        words.extend(ins[:comment])
    words = list(filter(lambda x: x in ['>', '<', '+', '-', '.', '[', ']'], words))[:128000]
    pointer, word_idx = 0, 0
    memory = [0] * 32768
    teleport = find_bracket(words)
    print(f'PROGRAM #{test_case}:')
    if not teleport:
        print('COMPILE ERROR')
        continue
    while word_idx < len(words):
        go(words[word_idx])
        word_idx += 1
    if test_case != t:
        print()
