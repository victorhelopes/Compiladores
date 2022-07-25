import analisadoLexico as Lexico

arquivo = open('programa.txt', 'r')
programa = arquivo.read()
Lexico.analisadorLexico(0, programa)