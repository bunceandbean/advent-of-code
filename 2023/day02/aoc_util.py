keep = "rbg0123456789;\n:"

def strip_non_alpha(line):
    return ''.join([i for i in line if not i.isalpha()])

def strip_up_to(line, ch):
    return line[line.index(ch) + 1:]

def str_arr_int(line):
    return list(map(int, line.split(',')))

def in_str(thing):
    return thing in keep

def cut_down(content, keep, rep, rep_with):
    if rep:
        return ''.join(filter(in_str, content)).replace(rep, rep_with).split("\n")[:~0]
    return ''.join(filter(in_str, content)).split("\n")[:~0]