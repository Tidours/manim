#!/usr/bin/env python

from manimlib.imports import *



class Sc1(Scene):
    def construct(self):
        text1 = TextMobject(
            "Comment les programmes apprennent-ils ?",
            tex_to_color_map={"text": YELLOW}
        )
        text2 = TextMobject(
            "L'apprentissage par renforcement",
            
        )
        text2.set_color(BLUE)
        text2.scale(0.75)
        group = VGroup(text1, text2)
        group.arrange_submobjects(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(3)
        self.play(Uncreate(text1))
        self.play(Uncreate(text2))


class Sc2(Scene):
    def construct(self):
        titre = TexMobject(r"Etat 	\rightarrow 	action",)
        
        #matrice = TexMobject(r"\begin{bmatrix} ennemi plus fort & \rightarrow & attaque \\ ennemiplusfort & \rightarrow & attaque \\ ennemiplusfort & \rightarrow & attaque \\ ennemiplusfort & \rightarrow & attaque \end{bmatrix}",)

        mat = [
              ["Etat 1", r"\rightarrow","   ", "    Action 1"],
              ["Etat 2", r"\rightarrow","   ", "    Action 2"],
              ["EnnemiPlusFort", r"\rightarrow", "   ","Fuire"],
              ["Etat 4", r"\rightarrow", "   ","    Action 4"],
              ["EnnemiMoinFort", r"\rightarrow", "   ","Attaquer"],
              ["Etat 9", r"\rightarrow", "   ","    Action 9"],
              ["Etat 10", r"\rightarrow","   ", "    Action 10"],
              ["Etat 11", r"\rightarrow", "   ","    Action 11"],
              ["DevantUnTrou", r"\rightarrow", "   ","Sauter"],
              ]

        matrice = Matrix(mat)

        matrice.set_width(6)
        
        matrice[0].set_color(RED)

        fleche =  TexMobject(r"\Rightarrow")


        self.play(Write(titre))
        self.play(ApplyMethod(titre.move_to, 3*UP ))
        
        matrice.move_to( 3 * DOWN +LEFT )
        self.play(FadeInFrom(matrice, DOWN))
       
        fleche.move_to( 4 * LEFT)
        self.play(Write(fleche))

        self.play(ApplyMethod(matrice.shift, 0.6 * UP ))
        self.wait(2)
        self.play(ApplyMethod(matrice.shift, 0.6 * UP ))
        self.wait(2)
        self.play(ApplyMethod(matrice.shift, 0.6 * UP ))
        self.wait(2)

class Sc3(Scene):
    def construct(self):

        morp=[
              ["O"," ", "O" ],
              ["X","X", " " ],
              ["X"," ", "O" ],
              ]

        t_morp1=Table.get_table(morp,text_color=BLACK,line_color=BLACK,background_color = WHITE)
        t_morp2=t_morp1.copy()


        morp=[
              ["O","O", "O" ],
              ["X","X", " " ],
              ["X"," ", "O" ],
              ]

        t_morp3=Table.get_table(morp,text_color=BLACK,line_color=BLACK,background_color = WHITE)
        #matrice = TexMobject(r"\begin{bmatrix} O & O & X \\ O & O & X \\ O & O & X \end{bmatrix}",)

        t_morp1.set_width(4)
        t_morp2.set_width(2)
        t_morp3.set_width(2)


        t_actions=Table.get_table([
              ["Deux 'O' sur la ligne (1)","'O' sur la ligne (1)"],
              ["Deux 'O' sur la ligne (2)","'O' sur la ligne (2)"],
              ["Deux 'O' sur la ligne (3)","'O' sur la ligne (3)"],
              ["Deux 'O' sur la colonne (1)","'O' sur la colonne (1)"],
              ["Deux 'O' sur la colonne (2)","'O' sur la colonne (2)"],
              ["Deux 'O' sur la colonne (3)","'O' sur la colonne (3)"],
              ["Deux 'O' sur la diag (1)","'O' sur la diag (1)"],

              ],
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



        t_head.next_to(t_actions,UP)
        t_actions.add(t_head)

        t_actions.set_width(6)

        t_morp1.move_to((0,0,0))



        self.play(Write(t_morp1))

        def f_anim_1(vg):
          vg.shift(5 * LEFT)
          vg.scale(0.5)
          return vg

        self.play(ApplyFunction(f_anim_1,t_morp1))

    
        t_actions.move_to( UP )

        self.play(FadeInFrom(t_actions, UP))



        t_morp2.move_to( 5 * RIGHT )
        t_morp3.move_to( 5 * RIGHT )
        self.play(FadeInFrom(t_morp2, LEFT))  

        self.wait(2)

        self.play(Transform(t_morp2,t_morp3))  
   

        self.wait(2)

class Sc4(Scene):
    def construct(self):

        morp=[
              ["O"," ", "O" ],
              ["X","X", " " ],
              ["X"," ", "O" ],
              ]

        t_morp1=Table.get_table(morp,text_color=BLACK,line_color=BLACK,background_color = WHITE)

        morp=[
              ["O","O", "O" ],
              ["X","X", " " ],
              ["X"," ", "O" ],
              ]

        t_morp2=Table.get_table(morp,text_color=BLACK,line_color=BLACK,background_color = WHITE)
        #matrice = TexMobject(r"\begin{bmatrix} O & O & X \\ O & O & X \\ O & O & X \end{bmatrix}",)


        t_morps=[t_morp1,t_morp2]

        t_morp = t_morps[0]

        num = Integer(0,edge_to_fix = (0,0,0))
        tracker = ValueTracker(0)
        num.add_updater(lambda d: d.set_value(tracker.get_value()))


        self.add(num.move_to([0,-1,0]))
        self.add(t_morp.move_to([0,1,0]))

        for i in range(200): #range(5478):
              t_morp = t_morps[i%2]
              self.add(t_morp.move_to([0,1,0]))
              
              tracker.set_value(float( i + 1 ))
              self.wait(max(2/(i+1),0.04))

        for i in range(100): #range(5478):
              t_morp = t_morps[i%2]
              self.add(t_morp.move_to([0,1,0]))
              
              tracker.set_value(float( i * 51+ 378 ))
              self.wait(0.05)




states1=[]

for i in range(9):
    states1.append([str(i+1)])
states1.append(["..."])
for i in range(5474,5478):
    states1.append([str(i+1)])

states2=[]

for i in range(9):
    states2.append([str(i+1)])
states2.append(["..."])
for i in range(95,105):
    states2.append([str(i+1)])
states2.append(["..."])
for i in range(782,792):
    states2.append([str(i+1)])


morp=[
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

class Sc5(Scene):

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

class Sc6(Scene):

    def construct(self):

        t_states1=Table.get_table(states2,cell_length=2,text_color=WHITE,line_color=WHITE,background_color = BLACK)

        self.add(t_states1.move_to(15 * DOWN))
        self.wait()

        t_morp1=Table.get_table(morp,text_color=BLACK,line_color=BLACK,background_color = WHITE)
        self.play(Write(t_morp1.move_to(5 * LEFT)))

        self.play(ApplyMethod(t_states1.shift,2 * LEFT))

        t_actions_h = Table.get_table(actions_h,cell_length=1.5,text_color=BLUE,line_color=BLACK,background_color = BLACK)
        t_actions_h.scale(0.5)

        t_actions = Table.get_table(actions,cell_length=1.5,text_color=WHITE,line_color=WHITE,background_color = BLACK)
        t_actions.scale(0.5)

        
        self.play(Write(t_actions_h.move_to(3 * RIGHT + 0.5 * UP )))
        self.play(Write(t_actions.move_to(3 * RIGHT)))

        self.wait()

        self.play(ApplyMethod(t_states1.shift, 14 * UP))


        #self.play()
        self.wait()


class Ts4(Scene):

    def construct(self):
        tabledict={
            "Etats":["...","100","101","102","...","110"],

        }

        table=Table2.get_table(tabledict)
        table.scale(0.50)
        table.move_to((0,0,0))
        self.play(Write(table))
        self.wait(1)


        tabledict={
            "Action 1":[],
            "Action 2":[],
            "Action 3":[],
            "Action 4":[],
            "Action 5":[],
            "Action 6":[],
        }

        table=Table.get_table(tabledict)
        table.scale(0.50)
        table.move_to((1,0,0))
        self.play(Write(table))
        self.wait(2)

class Ts5(Scene):

    def construct(self):
        tablelist=[["1", "4", "5", "12"], 
                  ["-5"," 8", "9", "0"],
                  ["-6"," 7", "11", "19"]]

        table=Table.get_table(tablelist,text_color=BLACK,background_color = DARK_BLUE)
        table.scale(0.50)
        table.move_to((0,0,0))
        self.play(Write(table))
        self.wait(1)

class Ts6(Scene):

    def construct(self):
        tablelist=[["O", "X", "O"], 
                  ["O"," X", "X"],
                  [" ","X","X"]]

        table=Table.get_table(tablelist)
        table.scale(0.50)
        table.move_to((0,0,0))
        self.play(Write(table))
        self.wait(1)

class Ts7(Scene):

    def construct(self):
        tablelist=[["-1","25","154","1"]]

        table=Table.get_table(tablelist,text_color=BLACK,background_color = DARK_GREY)
        table.scale(0.50)
        table.move_to((0,0,0))
        self.play(Write(table))
        self.wait(1)
        


        self.wait(4)

class Ts8(GraphFromData): #graph depuis des données csv
    def construct(self):
        self.setup_axes()
        # Get coords
        coords = get_coords_from_csv("myscenes/morpion_data/test")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph = SmoothGraphFromSetPoints(points,color=ORANGE)
        #graph = DiscreteGraphFromSetPoints(points,color=ORANGE)
        # Set dots
        dots = self.get_dots_from_coords(coords)
        self.add(dots)
        self.play(ShowCreation(graph,run_time=4))
        self.wait(3)
