from manimlib.imports import *
import sys  

sys.path.append("D:\Tidiane\Personnel\Developpement\Projet Morpion\QLearning")  
from QLearning_plots import board_list #scriptName without .py extension  






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
