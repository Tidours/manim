from manimlib.imports import *
import random
import sys  
import json

class Sc1(Scene): #TITRE
    def construct(self):
        text1 = TextMobject(
            "Comment les programmes apprennent-ils ?",
            tex_to_color_map={"text": YELLOW}
        )
        text2 = TextMobject(
            "L'apprentissage par renforcement", color = BLUE
            
        )
        
        text2.scale(0.75)
        group = VGroup(text1, text2)
        group.arrange_submobjects(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(3)
        self.play(Uncreate(text1))
        self.play(Uncreate(text2))

class Sc2(Scene): # EXEMPLE TABLE ETATS ACTIONS
    def construct(self):
        
        scale_fact = 0.75

        t_titre = Table.get_table([["Etats", "Actions"]],cell_length=5,text_color=WHITE,line_color=WHITE,background_color = BLACK)
        t_etats_actions = Table.get_table(
          [["Pacman en mode attaque", "S'éloigner de Pacman"],
          ["Pacman pas en mode attaque", "S'approcher de Pacman"]],cell_length=7.5,cell_height=2,text_color=GREY,line_color=WHITE,background_color = BLACK)

        rect = Rectangle(height=2 , width= 15  , color = DARK_BLUE,stroke_width = 10 ).move_to(0.5 * UP) #RECTANGLE DE SURBRILLANCE

        
        t_titre.scale(scale_fact).move_to(2 * UP)
        t_etats_actions.scale(2/3 * scale_fact).move_to((0,0,0))
        rect.scale(2/3 * scale_fact)


        txt1 = TexMobject("Etats").move_to(UP)
        txt2 = TexMobject("Etats", "\Longrightarrow", "Actions").move_to(txt1)
        self.play(Write(txt1))
        self.play(Transform(txt1,txt2))


        self.play(FadeInFrom(t_titre, DOWN),FadeOutAndShift(txt1,UP))
        #self.play(ApplyMethod(t_titre.move_to, 3*UP ))
        
        self.play(FadeIn(t_etats_actions))
       
        
        self.play(Write(rect),
          ApplyMethod(t_etats_actions[1][0].set_color,WHITE),
          ApplyMethod(t_etats_actions[1][1].set_color,WHITE))
        self.wait(2)
        self.play(ApplyMethod(rect.shift, 4/3 * scale_fact * DOWN ),
          ApplyMethod(t_etats_actions[1][0].set_color,GREY),
          ApplyMethod(t_etats_actions[1][1].set_color,GREY),
          ApplyMethod(t_etats_actions[1][2].set_color,WHITE),
          ApplyMethod(t_etats_actions[1][3].set_color,WHITE))
        self.wait(2)


class Sc3(Scene): ## EXEMPLE TABLE ETATS ACTIONS MORPION
    def construct(self):

        scale_fact = 0.6

        morp = [  #DEFINITION DES TABLES
              ["O"," ", "O" ],
              ["X","X", " " ],
              ["X"," ", "O" ],
              ]

        t_morp1=Table.get_table(morp,text_color=BLACK,line_color=BLACK,background_color = WHITE)

        #t_morp2=t_morp1.copy()

        etats_actions = [
              ["Deux 'O' sur la ligne (1)","'O' sur la ligne (1)"],
              ["Deux 'O' sur la ligne (2)","'O' sur la ligne (2)"],
              ["Deux 'O' sur la ligne (3)","'O' sur la ligne (3)"],
              ["Deux 'O' sur la colonne (1)","'O' sur la colonne (1)"],
              ["Deux 'O' sur la colonne (2)","'O' sur la colonne (2)"],
              ["Deux 'O' sur la colonne (3)","'O' sur la colonne (3)"],
              ["Deux 'O' sur la diag (1)","'O' sur la diag (1)"],

        ]
        

        for i in range(10):
        	etats_actions.append(["...", "..."])

        etats_actions.append(["Deux 'X' sur la ligne (1)","'O' sur la ligne (1)"])

        for i in range(10):
        	etats_actions.append(["...", "..."])
        	
        etats_actions.append(["Deux 'X' sur la colonne (2)","'O' sur la colonne (2)"])

        for i in range(10):
        	etats_actions.append(["...", "..."])

        t_etats_actions=Table.get_table(etats_actions,
              cell_length=7,
              text_color=WHITE,
              line_color=WHITE,
              background_color = BLACK)

        t_head=Table.get_table([
              ["Etat","Action"],
              ],
              cell_length=7,
              text_color=BLACK,
              line_color=WHITE,
              background_color = DARK_BLUE)


        t_etats_actions.scale(scale_fact)
        t_head.scale(scale_fact)

        t_morp1.move_to((0,0,0))



        self.play(Write(t_morp1))  #CREATION + SHIFT MORPION 

        def f_anim_1(vg):
          vg.shift(5 * LEFT)
          vg.scale(0.8)
          return vg

        self.play(ApplyFunction(f_anim_1,t_morp1))

    
        t_etats_actions.move_to( 19 * scale_fact * DOWN + 2 * RIGHT )
        t_head.next_to(t_etats_actions,UP)

        self.play(FadeInFrom(t_head, UP),FadeInFrom(t_etats_actions, UP))

        rect = Rectangle(height=1, width= 14, color = DARK_BLUE,stroke_width = 10 ) #RECTANGLE DE SURBRILLANCE
        rect.scale(scale_fact)
        self.play(Write(rect.move_to(2 * RIGHT)))
        self.wait(2)

        self.play(ApplyMethod(t_etats_actions.shift, 17 * scale_fact * UP )) #DEFILEMENT DES TABLES
        self.wait(2)
        self.play(ApplyMethod(t_etats_actions.shift, 11 * scale_fact * UP ))
        self.wait(2)
        self.play(ApplyMethod(t_etats_actions.shift, 11 * scale_fact * UP ))
        self.wait(2)

def get_board_chars(rank): #read the board and returns the rank in the qtable
  board = 9 * [' ']
  for r in range(0,9):
    if rank%pow(3,r) == 1 : board[r] = 'O'  
    if rank%pow(3,r) == 2 : board[r] = 'X' 
  return board

with open("D:\Tidiane\Personnel\Developpement\Projet Morpion\QLearning/board_list.json", 'r') as f:
    board_list = json.load(f) #taille : 20.000


class Sc4(Scene): #DEFILEMENT DE TOUS LES ETATS DIFFERENTS
    def construct(self):


        num_ep = Integer(0,edge_to_fix = (0,0,0))
        tracker_ep = ValueTracker(0)
        num_ep.add_updater(lambda d: d.set_value(tracker_ep.get_value()))
        self.add(num_ep.move_to([0,-1,0]))

        for i in range(200): #range(5478):
              
              morp = board_list[random.randrange(20000)] #generate random boards



              t_morp = Table.get_table(morp,text_color=BLACK,line_color=BLACK,background_color = WHITE)
              self.add(t_morp.move_to([0,1,0]))
              
              tracker_ep.set_value(float( i + 1 ))


              self.wait(max(2/(i+1),0.04))

        for i in range(100): #range(5478):
              morp = board_list[random.randrange(20000)] #generate random boards
              t_morp = Table.get_table(morp,text_color=BLACK,line_color=BLACK,background_color = WHITE)
              self.add(t_morp.move_to([0,1,0]))
              
              tracker_ep.set_value(float( i * 51+ 378 ))
              self.wait(0.05)



states1=[]

for i in range(9):
    states1.append([str(i+1)])
states1.append(["..."])
for i in range(5474,5478):
    states1.append([str(i+1)])

class Sc5(Scene): #VUE D ENSEMBLE DE LA LISTE D ETATS

    def construct(self):
        
        num = Integer(5478,edge_to_fix = (0,0,0))
        



        t_states1=Table.get_table(states1,cell_length=2,text_color=WHITE,line_color=WHITE,background_color = BLACK)
        t_states1.move_to(LEFT)
        t_states1.scale(0.5)
        self.add(num.move_to([0,-1,0]))
        self.wait()
        self.play(ApplyMethod(num.move_to,[2,0,0]))
        self.play(Write(t_states1))
        self.wait()


        def f_anim_1(vg):
          vg.shift(RIGHT + 7 * DOWN)
          vg.scale(2)
          return vg

        self.play(ApplyFunction(f_anim_1,t_states1),Uncreate(num))
        #self.play()
        self.wait()