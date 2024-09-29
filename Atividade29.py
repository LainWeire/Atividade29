# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.


lp = []
q = []

while True:
    al = input("Diga o nome de um aluno. Para parar, diga: stop     ")
    lp.append(al)
    q.append(al)

    if al == "stop":
        lp.remove("stop")
        break 

print("Alunos comparecidos: {}".format(len(lp)))
print(lp)

if len(lp)<5:
    print("Poucos alunos compareceram à aula hoje. Por favor, revise a chamada.")
else:
    print("Alunos comparecidos: {}".format(len(lp)))