

def encode_int(val):
    return 'i%de' % val


def encode_string(val):
    return '%d:%s' % (len(val), val)


def encode_list(val):
    encoded = map(encode, val)
    encoded = ''.join(encoded)
    return 'l%se' % encoded


def encode_dict(val):
    encoded = []
    for k, v in val.iteritems():
        encoded.append(encode(k))
        encoded.append(encode(v))
    encoded = ''.join(encoded)

    return 'd%se' % encoded


def encode(val):
    if isinstance(val, basestring):
        return encode_string(val)
    if isinstance(val, (list, tuple)):
        return encode_list(val)
    if isinstance(val, dict):
        return encode_dict(val)
    if isinstance(val, int):
        return encode_int(val)
    raise ValueError("Cannot encode type %s" % type(val))


if __name__ == '__main__':
    encode()