import time

foo_letters = ['s', 'l', 'f', 'w', 'k']


# Importa o texto armazenado em uma URL e realiza a conversão para lista
def import_file(url=input('Insert URL: ')):
    import urllib.request
    file = urllib.request.urlopen(url).read().decode('utf-8').split()
    return file


# Verifica quantas preposições existem no arquivo importado
def verify_prepositions(file):
    prepositions = [item for item in file if "d" not in item and len(item) == 3 and item[2] not in foo_letters]
    return prepositions


# Verifica quantos verbos existem no arquivo importado
def verify_verbs(file):
    verbs = [item for item in file if len(item) >= 8 and item[-1] in foo_letters]
    return verbs


# Verifica quantos verbos em primeira pessoa existem no arquivo importado
def verify_first_person_verbs(verbs):
    first_person_verbs = [item for item in verbs if item[0] not in foo_letters]
    return first_person_verbs


# Ordena um texto baseado na ordem lexicografica do alfabeto Klingon
def reorder_text(file):
    alphabet = 'kbwrqdnfxjmlvhtcgzps'
    ordered_text = sorted(file, key=lambda word: [alphabet.index(c) for c in word])
    return ordered_text


# Calcula quantos números bonitos distintos existem no texto
def alphabet_number_values(file):
    alphabet_numbers = {'k': 0, 'b': 1, 'w': 2, 'r': 3, 'q': 4, 'd': 5, 'n': 6, 'f': 7, 'x': 8, 'j': 9, 'm': 10, 'l': 11,
                    'v': 12, 'h': 13, 't': 14, 'c': 15, 'g': 16, 'z': 17, 'p': 18, 's': 19
                    }
    base = {0: 1, 1: 20, 2: 400, 3: 8000, 4: 160000, 5: 3200000, 6: 64000000, 7: 1280000000}
    numbers = []

    for item in file:
        b = 0
        total = 0
        for i in item:
            test = alphabet_numbers[i] * base[b]
            total += test
            b += 1
        if total >= 440566 and total % 3 == 0:
            numbers.append(item)

    return numbers


arquivo = import_file()
preposicoes = verify_prepositions(arquivo)
verbos = verify_verbs(arquivo)
primeira_pessoa = verify_first_person_verbs(verbos)
numeros_bonitos = (alphabet_number_values(arquivo))

print("O texto possui", len(preposicoes), "preposições e", len(verbos), "verbos, dos quais", len(primeira_pessoa), "estão em primeira pessoa")
print("Também possui", len(numeros_bonitos), "números bonitos distintos")

# Ordena o arquivo e ao final gera um txt com o texto formatado
texto_ordenado = reorder_text(arquivo)

print("\nGerando arquivo com o texto ordenado em ordem lexicográfica...")
time.sleep(2)
with open("klingon-texto-ordenado.txt", "w") as txt:
    txt.write(" ".join(texto_ordenado))
print("Arquivo gerado com sucesso!")
