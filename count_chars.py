frase = input()

freq = {}
for i in range(len(frase)):
    if frase [i] == " ":
        continue
    if frase [i] not in freq:
        freq[frase[i]] = 1
    else:
        freq[frase[i]] += 1
    
print(freq)
