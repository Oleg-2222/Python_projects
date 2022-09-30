def programm():
    users_plenty = list(input('Введите множество городов: ').split())
    used = []

    # Все города, начинающиеся на букву "C".
    def let_c():
        letter_C = []

        for city in users_plenty:
            if city[0] == 'С' and city not in used:
                letter_C.append(city)
                used.append(city)

        return letter_C

    # Все города, оканчивающиеся на букву "а".
    def let_a():
        ended_with_A = []

        for city in users_plenty:
            if city[-1] == 'а' and city not in used:
                ended_with_A.append(city)
                used.append(city)

        return ended_with_A

    # Все города, в названии которых есть буквы "В" / "в".
    def let_b():
        there_is_a_letter_B = []

        for city in users_plenty:
            if ('в' in city or 'В' in city) and city not in used:
                there_is_a_letter_B.append(city)
                used.append(city)

        return there_is_a_letter_B

    return let_c(), let_a(), let_b()


# Саратов Санкт-Петербург Самара Москва Киев Львов Актау
c, a, b = programm()
print('Все города, начинающиеся на букву "C": ', *c)
print('Все города, оканчивающиеся на букву "а": ', *a)
print('Все города, в названии которых есть буквы "В" / "в": ', *b)