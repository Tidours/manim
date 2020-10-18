from manimlib.imports import *
import random
import sys  
import json

POSITIONS = [UL,UP,UR,LEFT,(0,0,0),RIGHT,DL,DOWN,DR]

#TABLES DE MORPIONS
l_morp=[[
    ["X"," ", " " ],
    [" "," ", " " ],
    [" "," ", " " ],
     ]
,[
    ["O"," ", "O" ],
    ["X","X", " " ],
    ["X"," ", "O" ],
     ]
,[
    ["X","X", " " ],
    [" ","O", "X" ],
    ["O","O", " " ],
     ]
,[
    ["O","X", "O" ],
    [" ","X", " " ],
    [" "," ", "O" ],
     ]
]

l_t_morp = VGroup()
for i in range(len(l_morp)):
    l_t_morp.add(Table.get_table(l_morp[i]).move_to(5 * LEFT))

#TABLE DES ETATS
etats=[]

for i in range(9):
    etats.append([str(i+1)])
etats.append(["..."])
for i in range(95,105):
    etats.append([str(i+1)])
etats.append(["..."])
for i in range(782,792):
    etats.append([str(i+1)])


t_etats=Table.get_table(etats,cell_length=2,text_color=WHITE,line_color=WHITE,background_color = BLACK)


#TABLES D'ACTIONS

l_actions=[
[[" "," "," "," "," "," "," "," "," "]],
[[" "," "," "," "," "," "," "," "," "]],
[[" "," "," "," "," "," "," "," "," "]],
[[" "," "," "," "," "," "," "," "," "]]
 ]


l_t_actions = VGroup()
for i in range(len(l_actions)):
    l_t_actions.add(Table.get_table(l_actions[i],cell_length=0.75,cell_height = 0.75,text_color = BLACK).move_to(3 * RIGHT))

#LETTRES INDIQUANT LES POSITIONS

group_letters = VGroup()

for i in range(3):
    for j in range(3):

        nb = Text(chr(64+(j+1)+3*i), color = BLUE, size = 0.5).move_to(j*RIGHT+i*DOWN)
        group_letters.add(nb)

group_letters_2 = group_letters.copy()
#ELEMENTS SUPPLEMENTAIRES

rect = Rectangle(height=1, width= 2, color = DARK_BLUE,stroke_width = 10 ).move_to(2 * LEFT) #RECTANGLE DE SURBRILLANCE

rewards = [
            [1,5,7],
            [1,5,7],
            [1,5,7],
            [1,5,7]
            ]

class Sc6(Scene): #DEFILEMENT DE LA LISTE D ETATS

    def construct(self):

        #TABLE ETATS + MORPION
        self.play(Write(l_t_morp[0]),ApplyMethod(t_etats.shift,2 * LEFT))
        self.wait()

        #RECTANGLE DE SURBRILLANCE
        self.play(Write(rect))
        self.wait()

        # FAIRE APPARAITRE ET BOUGER LES 9 ACTIONS POSSIBLES
        self.play(Write(group_letters.move_to(5 * LEFT + 0.3 * UL )),run_time=1)
        self.add_foreground_mobjects(group_letters_2.move_to(5 * LEFT + 0.3 * UL ))
        self.wait()
        
        #ALLER A L ETAT 100
        self.play(ApplyMethod(t_etats.shift, 14 * UP),
            FadeIn(l_t_morp[1]))
        self.wait()
        

                    #TABLE ACTIONS        
        for i in range(9):
            self.play(ApplyMethod(group_letters[i].move_to, i * 0.75 * RIGHT + 0.9 * UP),run_time=0.4)
        self.wait()
        self.play(Write(l_t_actions[1]))

                    #EVALUER LES ACTIONS POSSIBLES
        joueur = TextMobject("O",color = DARK_BLUE).move_to( 5 * LEFT + 2 * DOWN)
        self.play(Write(joueur))      

        for j in range(0,len(rewards[1])):
            index_to_change = rewards[1][j] - 1
            self.play(ApplyMethod(joueur.move_to, 5 * LEFT + POSITIONS[index_to_change]))
            self.play(ApplyMethod(l_t_actions[1][1][index_to_change].set_color,BLUE))
            self.wait()

        #self.play(FadeOutAndShift(l_t_actions[1],UP))

        #BOUCLE SUR LES ETAPES DE JEU
        for i in range(2,4):

            self.play(ApplyMethod(t_etats.shift, 10 * UP),
            FadeIn(l_t_morp[i]),
            FadeOutAndShift(l_t_actions[i - 1],UP),
            FadeInFrom(l_t_actions[i].move_to(3 * RIGHT),DOWN)
            )

            #self.play()
            self.wait()

            joueur = joueur.copy()
            self.play(Write(joueur.move_to( 5 * LEFT + 2 * DOWN)))      

            for j in range(len(rewards[i])):
                index_to_change = rewards[i][j] - 1
                self.play(ApplyMethod(joueur.move_to, 5 * LEFT + POSITIONS[index_to_change] ))
                self.play(ApplyMethod(l_t_actions[i][1][index_to_change].set_color,BLUE))
                self.wait()


