# Solution for swap sorter problem

my_list = ['gnu', 'aardvark', 'horse', 'donkey', 'eagle', 'emu']

for i1 in range(len(my_list) - 1):
    for i2 in range(len(my_list) - 1):
        if my_list[i2].lower() > my_list[i2 + 1].lower():
            tmp1 = my_list[i2]
            tmp2 = my_list[i2 + 1]
            my_list[i2] = tmp2
            my_list[i2 + 1] = tmp1

print(my_list)
