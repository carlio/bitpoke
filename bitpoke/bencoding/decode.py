

def parse_string(string):
    length = 0
    to_strip = 0

    for c in string:
        to_strip += 1
        if c == ':':
            break
        length = 10 * length + int(c)

    string = string[to_strip:]
    value = string[:length]
    remainder = string[length:]
    return value, remainder


def parse_int(string):
    int_str = []
    for c in string[1:]:
        if c == 'e':
            break
        int_str.append(c)

    remainder = string[2+len(int_str):]  # skip 2 for 'i' and 'e'
    value = int(''.join(int_str))

    return value, remainder


def parse_list(string):
    return inner_parse(string[1:])


def parse_dict(string):
    values, remainder = parse_list(string)
    values = zip(values[::2], values[1::2])
    return dict(values), remainder


_type_map = {
    'i': parse_int,
    'l': parse_list,
    'd': parse_dict
}


def inner_parse(string):
    data = []
    while len(string) > 0:
        first_char = string[0]
        if first_char == 'e':
            return data, string[1:]
        parse_func = _type_map.get(first_char, parse_string)
        val, string = parse_func(string)
        data.append(val)

    return data, ''


def parse(string):
    return inner_parse(string)[0]


if __name__ == '__main__':
    print parse('4:boopi55eli8ei9e1:xed3:qwei4e2:pp2:lle')
