import glob

arr_c = glob.glob('../src/*.cpp')
arr_h = glob.glob('../src/*.h')
arr_j = glob.glob('../starJavaGUI_Linux/src/*.java')

def readLines(indata):
    with open(indata,'r') as rdr:
        ct = 0
        for line in rdr:
            ct += 1
        print('{} LINES IN FILE - {}'.format(ct,indata))
        return ct
    return 0

ctr = 0

for a in arr_c:
    ctr += readLines(a)

for a in arr_h:
    ctr += readLines(a)

for a in arr_j:
    ctr += readLines(a)

print('TOTAL SRC CODE LINES: {}'.format(ctr))

