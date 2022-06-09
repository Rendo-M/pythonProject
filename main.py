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


def print_generated_items():
    # тестовый вывод всех 3-модовых комбинаций
    print('3 mod items')
    for ind in range(0, len(list3mod), 3):
        print('[', list3mod[ind], list3mod[ind + 1], list3mod[ind + 2], ']')
    print('2 mod items')
    for ind in range(0, len(list2mod), 2):
        print('[', list2mod[ind], list2mod[ind + 1], ']')
    print('1 mod items')
    print(list1mod)


#
#
#
#
#
#
#
def print_base_items():
    print('base items')
    print(mods1)
    print(mods2)


desired_pull = []
# create list of unique desired mods
for i in range(len(pull)):
    if pull[i] < 0:
        if pull[i] not in desired_pull:
            desired_pull += [pull[i]]


def print_desired_mods():
    print('list of desired mods')
    print(desired_pull)


# choose probability
weights = []
for i in range(4):
    weights += [prob[len(pull) * 4 + i]]


def print_weights():
    print(weights)


# calculate all event probabilities:
# 3 desired (3 mods)
# 2 desired (3 mods)
# 1 desired (3 mds)

desired33 = 0
prb_desired33 = 0
desired23 = 0
prob_desired23 = 0
desired13 = 0
prob_desired13 = 0
desired03 = 0
prob_desired03 = 0

for i in range(0, len(list3mod), 3):
    if (list3mod[i] < 0) and (list3mod[i + 1] < 0) and (list3mod[i + 2] < 0):
        desired33 += 1
    elif (list3mod[i]) * (list3mod[i + 1]) * (list3mod[i + 2]) < 0:
        desired13 += 1
    elif (list3mod[i] > 0) and (list3mod[i + 1] > 0) and (list3mod[i + 2] > 0):
        desired03 += 1
    else:
        desired23 += 1
prob_desired33 = desired33 / (len(list3mod) / 3)
prob_desired23 = desired23 / (len(list3mod) / 3)
prob_desired13 = desired13 / (len(list3mod) / 3)
prob_desired03 = desired03 / (len(list3mod) / 3)

print('statistics 3 mods')
print('total generations', len(list3mod) / 3, 'chance for 3 mods', round(weights[3] * 100), 'percent')
print('3 desired mod cases', desired33, 'probability = ', round(weights[3] * prob_desired33 * 100), 'percent')
print('2 desired mod cases', desired23, 'probability = ', round(weights[3] * prob_desired23 * 100), 'percent')
print('1 desired mod cases', desired13, 'probability = ', round(weights[3] * prob_desired13 * 100), 'percent')
print('0 desired mod cases', desired03, 'probability = ', round(weights[3] * prob_desired03 * 100), 'percent')
print('**************************************************************************************************************'
      '*************')
# 0 desired (3 mods)


# 2 desired (2 mods)
# 1 desired (2 ods)
# 0 desired (2 mods)


desired22 = 0
desired12 = 0
desired02 = 0
prob_desired22 = 0
prob_desired12 = 0
prob_desired02 = 0

for i in range(0, len(list2mod), 2):
    if (list2mod[i] < 0) and (list2mod[i + 1] < 0):
        desired22 += 1
    elif (list2mod[i] < 0) or (list2mod[i + 1] < 0):
        desired12 += 1
    else:
        desired02 += 1

prob_desired22 = desired22 / (len(list2mod) / 2)
prob_desired12 = desired12 / (len(list2mod) / 2)
prob_desired02 = desired02 / (len(list2mod) / 2)

print('statistics 2 mods')
print('total generations', len(list2mod) / 2, 'chance for 2 mods', round(weights[2] * 100), 'percent')
print('2 desired mod cases', desired22, 'probability = ', round(weights[2] * prob_desired22 * 100), 'percent')
print('1 desired mod cases', desired12, 'probability = ', round(weights[2] * prob_desired12 * 100), 'percent')
print('0 desired mod cases', desired02, 'probability = ', round(weights[2] * prob_desired02 * 100), 'percent')
print('**************************************************************************************************************'
      '*************')
# 1 desired (1 mod)
# 0 desired (1 mod)

desired11 = 0
desired01 = 0
prob_desired11 = 0
prob_desired01 = 0

for i in range(len(list1mod)):
    if list1mod[i] < 0:
        desired11 += 1
    else:
        desired01 += 1

prob_desired11 = desired11 / (len(list1mod))
prob_desired01 = desired01 / (len(list1mod))

print('statistics 2 mods')
print('total generations', len(list1mod), 'chance for 2 mods', round(weights[1] * 100), 'percent')
print('1 desired mod cases', desired11, 'probability = ', round(weights[1] * prob_desired11 * 100), 'percent')
print('0 desired mod cases', desired01, 'probability = ', round(weights[1] * prob_desired01 * 100), 'percent')
print('**************************************************************************************************************'
      '*************')
print('total chance for 0 mods', round(weights[0] * 100), 'percent')

# 0 mods


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
