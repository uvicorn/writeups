# Pass DEBUG as argument to see all client-server interaction: python3 crossword_template.py DEBUG
import z3
import pwn

ops = {
  "+": "+", 
  "-": "-", 
  "*": "*", 
  "/": "//",
  '=': '==',
}


def process_equations(expressions):
    s = z3.Solver()
    for expression in expressions:
        tokens = expression.split()
        stack = []
        for token in tokens:
            if token in ops:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = f"({arg2}) {ops[token]} ({arg1})"
                stack.append(result)
            else:
                stack.append(token)
        res = stack.pop()
        while True:
            try:
                res = eval(res)
                break
            except Exception as e:
                var =  repr(e).replace("' is not defined\")",'').replace('NameError("name \'','')
                exec(f'{var} = z3.Int("{var}")')
        s.add(res)
    print(s.check())
    m = s.model()
    print(m)
    final = []
    for i in range(1, len(m)+1):
        final.append(m[eval(f'x{i}')])
    return ''.join(map(lambda x: chr((x).as_long()), final))


def solve():
    r = pwn.remote('109.233.56.90', 11542)

    r.recvline()
    
    while True:
        print()

        line = r.recvline().decode().strip()
        print(line)

        if not line.startswith("Crossword"):
            return

        count = int(line.split()[4])
        
        lines = []
        for _ in range(count):
            lines.append(r.recvline().decode().strip())
        
        print("Equations:", lines)
        result = process_equations(lines)
        print("Result:", result)

        r.sendline(result)


if __name__ == "__main__":
    solve()
