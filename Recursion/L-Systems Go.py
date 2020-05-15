#https://dmoj.ca/problem/ecoo19r1p2

f = open("DATA21.txt", "r")

def turnAxiom(T, axiom):
    if T == 0:
        return axiom
    else:
        tempA = ""
        for that in axiom:
            if that in rules:
                tempA+=rules[that]
        return turnAxiom(T-1, tempA)
for _ in range(10):
    data = list(f.readline().split())
    rules = {}
    tempA = ""
    R = int(data[0])
    T = int(data[1])
    A = data[2]
    for i in range(R):
        one, two = f.readline().split()
        rules.update({one:two})

    print((turnAxiom(T, A))[0] + (turnAxiom(T, A))[-1], len(turnAxiom(T, A)))
