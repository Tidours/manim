from manimlib.imports import *
import random
import sys  
import json

etats=[]

for i in range(9):
    etats.append([str(i+1)])
etats.append(["..."])
for i in range(95,105):
    etats.append([str(i+1)])
etats.append(["..."])
for i in range(782,792):
    etats.append([str(i+1)])


morp1=[
    ["X"," ", " " ],
    [" "," ", " " ],
    [" "," ", " " ],
     ]
morp2=[
    ["O"," ", "O" ],
    ["X","X", " " ],
    ["X"," ", "O" ],
     ]
morp3=[
    ["X","X", " " ],
    [" ","O", "X" ],
    ["O","O", " " ],
     ]
morp4=[
    ["O","X", " " ],
    [" ","X", " " ],
    [" "," ", "O" ],
     ]

actions_h=[[]]
for i in range(9):
    actions_h[0].append(str(i+1))

actions=[[]]
for i in range(9):
    actions[0].append(" ")


POSITIONS = [0,UL,UP,UR,LEFT,(0,0,0),RIGHT,DL,DOWN,DR]




class Sc6(Scene): #DEFILEMENT DE LA LISTE D ETATS

    def construct(self):

        t_etats=Table.get_table(etats,cell_length=2,text_color=WHITE,line_color=WHITE,background_color = BLACK)

        #DEF

        group_letters = VGroup()

        for i in range(3):
            for j in range(3):

                nb = Text(chr(64+(j+1)+3*i), color = BLUE, size = 0.5).move_to(j*RIGHT+i*DOWN)
                group_letters.add(nb)

        group_letters_2 = group_letters.copy()


        #t_actions_h = Table.get_table(actions_h,cell_length=1.5,text_color=BLUE,line_color=BLACK,background_color = BLACK)
        #t_actions_h.scale(0.5)

        t_actions = Table.get_table(actions,cell_length=0.75,cell_height = 0.75 ,text_color=WHITE,line_color=WHITE,background_color = BLACK)
       

        rect = Rectangle(height=1, width= 2, color = DARK_BLUE,stroke_width = 10 ) #RECTANGLE DE SURBRILLANCE

        t_morp1=Table.get_table(morp1,text_color=BLACK,line_color=BLACK,background_color = WHITE) #TABLES MORPION
        t_morp2=Table.get_table(morp2,text_color=BLACK,line_color=BLACK,background_color = WHITE)
        t_morp3=Table.get_table(morp3,text_color=BLACK,line_color=BLACK,background_color = WHITE)
        t_morp4=Table.get_table(morp4,text_color=BLACK,line_color=BLACK,background_color = WHITE)

        joueur = TextMobject("O",color = DARK_BLUE) #PION DU JOUEUR

        #TABLE ETATS + MORPION
        self.add(t_etats.move_to(15 * DOWN))
        self.wait()

        self.play(Write(t_morp1.move_to(5 * LEFT)),ApplyMethod(t_etats.shift,2 * LEFT))
        
        #RECTANGLE DE SURBRILLANCE

        self.play(Write(rect.move_to(2 * LEFT)))
        self.wait()

        # FAIRE APPARAITRE ET BOUGER LES 9 ACTIONS POSSIBLES

        self.play(Write(group_letters.move_to(5 * LEFT + 0.3 * UL )),run_time=1)
        self.wait()


        #ALLER A L ETAT 100
        self.play(ApplyMethod(t_etats.shift, 14 * UP),Write(t_morp2.move_to(5 * LEFT)))
        self.wait()

        			#TABLE ACTIONS

        self.play(Write(group_letters_2.move_to(5 * LEFT + 0.3 * UL )))

        for i in range(9):
        	self.play(ApplyMethod(group_letters_2[i].move_to, i * 0.75 * RIGHT + 0.75 * UP),run_time=0.2)
        self.wait()

        self.play(Write(t_actions.move_to(3 * RIGHT)))
					
					#EVALUER LES ACTIONS POSSIBLES

        self.play(Write(joueur.move_to( 5 * LEFT + POSITIONS[2] )))

        self.play(Write(Text(str(1)).move_to( 1 * 0.75 * RIGHT)))
        self.wait()
        self.play(ApplyMethod(joueur.move_to, 4 * LEFT ))
        self.play(Write(Text(str(1)).move_to( 5 * 0.75 * RIGHT)))
        self.wait()
        self.play(ApplyMethod(joueur.move_to, 5 * LEFT + DOWN))
        self.play(Write(Text(str(-1)).move_to( 7 * 0.75 * RIGHT)))
        self.wait()

        self.play(ApplyMethod(joueur.move_to,5 * LEFT + 2 * DOWN))


        #ALLER A L ETAT 787
        self.play(ApplyMethod(t_etats.shift, 10 * UP),Write(t_morp3.move_to(5 * LEFT)))
        self.wait()

					#EVALUER LES ACTIONS POSSIBLES



        joueur = joueur.copy()
        self.play(Write(joueur.move_to( 5 * LEFT + POSITIONS[3] ))) #REMETTRE LE JOUEUR AU PREMIER PLAN
        self.play(ApplyMethod(joueur.move_to, 4 * LEFT ))

        self.play(Write(Text(str(1)).move_to( 1 * 0.75 * RIGHT)))
        self.wait()
        self.play(ApplyMethod(joueur.move_to, 4 * LEFT ))
        self.play(Write(Text(str(-1)).move_to( 5 * 0.75 * RIGHT)))
        self.wait()
        self.play(ApplyMethod(joueur.move_to, 5 * LEFT + DOWN))
        self.play(Write(Text(str(-1)).move_to( 7 * 0.75 * RIGHT)))
        self.wait()

        self.play(ApplyMethod(joueur.move_to,5 * LEFT + 5 * DOWN))

class Sc7(Scene): #DEFILEMENT DE LA LISTE D ETATS

    def construct(self):

        group_letters = VGroup()

        for i in range(3):
            for j in range(3):

                nb = Text(chr(65+(i+1)+3*j), color = BLUE, size = 0.4).move_to(i*RIGHT+j*DOWN)
                group_letters.add(nb)

        self.play(Write(group_letters.move_to((0,0,0))))

        self.play(ApplyMethod(group_letters[0].shift,LEFT))