l_actions=[
[["1","1","1","1","1","1","1","1","1"]],
[["1","1","1","1","1","1","1","1","1"]],
[["1","1","1","1","1","1","1","1","1"]],
[["1","1","1","1","1","1","1","1","1"]]
]

l_t_actions = VGroup()
for i in range(len(l_actions)):
    l_t_actions.add(Table.get_table(l_actions[i],cell_length=0.75,cell_height = 0.75 , text_color = BLACK).move_to(3 * RIGHT))

l_pos = [ 2,1,6,9 ]



        
class Sc7(Scene): #PARTIE EXEMPLE

    def construct(self):

        #TABLE ETATS , RECTANGLE DE SURBRILLANCE
        self.add(t_etats.move_to(2 * LEFT),rect,l_t_morp[0])
        self.play(Write(group_letters_2.move_to(5 * LEFT + 0.3 * UL )))

        for i in range(9):
            self.play(ApplyMethod(group_letters_2[i].move_to, i * 0.75 * RIGHT + 0.9 * UP),run_time=0.1)
        self.wait()


                    #EVALUER LES ACTIONS POSSIBLES

        joueur = TextMobject("O",color = DARK_BLUE).move_to( 5 * LEFT + 2 * DOWN)
        self.play(Write(joueur))     

        for i in range(1,4):

            self.play(ApplyMethod(t_etats.shift, 10 * UP),
            FadeIn(l_t_morp[i]))
            if i != 1 :
                self.play(FadeOutAndShift(l_t_actions[i - 1],UP))

            self.play(FadeInFrom(l_t_actions[i].move_to(3 * RIGHT),DOWN))
            self.wait()

            joueur = joueur.copy()
            self.play(Write(joueur.move_to( 5 * LEFT + 2 * DOWN)))      

            pos = l_pos[i]

            self.play(ApplyMethod(l_t_actions[i][1][pos - 1].set_color,GREEN))
            self.play(ApplyMethod(l_t_actions[i][1][pos - 1].set_width,0.3))
            self.play(ApplyMethod(l_t_actions[i][1][pos - 1].set_width,0.15))
            self.play(ApplyMethod(l_t_actions[i][1][pos - 1].set_width,0.3))      

            self.play(ApplyMethod(joueur.move_to, 5 * LEFT + POSITIONS[pos] ))      

class Sc8(Sc7): #PARTIE EXEMPLE

    def construct(self):

        self.add(t_etats.move_to(2 * LEFT),rect,l_t_morp[0])    



class Ex(Scene): #exemple d'utilisation de fonctions scenes

    def construct(self):

        self.show_morp(l_t_morp,0)
        self.move_morp(l_t_morp[0])

    def show_morp(self,obj,i):
        self.play(Write(obj[i]))

    def move_morp(self,obj):
        self.play(ApplyMethod(obj.shift,UP))




#class Sc11(Scene):  PARTIE EXEMPLE EN AJOUTANT LES RECOMPENSES ET LESTIMATION DE RECOMPENSES


#class Sc12(Scene): #Explication de pourquoi ça marche ?




#class Sc12(Scene): #JEU CONTRE LORDI ET GRAPHIQUE DES VICTOIRES/DEFAITES