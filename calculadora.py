# Simple command-line calculator

import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def main():
    print("Calculadora básica. Introduzca una operación como '2 + 2'.")
    try:
        while True:
            entrada = input('> ')
            if entrada.lower() in {'salir', 'exit', 'quit'}:
                print('Saliendo...')
                break
            try:
                izquierda, operacion, derecha = entrada.split()
                izquierda = float(izquierda)
                derecha = float(derecha)
                if operacion not in ops:
                    print(f"Operación no soportada: {operacion}")
                    continue
                resultado = ops[operacion](izquierda, derecha)
                print("=", resultado)
            except ValueError:
                print("Formato no válido. Use: número operación número")
            except ZeroDivisionError:
                print("Error: división por cero")
    except KeyboardInterrupt:
        print('\nSaliendo...')


if __name__ == '__main__':
    main()
