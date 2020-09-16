# IMPORT
import builds
import function
"""import colorama
from colorama import init, Fore, Back, Style"""
# IMPORT 

# VARIABLES
map_houses = ['#', '#', '#', '#']
    # ICONS
playr_icon_TownHall = builds.default_icon_TownHall
playr_icon_Mine = builds.default_icon_Mine
playr_icon_Temple = builds.default_icon_Temple
playr_icon_Wall = builds.default_icon_Wall
palyr_icon_Defence = builds.default_icon_Defence
    #ICONS

do_var = ''

    # SAYS
playr_say = ['>> ', '-> ', '=> ', '- ']
playr_say_i = 0
NPS_say = ['/- ', 'I- ', '-: ']
NPS_say_i = 2
    # SAYS


# VARIABLES

#init(autoreset=True)
map_houses[0] = builds.default_icon_TownHall

while True:
    do_var = input(playr_say[playr_say_i])
    
    if do_var == 'options':
        print('\n', NPS_say[NPS_say_i] + 'Choose what you want.')
        print('1) ...')
        print('а всё')
        continue
    
    elif do_var == 'map':
        function.print_map(map_houses, playr_say, playr_say_i, NPS_say, NPS_say_i)

    else:
        function.oops(a)

        
# playr_say, playr_say_i, NPS_say, NPS_say_i
