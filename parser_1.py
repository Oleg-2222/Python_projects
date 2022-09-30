def plenty_calculator():

    # Ввод множеств.
    def plenty_input():
        plenty_1 = list(input('Введите первое множество: ').split())
        plenty_2 = list(input('Введите второе множество: ').split())
        return plenty_1, plenty_2

    def binary_relationship_input():
        print('Ввод (для окончания введите 0):')

        binary_relationship = []
        num = 1

        while num != ['0']:
            num = list(input().split())

            if num != ['0']:
                binary_relationship.append(num)

        return  binary_relationship

    # Пересечение.
    def intersection():
        plenty_1, plenty_2 = plenty_input()

        ans = []
        for element_1 in plenty_1:
            if element_1 in plenty_2:
                ans.append(element_1)

        return 'Пересечение:', *ans

    # Объединение.
    def unification():
        plenty_1, plenty_2 = plenty_input()

        ans = []
        for el in plenty_2:
            if el not in plenty_1:
                ans.append(el)

        return 'Объединение:', *plenty_1, *ans

    # Разность.
    def difference():
        plenty_1, plenty_2 = plenty_input()

        ans = []
        for el in plenty_1:
            if el not in plenty_2:
                ans.append(el)

        return 'Разность:', *ans

    # Симметрическая разность.
    def symmetric_difference():
        plenty_1, plenty_2 = plenty_input()

        ans = []
        for el in plenty_1:
            if el not in plenty_2:
                ans.append(el)

        for el in plenty_2:
            if el not in plenty_1:
                ans.append(el)

        return 'Симметрическая разность:', *ans

    # Дополнение.
    def addition():
        plenty_1 = list(input('Введите множество: ').split())

        universal = [i for i in range(-1000, 1000)]
        ans = []
        for el in universal:
            if el not in plenty_1:
                ans.append(el)

        return 'Дополнение:', *ans

    # Декартово произведение.
    def dec_mult():
        plenty_1, plenty_2 = plenty_input()

        ans = []
        for el_1 in plenty_1:
            for el_2 in plenty_2:
                ans.append([el_1, el_2])    

        return 'Декартово произведение:', *ans

    # Обращение.
    def appeal():
        binary_relationship = binary_relationship_input()
        ans = []

        for elem in binary_relationship:
                ans.append(elem[::-1])

        return 'Обращение:', ans

    # Композиция
    def composition():
        ans = []

        print('Введите первое б. о.')
        binary_relationship_1 = binary_relationship_input()

        print('Введите второе б. о.')
        binary_relationship_2 = binary_relationship_input()

        for elem_1 in binary_relationship_1:
            for elem_2 in binary_relationship_2:
                if elem_1[1] == elem_2[0] and [elem_1[0], elem_2[1]] not in ans:
                        ans.append([elem_1[0], elem_2[1]])
        return 'Композиция:', ans
    # Меню
    def menu():
        print('1.Пересечение\n'
              '2.Объединение\n'
              '3.Разность\n'
              '4.Симметрическая разность\n'
              '5.Дополнение\n'
              '6.Декартово произведение\n'
              '7.Обращение\n'
              '8.Композиция\n'
              '9.Выход')

        req = -1
        while True:
            req = int(input('Ввод: '))

            if req == 1:
                ans = intersection()
                return ans

            elif req == 2:
                ans = unification()
                return ans

            elif req == 3:
                ans = difference()
                return ans

            elif req == 4:
                ans = symmetric_difference()
                return ans

            elif req == 5:
                ans = addition()
                return ans

            elif req == 6:
                ans = dec_mult()
                return ans

            elif req == 7:
                ans = appeal()
                return ans

            elif req == 8:
                ans = composition()
                return ans

            elif req == 0:
                break

    return menu()

print(*plenty_calculator())
