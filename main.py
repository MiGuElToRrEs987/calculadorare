import re

def calcular(entrada):
    partes = re.findall(r'[a-zA-Z0-9.]+|[-+*/^()]', entrada)
    tokens = []
    for parte in partes:
        if parte.isdigit() or parte.replace('.', '', 1).isdigit():
            tokens.append(float(parte))
        else:
            tokens.append(parte)
    if len(tokens) < 3 or not any(isinstance(token, float) for token in tokens):
        raise ValueError("Expresión no válida")
    resultado = evaluar_expresion(tokens)
    return resultado

def evaluar_expresion(tokens):
    prioridades = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    salida = []
    pila = []
    
    for token in tokens:
        if isinstance(token, float):
            salida.append(token)
        elif token == '(':
            pila.append(token)
        elif token == ')':
            while pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()
        else:
            while (pila and pila[-1] != '(' and
                   prioridades.get(token, 0) <= prioridades.get(pila[-1], 0)):
                salida.append(pila.pop())
            pila.append(token)
    
    while pila:
        salida.append(pila.pop())
    
    resultado = evaluar_postfix(salida)
    return resultado

def evaluar_postfix(salida):
    pila = []
    for token in salida:
        if isinstance(token, float):
            pila.append(token)
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ValueError("División por cero")
                pila.append(a / b)
            elif token == '^':
                pila.append(a ** b)
    return pila[0]

def main():
    entrada = input("usa * para multiplicar , / para dividir , ^ para potencia , + para sumar y - para restar ,Ingrese la expresión matemática: ")
    
    try:
        resultado = calcular(entrada)
        print("Resultado:", resultado)
    except ValueError as e:
        print("ERROR!")
        print("Error:", e)

if __name__ == "__main__":
    main()
