n = int(input())
gornja = list(map(int, input().split()))
donja = list(map(int, input().split()))
k = int(input())

debljina = [1] * n

def presavini(gornja, donja, debljina, smjer, duljina):
    if smjer == "L":
        gornja_nova = donja[:duljina][::-1]
        donja_nova = donja[duljina:]
        
        debljina_nova = []
        for j in range(min(duljina, len(debljina) - duljina)):
            debljina_nova.append(debljina[duljina + j] + debljina[duljina - 1 - j])

        if 2*duljina < len(gornja):
            gornja_nova += gornja[2*duljina:]
            debljina_nova += debljina[2*duljina:]
        elif 2*duljina > len(gornja):
            donja_nova += gornja[:2*duljina - len(gornja)][::-1]
            debljina_nova += debljina[:2*duljina - len(debljina)][::-1]
        
    elif smjer == "R":
        gornja_nova = donja[len(donja) - duljina:][::-1]
        donja_nova = donja[:len(donja) - duljina]

        debljina_nova = []
        for j in range(min(duljina, len(debljina) - duljina)):
            debljina_nova.insert(0, debljina[-duljina - 1 - j] + debljina[-duljina + j])

        if 2*duljina < len(gornja):
            gornja_nova = gornja[:-2*duljina] + gornja_nova
            debljina_nova = debljina[:-2*duljina] + debljina_nova
        elif 2*duljina > len(gornja):
            donja_nova = gornja[2*len(gornja) - 2*duljina:][::-1] + donja_nova
            debljina_nova = debljina[2*len(gornja) - 2*duljina:][::-1] + debljina_nova
    
    return (gornja_nova, donja_nova, debljina_nova)

for i in range(k):
    ulaz = input().split()
    smjer = ulaz[0]
    duljina = int(ulaz[1])

    gornja, donja, debljina = presavini(gornja, donja, debljina, smjer, duljina)

minimum = sum(gornja)

for smjer1 in ["L", "R"]:
    for duljina1 in range(1, len(gornja)):
        gornja1, donja1, debljina1 = presavini(gornja, donja, debljina, smjer1, duljina1)

        if minimum > sum(gornja1):
            minimum = sum(gornja1)

        for smjer2 in ["L", "R"]:
            for duljina2 in range(1, len(gornja1)):
                gornja2, donja2, debljina2 = presavini(gornja1, donja1, debljina1, smjer2, duljina2)

                if minimum > sum(gornja2):
                    minimum = sum(gornja2)

print(len(gornja))
print(max(debljina))
print(sum(gornja))
print(minimum)
