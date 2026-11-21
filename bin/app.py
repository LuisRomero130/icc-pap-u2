import re
def main():
    #runEjemplo1()
    #runEjemplo2()
    runEjemplo3()

def runEjemplo1():
    patron= r"ab*"
    palabras = ["a","ab","abbb","abab","b",""]
    for i in palabras:
        res= re.fullmatch(patron,i)
        print(f"{i}=> {res}")
       

def runEjemplo2():
    regex= "[TO][0-9]{3}"
    list = ["T001","O120","T01","X001","T0001"]
    for i in list:
        res= re.fullmatch(regex,i)
        print(f"{i}=>{res}")

import re

def runEjemplo3():
    texto = "Sensores: T001 reporta 23.5 C ; O001 reporta 12 PERSONAS; T002 reporta -2 C."

    patron = re.compile(r"T[0-9]{3}")

    for i in patron.finditer(texto):
        print(f"Encontrado: {i.group()}, posición: {i.start()}")


if __name__ == "__main__" :


    main()