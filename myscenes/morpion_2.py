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
    ["O","X", "O" ],
    [" ","X", " " ],
    [" "," ", "O" ],
     ]

actions=[[]]
for i in range(9):
    actions[0].append(" ")


POSITIONS = [0,UL,UP,UR,LEFT,(0,0,0),RIGHT,DL,DOWN,DR]


group_letters = VGroup()

for i in range(3):
    for j in range(3):

        nb = Text(chr(64+(j+1)+3*i), color = BLUE, size = 0.5).move_to(j*RIGHT+i*DOWN)
        group_letters.add(nb)

group_letters_2 = group_letters.copy()


class Sc6(Scene): #DEFILEMENT DE LA LISTE D ETATS

    def construct(self):

        t_etats=Table.get_table(etats,cell_length=2,text_color=WHITE,line_color=WHITE,background_color = BLACK)

        #DEF

        group_rewards = VGroup()

        group_rewards.add(Text(str(1)).move_to( 1 * 0.75 * RIGHT))
        group_rewards.add(Text(str(1)).move_to( 5 * 0.75 * RIGHT))
        group_rewards.add(Text(str(-1)).move_to( 7 * 0.75 * RIGHT))
 

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
        self.play(ApplyMethod(t_etats.shift, 14 * UP),FadeIn(t_morp2.move_to(5 * LEFT)))
        self.wait()

        			#TABLE ACTIONS

        self.play(Write(group_letters_2.move_to(5 * LEFT + 0.3 * UL )))

        for i in range(9):
        	self.play(ApplyMethod(group_letters_2[i].move_to, i * 0.75 * RIGHT + 0.9 * UP),run_time=0.2)
        self.wait()

        self.play(Write(t_actions.move_to(3 * RIGHT)))
					
					#EVALUER LES ACTIONS POSSIBLES

        self.play(Write(joueur.move_to( 5 * LEFT + POSITIONS[2] )))

        self.play(Write(group_rewards[0]))
        self.wait()
        self.play(ApplyMethod(joueur.move_to, 4 * LEFT ))
        self.play(Write(group_rewards[1]))
        self.wait()
        self.play(ApplyMethod(joueur.move_to, 5 * LEFT + DOWN))
        self.play(Write(group_rewards[2]))
        self.wait()


        #ALLER A L ETAT 787
        self.play(ApplyMethod(t_etats.shift, 10 * UP),
        	FadeIn(t_morp3.move_to(5 * LEFT)),
        	FadeOutAndShift(t_actions,UP),
        	FadeOutAndShift(group_rewards,UP)
        	)

        self.play(FadeInFrom(t_actions.move_to(3 * RIGHT),DOWN))
        self.wait()

					#EVALUER LES ACTIONS POSSIBLES


        joueur = joueur.copy()
        self.play(Write(joueur.move_to( 5 * LEFT + POSITIONS[3] ))) #REMETTRE LE JOUEUR AU PREMIER PLAN
        self.play(ApplyMethod(joueur.move_to, 4 * LEFT ))

        self.play(Write(group_rewards[0]))
        self.wait()
        self.play(ApplyMethod(joueur.move_to, 4 * LEFT ))
        self.play(Write(group_rewards[1]))
        self.wait()
        self.play(ApplyMethod(joueur.move_to, 5 * LEFT + DOWN))
        self.play(Write(group_rewards[2]))
        self.wait()

        self.play(ApplyMethod(joueur.move_to,5 * LEFT + 5 * DOWN))

