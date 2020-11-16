import random
import os



class create_matrix():

    def args(self):
        print("Введите размерность первой матрицы \nСтрок будет:")
        try:
            arg1 = int(input())
            print("Столбцов будет: ")
            arg2 = int(input())
            arg3=arg2
            print("Столбцов во второй матрице будет: ")
            arg4 = int(input())
            return [arg1, arg2, arg3, arg4]
        except:
            print("Опечаточка. Выхожу в главное меню")
            gui()
        


    def random_matrix(self, strings1, colums1, strings2, colums2):
        matrix1 = []
        matrix2 = []

        for i in range(strings1):
            matrix1.append([])
            for j in range(colums1):
                matrix1[i].append(random.randint(0, 100))

        for i in range(strings2):
            matrix2.append([])
            for j in range(colums2):
                matrix2[i].append(random.randint(0, 100))

        return [matrix1, matrix2]


    def hand_matrix(self, strings1, colums1, strings2, colums2):
        matrix1=[]
        matrix2=[]

        print(f"Вводим построчно первую матрицу:")
        for i in range(strings1):
            matrix1.append([])
            for j in range(colums1):
                print(f"Строка {i+1}, столбец {j+1}")
                try:
                    matrix1[i].append(int(input()))
                except:
                    print("Опечаточка. Перенаправляю в главное меню")
                    gui()

        print(f"Вводим построчно вторую матрицу:")
        for i in range(strings2):
            matrix1.append([])
            for j in range(colums2):
                if flag == 1:
                    j-=1
                    flag = 0
                print(f"Строка {i+1}, столбец {j+1}")
                try:
                    matrix2[i].append(int(input()))
                except:
                    print("Опечаточка. Перенаправляю в главное меню")
                    gui()

        return [matrix1, matrix2]


    def multiplication(self, matrix1, matrix2, strings1, colums2):
        total = []
        for i in range(strings1):
            total.append([])
            for j in range(colums2):
                total[i].append(0)

        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len( matrix2)):
                      total[i][j] +=  matrix1[i][k] *  matrix2[k][j]

        return total

    global count
def gui():   
    create = create_matrix()
    global strings1, colums1, strings2, colums2, n, matrix1, matrix2
    
    print("1 - Указать размерности матриц \n2 - Сгенерировать рандомные матрицы \n3 - Ввести матрицы ручками \n4 - Перемножаем матрицы")
    try:
        n = int(input())       
    except:
        print("Опечаточка. Повторим.")
        gui()
    if n!=1 and n!=2 and n!=3 and n!=4:
        print("Опечаточка. Повторим.")
        gui()

    try:    
        if n==1:
            [strings1, colums1, strings2, colums2] = create.args()
            gui()

        if n==2:
            [matrix1, matrix2] = create.random_matrix(strings1, colums1, strings2, colums2)
            print("Матрица 1: ")
            for i in range(strings1):
                for j in range(colums1):
                    print ( "{:4d}".format(matrix1[i][j]), end = " " ) 
                print("\n")

            print("Матрица 2: ")
            for i in range(strings2):
                for j in range(colums2):
                    print ( "{:4d}".format(matrix2[i][j]), end = " " ) 
                print("\n")

            gui()

        if n==3:
            [matrix1, matrix2] = create.hand_matrix(strings1, colums1, strings2, colums2)
            print("Матрица 1: ")
            for i in range(strings1):
                for j in range(colums1):
                    print ( "{:4d}".format(matrix1[i][j]), end = " " ) 
                print("\n")

            print("Матрица 2: ")
            for i in range(strings2):
                for j in range(colums2):
                    print ( "{:4d}".format(matrix2[i][j]), end = " " ) 
                print("\n")

            gui()

        if n==4:
            matrix = create.multiplication(matrix1, matrix2, strings1, colums2)
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    print ( "{:4d}".format(matrix[i][j]), end = " " ) 
                print("\n")

            gui()
    except:
        print("Сначала генерим размерности, затем матрицы, и только потом умножаем.")
        gui()

        

if __name__ == "__main__":
    gui()

