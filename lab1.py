import numpy


def lab1(path):
    #Логические значения таблиц, которые считываем из файла
    #материалы
    m = True
    #стоимость
    c = False
    #план
    p = False
    #Списки с данными для матриц
    materials = []
    cost = []
    plan = []
    count_materials = 0
    count_product = 0

    try:
        file = open(path)
        for line in file:
            if m:
                if line == "Матрица материалов:\n":
                    continue
                if line == "Матрица стоимости:\n":
                    m = False
                    c = True
                    continue
                line = line.split()
                if count_materials == 0:
                    count_materials = len(line)
                    materials.append(list(int(i, 10) for i in line))
                elif count_materials == len(line):
                    materials.append(list(int(i,10) for i in line))
                else:
                    file.close()
                    return "Матрица материалов не верна"
                    #m = True
                    #c = False
                    #p = False
                    #materials = []
                    #count_materials = 0
                    #break
            count_product = len(materials)
            if c:
                line = line.split()
                if count_materials == len(line):
                    cost = list(int(i, 10) for i in line)
                    c = False
                    p = True
                    continue
                else:
                    file.close()
                    return "Матрица стоимости не верна"
                    #m = True
                    #c = False
                    #p = False
                    #materials = []
                    #cost = []
                    #count_materials = 0
                    #count_product = 0
                    #break
            if p:
                if not plan:
                    plan.append([])
                if line == "План выпуска:\n":
                    continue
                line = line.split()
                if line:
                    if count_product > len(plan):
                        if line:
                            plan[0].append(int(line[0], 10))
                    else:
                        file.close()
                        return "План введен не верно"
                        #m = True
                        #c = False
                        #p = False
                        #materials = []
                        #cost = []
                        #plan = []
                        #count_materials = 0
                        #count_product = 0
                        #break
        if materials:
            file.close()
            file = open(path, 'a')
            #работа с матрицами
            materials = numpy.array(materials)
            cost = numpy.array(cost)
            plan = numpy.array(plan)
            plan = plan.transpose()
            #Расчет потребности материала
            matrix = materials * plan
            file.write("Матрица потребности материала:\n")
            result = ""
            for i in matrix.sum(axis=0).tolist():
                result+=str(i)+" "
            result += "\n"
            file.write(result)
            #Расчет стоимости единицы продукции
            matrix = materials * cost
            file.write("Матрица стоимости единицы изделия:\n")
            result = ""
            for i in matrix.sum(axis=1).tolist():
                result += str(i) + "\n"
            file.write(result)
            #Расчет общей стоимости
            file.write("Общая стоимость:\n")
            file.write(str(matrix.sum()))
            file.close()
            return "Успешно!"
    except FileNotFoundError:
        return "Файл не найден!"
    except ValueError:
        return "В полученных данных ошибка"


#lab1("/home/anikitaev/1")