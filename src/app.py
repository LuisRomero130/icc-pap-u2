import re
def main():
    #runEjemplo1()
    runEjemplo2()
    #runEjemplo3()

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



if __name__ == "__main__" :


    main()