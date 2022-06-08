# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def calc_chance_recombine (mods_1 , mods_2, needed_mods1, needed_mods_2 ):
#    mods = mods_1 + mods_2
#    for mod_counter in mods:
#        for counter in range(mod_counter,len(mods)+1):            if mods

# Press the green button in the gutter to run the script.
# input data

def read_mods():
    """Read list of mods for recombinator
    and setup which of them good
    """
    mods1 = int(input('Сколько модов на 1 предмете: '))
    i = 0
    while i < mods1:
        i += 1
        mod_list1 += [input('Введите ' + str(i) + ' мод: ')]
        tier_mod1 += [input('Это нужный мод? [y/n]: ')]
    pass



mod_list1 = []
mod_list2 = []
tier_mod1 = []
tier_mod2 = []
print('Первый предмет')
mods1 = int(input('Сколько модов на 1 предмете: '))
i = 0
while i < mods1:
    i += 1
    mod_list1 += [input('Введите '+str(i)+' мод: ')]
    tier_mod1 += [input('Это нужный мод? [y/n]: ')]
print('Второй предмет')
mods2 = int(input('Сколько модов на 2 предмете: '))
i = 0
while i < mods2:
    i += 1
    mod_list2 += [input('Введите '+str(i)+' мод: ')]
    tier_mod2 += [input('Это нужный мод? [y/n]: ')]

print('моды 1 предмета ', mod_list1)
print('Хорошие моды 1 предмета')
i = 0
while i < len(mod_list1):
    if tier_mod1[i] == 'y':
        print(mod_list1[i])
    i += 1
print('моды 2 предмета ', mod_list2)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