class Sc7(Scene): #PARTIE EXEMPLE

    def construct(self):

        t_etats=Table.get_table(etats,cell_length=2,text_color=WHITE,line_color=WHITE,background_color = BLACK)

        #DEF

        group_letters = VGroup()

        for i in range(3):
            for j in range(3):

                nb = Text(chr(64+(j+1)+3*i), color = BLUE, size = 0.5).move_to(j*RIGHT+i*DOWN)
                group_letters.add(nb)

        group_letters_2 = group_letters.copy()

        group_rewards = VGroup()

        group_rewards.add(Text(str(1)).move_to( 1 * 0.75 * RIGHT))
        group_rewards.add(Text(str(1)).move_to( 5 * 0.75 * RIGHT))
        group_rewards.add(Text(str(-1)).move_to( 7 * 0.75 * RIGHT))
 

        t_actions1 = Table.get_table([["1","1","1","1","1","1","1","1","1"]],cell_length=0.75,cell_height = 0.75 ,text_color=WHITE,line_color=WHITE,background_color = BLACK)
        t_actions2 = Table.get_table([["1","1","1","1","1","1","1","1","1"]],cell_length=0.75,cell_height = 0.75 ,text_color=WHITE,line_color=WHITE,background_color = BLACK)
        t_actions3 = Table.get_table([["1","1","1","1","1","1","1","1","1"]],cell_length=0.75,cell_height = 0.75 ,text_color=WHITE,line_color=WHITE,background_color = BLACK)
        t_actions4 = Table.get_table([["1","1","1","1","1","1","1","1","1"]],cell_length=0.75,cell_height = 0.75 ,text_color=WHITE,line_color=WHITE,background_color = BLACK)
       

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

        
        self.play(Write(t_actions1.move_to(3 * RIGHT)))
        for i in range(9):
        	self.play(Write(group_letters_2[i].move_to( i * 0.75 * RIGHT + 0.9 * UP)),run_time=0.1)

        self.play(Write(group_letters.move_to(5 * LEFT + 0.3 * UL )),run_time=1)


        self.wait()



        #ALLER A L ETAT 100
        self.play(ApplyMethod(t_etats.shift, 14 * UP),
        	Write(t_morp2.move_to(5 * LEFT)),
        	FadeOutAndShift(t_actions1,UP),
            FadeInFrom(t_actions2.move_to(3 * RIGHT),DOWN))

        self.wait()

        				#SURBRILLANCE REWARD MAXIMUM

        self.play(ApplyMethod(t_actions2[1][2].set_color,GREEN))
        self.play(ApplyMethod(t_actions2[1][2].set_width,0.3))
        self.play(ApplyMethod(t_actions2[1][2].set_width,0.15))
        self.play(ApplyMethod(t_actions2[1][2].set_width,0.3))

        self.wait()

        				#LES DEUX JOUEURS JOUENT


class Sc8(Scene): #VUE D'ENSEMBLE DE TOUTE LA TABLE 

    def construct(self):





        etats_1=[]

        for i in range(9):
          etats_1.append([str(i+1)])
        etats_1.append(["..."])
        for i in range(5474,5478):
          etats_1.append([str(i+1)])



        t_etats_1=Table.get_table(etats_1,cell_length=2,text_color=WHITE,line_color=WHITE,background_color = BLACK).move_to(2 * LEFT + 7 * DOWN)


        group_etats_actions = VGroup()
        for i in (range(9) + range (10,14)) :
        	group_etats_actions.add(Table.get_table([["1","1","1","1","1","1","1","1","1"]]).move_to(( i + 0.5) * DOWN + 2 * RIGHT).scale(0.5))

        group_etats_actions.add(t_etats_1)
        


        self.wait()


        self.play(FadeIn(group_etats_actions))
        self.wait()


        def f_anim_1(vg):
          vg.move_to(2 * LEFT )
          vg.scale(0.5)
          return vg

        self.play(ApplyFunction(f_anim_1,group_etats_actions))
 
        self.wait()



#class Sc9(Scene): #PARTIE EXEMPLE EN AJOUTANT LES RECOMPENSES

#    def construct(self):


#class Sc10(Scene): #AU MORPION, ON N'A DE RECOMPENSE QUA LA FIN DE LA PARTIE. CERTAINES ACTIONS NE DONNENT PAS DE RECOMPENSES DIRECTEMENT MEME SI ELLES SONT BONNES SUR LE LONG TERME


#    def construct(self):