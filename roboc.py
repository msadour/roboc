from classes import *
from function_lib import *

info_player = get_info_player()
nickname = input("veuillez saisir votre pseudo : ")

# Here we check if the user is in the list of users file (we get them position by the level choosed). if the user not
# exist, we create him in the file
if nickname not in info_player.keys():
    print('Bonjour et bienvenue ' + nickname)
    level = choose_level()
    info_player[nickname] = {
        level : {'position' : (2,2), 'is_finish' : False}
    }
    robot = Robot(nickname)
else:
    print('Bonjour, cela fait plaisir de vous revoir ' + nickname + ' !')
    level = choose_level(info_player[nickname])
    if level not in info_player[nickname].keys():
        info_player[nickname][level] = {'position' : (2,2), 'is_finish' : False}
    robot = Robot(nickname, info_player[nickname][level]['position'])

print("Vous avez choisi le niveau '"+ level +"' \n")
labirynth = Labirynth(level, info_player[nickname][level]['position'])
print(labirynth)
direction = choose_direction()
while True:
    if direction != 'q':
        nb_move = choose_nb_move()
        playing = robot.move(direction, int(nb_move), labirynth)
        print('\n')
        print(labirynth)
        if playing == 'win':
            print('Felicitation vous avez terminer le niveau ' + level + ' !')
            print(labirynth)
            info_player[nickname][level] = {'position': (playing[0], playing[1]), 'is_finish' : True}
            save_info_player(info_player)
            break
        direction = choose_direction()
    else:
        print('Votre position sur le niveau '+ level + ' est enregistré')
        try:
            position = playing
        except:
            position = info_player[nickname][level]['position']

        info_player[nickname][level] = {'position': (position[0], position[1]), 'is_finish' : False}
        save_info_player(info_player)
        break



