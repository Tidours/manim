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
    [" "," ", " " ],
    [" "," ", " " ],
    [" "," ", " " ],
     ]

morp2=[
    ["O"," ", "O" ],
    ["X","X", " " ],
    ["X"," ", "O" ],
     ]

actions_h=[[]]
for i in range(9):
    actions_h[0].append(str(i+1))

actions=[[]]
for i in range(9):
    actions[0].append(str(0.5))




class Sc6(Scene): #DEFILEMENT DE LA LISTE D ETATS

    def construct(self):

        t_etats=Table.get_table(etats,cell_length=2,text_color=WHITE,line_color=WHITE,background_color = BLACK)

        group_numbers = VGroup()

        for i in range(3):
            for j in range(3):

                nb = Text(str((j+1)+3*i), color = BLUE, size = 0.5).move_to(j*RIGHT+i*DOWN)
                group_numbers.add(nb)


        t_actions_h = Table.get_table(actions_h,cell_length=1.5,text_color=BLUE,line_color=BLACK,background_color = BLACK)
        t_actions_h.scale(0.5)

        t_actions = Table.get_table(actions,cell_length=1.5,text_color=WHITE,line_color=WHITE,background_color = BLACK)
        t_actions.scale(0.5)

        rect = Rectangle(height=1, width= 2, color = DARK_BLUE,stroke_width = 10 ) #RECTANGLE DE SURBRILLANCE

        t_morp1=Table.get_table(morp1,text_color=BLACK,line_color=BLACK,background_color = WHITE) #TABLE MORPION

        self.add(t_etats.move_to(15 * DOWN))
        self.wait()

        
        self.play(Write(t_morp1.move_to(5 * LEFT)),ApplyMethod(t_etats.shift,2 * LEFT))

        
        self.play(Write(rect.move_to(2 * LEFT)))
        self.wait(2)




        self.play(Write(group_numbers.move_to(5 * LEFT + 0.2 * UL )))

        #



        
        #self.play(Write())
        #t_actions_h.move_to(3 * RIGHT + 0.5 * UP )

        #self.play(Transform(group_numbers,t_actions_h))

        for i in range(9):
        	self.play(ApplyMethod(group_numbers[i].move_to, i * 0.75 * RIGHT + 0.5 * UP),run_time=0.2)

        self.play(Write(t_actions.move_to(3 * RIGHT)))

        self.wait()

        self.play(ApplyMethod(t_etats.shift, 14 * UP))

        self.wait()



class Sc7(Scene): #DEFILEMENT DE LA LISTE D ETATS

    def construct(self):

        group_numbers = VGroup()

        for i in range(3):
            for j in range(3):

                nb = Text(str((i+1)+3*j), color = BLUE, size = 0.4).move_to(i*RIGHT+j*DOWN)
                group_numbers.add(nb)

        self.play(Write(group_numbers.move_to((0,0,0))))

        self.play(ApplyMethod(group_numbers[0].shift,LEFT))

