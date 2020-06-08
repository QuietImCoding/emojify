import sys

def toemoji(fname, outfile = None):
    with open(fname, 'rb') as infile:
        contents = infile.read()
        barray = []
        for mybyte in contents:
            if mybyte == int('FE', 16):
                barray.append(chr(int('1F914', 16)))
            elif mybyte < 16:
                barray.append(chr(int('1F92' + format(mybyte, 'x'), 16)) )
            else:
                barray.append(chr(int('1F4' + format(mybyte, 'x'), 16)) )
    if outfile is not None:
        with open(outfile, 'w') as ofile:
            ofile.write(''.join(barray))
    else:
        print(''.join(barray))

def fromemoji(fname, outfile = None):
    with open(fname, 'r') as infile:
        contents = infile.read()
        barray = []
        for mybyte in contents:
            if ord(mybyte) < 256: continue
            if ord(mybyte) == (int('1F914', 16)):
                barray.append(int('FE', 16))
            elif format(ord(mybyte), 'x')[:4] == '1f92':
                barray.append(int(format(ord(mybyte), 'x')[4:], 16))
            else:
                nbyte = format(ord(mybyte), 'x')[3:]
                barray.append(int(nbyte, 16))
    if outfile is not None:
        with open(outfile, 'wb') as ofile:
            ofile.write(bytes(barray))
    else:
        print(bytes(barray).decode())

outfile = None if len(sys.argv) < 4 else sys.argv[3]
if len(sys.argv) >= 2:
    if sys.argv[1] == 'to':
        toemoji(sys.argv[2], outfile)
    elif sys.argv[1] == 'from':
        fromemoji(sys.argv[2], outfile)
else:
    print('''Usage:
\tpython3 emojify.py <to/from> <infile> {{outfile}}''')
