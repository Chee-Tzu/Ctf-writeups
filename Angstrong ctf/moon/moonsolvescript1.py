from pwn import *
from sage.all import *



e = ELF('./moon',checksec = False)

needed = []
for i in range(1293):
    needed.append(int.from_bytes(e.read(e.sym['needed']+i*8, 8),'little'))

#print(needed)
eq = []

base = 0x400000

check = []
for i in range(1292,1293):
    if i != 1292:
        func = e.disasm(e.sym[f'func{i}'], e.sym[f'func{i+1}']-e.sym[f'func{i}'])
        #print(func)
    else:
        func = e.disasm(e.sym['func1292'],e.sym['main']-e.sym['func1292'])
    ins = func.split('\n')
    eq = []
    i = 3
    while i < len(ins):
        if 'mov' in ins[i] and 'add    rax,' in ins[i+1] and 'mov' in ins[i+2]:
            # print(ins[i+1])
            num = int(ins[i+1].split(',')[1],16)
            eq.append(num)
            i = i + 3
        elif 'mov' in ins[i] and 'sub    rax,' in ins[i+1] and 'mov' in ins[i+2]:
            num = 0xffffffffffffffff - int(ins[i+1].split(',')[1], 16) + 1
            eq.append(num)
            i = i + 3
        elif 'mov' in ins[i] and 'mov' in ins[i+1]:
            eq.append(0)
            i = i + 2 
        else:
            i = i + 1      
    check.append(eq)
#print(eq)

mat = Matrix(check)
mat = mat.T
needed = vector(needed)
print(mat.solve_right(needed))