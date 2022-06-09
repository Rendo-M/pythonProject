# Вводятся моды 2 предметов
# указываются желаемые моды  в 1 и 2 предмете
#
#
#
# Условия налагаемые на вводимые данные:
# В предметах от 0 до 3 модов
# в предметах от 0 до 2 желаемых модов
#
# Генерируем 3 списка модов:
# - 3 мода
# - 2 мода
# - 1 мод
#
# Считаем общее число !разных! желаемых модов - desired_mod_count
# считаем число комбинаций для желаемых модов, количество модов от 1 до max(3,desired_mod_count)
# И генерируем их список
#
#
# Для каждого из элементов списка считаем количество генераций и с учетом веса по числу модов выводим шансы на получение
#
#
# Одинаковые моды блокируют друг друга ( то есть в конечный предмет может попасть только 1 из них)
# Одинаковые моды могут иметь разные тиры (и соответственно "желаемым" может быть только 1 из них)
#
#
# Генерируем список модов
#
#

#    """Read list of mods for recombinator
#    and setup which of them good   """

# Initialisation:
# 0 elem - 0 mod chance, 1 elem - 1 mod chance, 2 elem - 2 mod chance, 3 elem - 3 mod chance
prob = []
prob += [1, 0, 0, 0]  # 0 mods
prob += [1 / 3, 2 / 3, 0, 0]  # 1 mod
prob += [0, 2 / 3, 1 / 3, 0]  # 2 mods
prob += [0, 0.3, 0.5, 0.2]  # 3 mods
prob += [0, 0.1, 0.55, 0.35]  # 4 mods
prob += [0, 0, 0.5, 0.5]  # 5 mods
prob += [0, 0, 0.3, 0.7]  # 6 mods

list3mod = []
list2mod = []
list1mod = []

mod_list1 = []
mod_list2 = []
tier_mod1 = []
tier_mod2 = []
mods1 = []
mods2 = []
# End Initialisation
#
# Input DATA:
print('Первый предмет')
count = int(input('Сколько модов на 1 предмете: '))
i = 0
while i < count:
    i += 1
    mod_list1 += [input('Введите ' + str(i) + ' мод: ')]
    tier_mod1 += [input('Это нужный мод? [y/n]: ')]
print('Второй предмет')
count = int(input('Сколько модов на 2 предмете: '))
i = 0
while i < count:
    i += 1
    mod_list2 += [input('Введите ' + str(i) + ' мод: ')]
    tier_mod2 += [input('Это нужный мод? [y/n]: ')]
mods1 = [0] * len(mod_list1)
mods2 = [0] * len(mod_list2)
#
# End Input DATA
#

i = 0
# приводим список модов удобному виду:

while i < len(mods1):
    j = 0
    i += 1
    if tier_mod1[i - 1] == 'n':
        mods1[i - 1] = i
    elif tier_mod1[i - 1] == 'y':
        mods1[i - 1] = -i
    else:
        print("error: wrong desired flag in 1 item")
    while j < len(mods2):
        if mod_list1[i - 1] == mod_list2[j] and tier_mod2[j] == 'n':
            mods2[j] = i
        elif mod_list1[i - 1] == mod_list2[j] and tier_mod2[j] == 'y':
            mods2[j] = -i
        j += 1

j = 0
while j < len(mods2):
    if mods2[j] == 0:
        i += 1
        if tier_mod2[j] == 'y':
            mods2[j] = -i
        else:
            mods2[j] = i
    j += 1
# /Приводим данные к удобному виду

#
#  Создаем общий пулл модов:
pull = mods1 + mods2
#
# Работаем с набором вероятностей prob[len(pull)]
# Генерируем списки преметов с 3, 2 и 1 модом


# C 3 модами:

i = 0
while i < len(pull):
    j = i + 1
    while j < len(pull):
        k = j + 1
        if abs(pull[i]) == abs(pull[j]):
            j += 1
            continue
        while k < len(pull):
            if (abs(pull[i]) == abs(pull[k])) or (abs(pull[j]) == abs(pull[k])):
                k += 1
                continue
            list3mod += [pull[i], pull[j], pull[k]]
            k += 1
        j += 1
    i += 1


# C 2 модами:

i = 0
while i < len(pull):
    j = i + 1
    while j < len(pull):
        if abs(pull[i]) == abs(pull[j]):
            j += 1
            continue
        list2mod += [pull[i], pull[j]]
        j += 1
    i += 1

# с 1 модом
i = 0
while i < len(pull):
    list1mod += [pull[i]]
    i += 1


# тестовый вывод всех 3-модовых комбинаций
print('3 mod items')
for i in range(0, len(list3mod), 3):
    print('[', list3mod[i], list3mod[i + 1], list3mod[i + 2], ']')
print('2 mod items')
for i in range(0, len(list2mod), 2):
    print('[', list2mod[i], list2mod[i + 1], ']')
print('1 mod items')
print(list1mod)
#
#
#
#
#
#
#

print('base items')
print(mods1)
print(mods2)
desired_pull = []
# create list of unique desired mods
for i in range(len(pull)):
    if pull[i] < 0:
        if pull[i] not in desired_pull:
            desired_pull += [pull[i]]

print('list of desired mods')
print(desired_pull)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
