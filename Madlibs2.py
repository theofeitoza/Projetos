from random import randint
lugar = input(str('Digite um lugar: '))
animal = input(str('Digite um animal: '))
adjetivo = input(str('Digite um adjetivo no plural: '))
objeto = input(str('Digite um objeto: '))

num=randint(1,4)
textos = [f'Você está preso em um {lugar} com um {animal} que tem {adjetivo} garras. Você só tem um {objeto} para se comunicar. O que você diz?',
f'Você está preso em um {lugar} com um {animal} que tem {adjetivo} olhos. Você só tem um {objeto} para se esconder. Onde você vai?',
f'Você está preso em um {lugar} com um {animal} que tem {adjetivo} asas. Você só tem um {objeto} para se libertar. Como você faz?',
f'Você está preso em um {lugar} com um {animal} que tem {adjetivo} dentes. Você só tem um {objeto} para se defender. O que você faz?']

print(textos[num])