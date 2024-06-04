from caesarcipher import caesar

def caesar_file(inp_file, out_file, key, enc):
    with open(inp_file, 'r') as inp:
        text = inp.read()
        m = caesar(enc, text, key)
    with open(out_file, 'w') as out:
        out.write(m)


