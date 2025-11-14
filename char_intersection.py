frase1 = input()
frase2 = input()

palavras1 = set(frase1.split())
palavras2 = set(frase2.split())

intersecao = palavras1.intersection(palavras2)

normal = []
pontuacao = []

for p in intersecao:
    if p == "?":
        pontuacao.append(p)
    else:
        normal.append(p)

normal.sort()

resultado = normal + pontuacao

print(" ".join(resultado))
