class analisadorLexico:
    def __init__(self,estado, programa):
        self.percorre(estado, programa)
    
    def percorre(self,estado, programa):
        for caracter in range(0,len(programa)):
            estado = self.automato(programa[caracter], estado)
            if not(type(estado) == int):
                print("Result",estado)
                if(estado == ('id', 'posTabela') or estado == ('Numero', 'valor') ):
                    estado = 0
                    estado = self.automato(programa[caracter], estado)
                    if not(type(estado) == int):
                        print('Result', estado)
                        estado = 0
                else:
                    estado = 0
        if(estado == 39):
            print("Result",'Numero', 'valor')
        if(estado == 11):
            print("Result",'id', 'posTabela')
        if(estado == 46):
            print ("Result",'(','id', ',', 'posTabela',')')
        

    def automato(self,caracter,estado):
        if(estado == 0):
            if(caracter == '<'):
                return 1
            if(caracter == ')'):
                return ('pont','Dparen')
            if(caracter == '='):
                return ('opRel','EQ')
            if(caracter == '>'):
                return 5
            if(caracter == '~'):
                return 8
            if(caracter == 'i'):
                return 11
            if(caracter == 't'):
                return 13
            if(caracter == 'w'):
                return 21
            if(caracter == 'f'):
                return 34
            if(caracter == 'c'):
                return 30
            if(caracter == 'd'):
                return 26
            if(caracter == '+'):
                return ('opAritMais')
            if(caracter == '-'):
                return ('opAritMenos')
            if(caracter == '('):
                return ('pont','Lparen')
            if((caracter >='0'  and caracter <= '9')):
                return 39
            if(caracter == '/'):
                return ('opAritDiv')
            if(caracter == '^'):
                return ('opAritExp')
            if(caracter == 'e'):
                return 17
            if(caracter == ' ' or caracter == '\n' ):
                return 0   
            if(caracter != ' '):
                return 46
        if(estado == 1):
            if(caracter == '='):
                return ('opRel', 'LE')
            else:
                return ('opRel', 'LT')
        if(estado == 5):
            if(caracter == '='):
                return ('opRel', 'GE')
            else:
                return ('opRel', 'GT')
        if(estado == 8):
            if(caracter == '='):
                return ('opRel', 'NE')
            else:
                return 'token não reconhecido'    
        if(estado == 11):
            if(caracter == 'n'):
                return 28
            if(caracter == 'f'):
                return ('if')
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
            else:
                return 'id'    
        if(estado == 13):
            if(caracter == 'h'):
                return 14
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 14):
            if(caracter == 'e'):
                return 15
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 15):
            if(caracter == 'n'):
                return ('then')
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 17):
            if(caracter == 'l'):
                return 18
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 18):
            if(caracter == 's'):
                return 19
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 19):
            if(caracter == 'e'):
                return ('else')
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 21):
            if(caracter == 'h'):
                return 22
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 22):
            if(caracter == 'i'):
                return 23
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 23):
            if(caracter == 'l'):
                return 24
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 24):
            if(caracter == 'e'):
                return ('while')
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 26):
            if(caracter == 'o'):
                return ('do')
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 28):
            if(caracter == 't'):
                return ('tipo','int')
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 30):
            if(caracter == 'h'):
                return 31
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 31):
            if(caracter == 'a'):
                return 32
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 32):
            if(caracter == 'r'):
                return ('tipo','char')
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 34):
            if(caracter == 'l'):
                return 35
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 35):
            if(caracter == 'o'):
                return 36
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 36):
            if(caracter == 'a'):
                return 37
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 37):
            if(caracter == 't'):
                return ('tipo','float')
            if(caracter != '=' or caracter != '>' or caracter != '<' or caracter != '^' or caracter != '~' or caracter != '/' or caracter != '*' or caracter != '-' or caracter != '+'):
                return 46
        if(estado == 39):
            if(caracter > '0' and caracter < '9'):
                return 39
            else:
                return('Numero', 'valor')
        if(estado == 46):
            if(caracter == ' ' or caracter == '=' or caracter == '>' or caracter == '<' or caracter == '^' or caracter == '~' or caracter == '/' or caracter == '*' or caracter == '-' or caracter == '+'):
                return ('id', 'posTabela')