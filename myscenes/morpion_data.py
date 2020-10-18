from manimlib.imports import *
import random
import sys  


POSITIONS = [UL,UP,UR,LEFT,(0,0,0),RIGHT,DL,DOWN,DR]

#############################################################    TABLES DE MORPIONS


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



l_morp2=[[
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

l_t_morp2 = VGroup()
for i in range(len(l_morp2)):
    l_t_morp2.add(Table.get_table(l_morp2[i]).move_to(5 * LEFT))


#############################################################    TABLE DES ETATS

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




#############################################################    TABLES D'ACTIONS

l_actions=[
[[" "," "," "," "," "," "," "," "," "]],
[[" "," "," "," "," "," "," "," "," "]],
[[" "," "," "," "," "," "," "," "," "]],
[[" "," "," "," "," "," "," "," "," "]]
 ]


l_t_actions = VGroup()
for i in range(len(l_actions)):
    l_t_actions.add(Table.get_table(l_actions[i],cell_length=0.85,cell_height = 0.75,text_color = BLACK).move_to(3.25 * RIGHT))



l_actions2=[
[["0,2","0,4","0,2","0,1","0,5","0,9","0,1","0,3","0,3"]],
[["0,2","0,4","0,2","0,1","0,5","0,9","0,1","0,3","0,3"]],
[["0,2","0,4","0,2","0,1","0,5","0,9","0,1","0,3","0,3"]],
[["0,2","0,4","0,2","0,1","0,5","0,9","0,4","0,3","0,3"]],
]

l_t_actions2 = VGroup()
for i in range(len(l_actions2)):
    l_t_actions2.add(Table.get_table(l_actions2[i],cell_length=0.85,cell_height = 0.75 , text_color = BLUE).move_to(3.25 * RIGHT))


#############################################################    LETTRES INDIQUANT LES POSITIONS

group_letters = VGroup()

for i in range(3):
    for j in range(3):

        nb = Text(chr(64+(j+1)+3*i), color = BLUE, size = 0.5).move_to(j*RIGHT+i*DOWN)
        group_letters.add(nb)

group_letters_2 = group_letters.copy()



#############################################################    ELEMENTS SUPPLEMENTAIRES

rect = Rectangle(height=1, width= 2, color = DARK_BLUE,stroke_width = 10 ).move_to(2 * LEFT) #RECTANGLE DE SURBRILLANCE

rewards = [
            [1,5,7],
            [1,5,7],
            [1,5,7],
            [1,5,7]
            ]



l_pos = [ 2,1,6,8 ]

REWARDS_TO_DISPLAY = "BOTH"   #"NONE", "CURRENT" or "BOTH"
