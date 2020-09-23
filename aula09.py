frase = 'Curso em Video Python'
print('frase = "Curso em Video Python"\n')
print('frase[3] = Mostra o elemento 3 da string: ' + frase[3])
print('frase[3:13] = Mostra do elemento 3 até o 13 da string: ' + frase[3:13])
print('frase[:13] = Mostra do inicio até o elemento 13 da string: ' + frase[:13])
print('frase[13:] = Mostra do elemento 13 até o fim da string: ' + frase[13:])
print('frase[1:15] = Mostra do elemento 1 até o elemento 15 da string: ' + frase[1:15])
print('frase[1:15:2] = Mostra do elemento 1 até o 15 da string pulando de 2 em 2: ' + frase[1:15:2])
print('frase[::2] = Mostra do inicio ao fim da string pulando de 2 em 2: ' + frase[::2])

# print("""texto""") = para imprimir o texto inteiro.
print('Oi')
print("""Everyone has their own reasons for learning how to code, but here's
the reality: Not everyone is cut out to be a programmer. While anyone
can learn how to write code, that's not the same as enjoying a long career.
It's entirely possible to be a talented coder and still not be a perfect fit.\n""")
# Caise censsitive
print('frase.count("o") = Mostra quantas vezes o elemento selecionado aparece na string: ', frase.count('o'))
print('len(frase) = Mostra o tamanho da string: ', len(frase))
print('frase.strip() = Remove os espaços do inicio e do fim da string')
print('frase = frase.replace("Python","Android") = Troca o elemento Python pelo elemento Android')
print("print('Curso' in frase) = Testa se o elemento Curso existe na string = ", 'Curso' in frase)
print("print(frase.find('Curso')) = Mostra a posição do elemento 'Curso' na string: ", frase.find('Curso'))
print("pint(frase.upper()) = Altera todos os elementos dentro da string para Maiúsculo: ", frase.upper())
print("pint(frase.lower()) = Altera todos os elementos dentro da string para Minúsculo: ", frase.lower())
print("print(frase.split()) = Divide a string em uma lista separando os elementos em palavras: ", frase.split())