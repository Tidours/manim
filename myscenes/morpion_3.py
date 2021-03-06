from manimlib.imports import *
import sys  
import json

#sys.path.append("D:\Tidiane\Personnel\Developpement\Projet Morpion\QLearning")  
#from QLearning_plots import board_list #scriptName without .py extension  


with open("D:\Tidiane\Personnel\Developpement\Projet Morpion\QLearning/board_list.json", 'r') as f:
    board_list = json.load(f)
with open("D:\Tidiane\Personnel\Developpement\Projet Morpion\QLearning/rewards.json", 'r') as f:
    rewards = json.load(f)

def get_board_chars(rank): #read the board and returns the rank in the qtable
  board = 9 * [' ']
  for r in range(0,9):
    if rank%pow(3,r) == 1 : board[r] = 'O'  
    if rank%pow(3,r) == 2 : board[r] = 'X' 
  return board



class Sc12(Scene):
    def construct(self):



        num_ep = Integer(0,edge_to_fix = (0,0,0))
        tracker_ep = ValueTracker(0)
        num_ep.add_updater(lambda d: d.set_value(tracker_ep.get_value()))
        self.add(num_ep.move_to([0,-1,0]))




        for i in range(200): #range(5478):
              
              morp = board_list[i] #generate random boards

              board = get_board_chars(i)

              morp = [  #DEFINITION DES TABLES
              [board[1],board[2],board[3]],
              [board[4],board[5],board[6]],
              [board[7],board[8],board[9]]
              ]

              t_morp = Table.get_table(morp,text_color=BLACK,line_color=BLACK,background_color = WHITE)
              self.add(t_morp.move_to([0,1,0]))
              
              tracker_ep.set_value(float( i + 1 ))


              self.wait(max(2/(i+1),0.04))

        for i in range(100): #range(5478):
              morp = board_list[i] #generate random boards
              t_morp = Table.get_table(morp,text_color=BLACK,line_color=BLACK,background_color = WHITE)
              self.add(t_morp.move_to([0,1,0]))
              
              tracker_ep.set_value(float( i * 51+ 378 ))
              self.wait(0.05)


class Sc13(Scene):
    def construct(self):



        num_ep = Integer(0,edge_to_fix = (0,0,0))
        tracker_ep = ValueTracker(0)
        num_ep.add_updater(lambda d: d.set_value(tracker_ep.get_value()))
        self.add(num_ep.move_to(3 * DOWN))
        self.add(TextMobject("Coups joués :").next_to(num_ep,LEFT))

        num_win = Integer(0,edge_to_fix = (0,0,0))
        tracker_win = ValueTracker(0)
        num_win.add_updater(lambda d: d.set_value(tracker_win.get_value()))
        self.add(num_win.move_to(2 * DOWN))
        self.add(TextMobject("O :",color = BLUE).next_to(num_win,LEFT))

        num_lose = Integer(0,edge_to_fix = (0,0,0))
        tracker_lose = ValueTracker(0)
        num_lose.add_updater(lambda d: d.set_value(tracker_lose.get_value()))
        self.add(num_lose.move_to(2 * UP))
        self.add(TextMobject("X :", color = ORANGE).next_to(num_lose,LEFT))


        for i in range(5): #range(5478):
              
              morp = board_list[i+5]
              t_morp = Table.get_table(morp,text_color=BLACK,line_color=BLACK,background_color = WHITE)
              self.add(t_morp.move_to([0,0,0]))
              
              tracker_ep.set_value(float( i + 1 ))
              tracker_win.set_value(float( rewards['win'] [i]))
              tracker_lose.set_value(float( rewards['lose'] [i]))

              self.wait(max(3/(i+1),0.04))




class Sc14(GraphFromData): #graph depuis des données csv
    CONFIG = {
        "x_min" : 0,
        "x_max" : 10000,
        "x_axis_label": "Coups joués",

        "y_min" : 0,
        "y_max" : 1800,
        "y_axis_label": "Victoires",
        #"graph_origin" : ORIGIN ,
        #"function_color" : RED ,
        #"axes_color" : GREEN,
        "x_tick_frequency": 4000,
        "y_tick_frequency": 400,
        "x_labeled_nums" : range(0,10000,4000),
        "y_labeled_nums" : range(0,1800,400),
 
        }
    def construct(self):
        
        self.setup_axes()
        # Get coords
        
        x = rewards['ep'][0::500]
        y_win = rewards['win'][0::500]
        y_lose = rewards['lose'][0::500]

        coords_win = [[px,py] for px,py in zip(x,y_win)]
        coords_lose = [[px,py] for px,py in zip(x,y_lose)]
        #coords = get_coords_from_csv("myscenes/morpion_data/test")
        points_win = self.get_points_from_coords(coords_win)
        points_lose = self.get_points_from_coords(coords_lose)


        # Set graph
        graph_win = SmoothGraphFromSetPoints(points_win,color=ORANGE)
        graph_lose = SmoothGraphFromSetPoints(points_lose,color=BLUE)

        #area_win = self.get_area(graph_win, 0, 10000)
        #graph = DiscreteGraphFromSetPoints(points,color=ORANGE)
        # Set dots
        #dots = self.get_dots_from_coords(coords)
        #self.add(dots)
        self.play(ShowCreation(graph_win,run_time=10),ShowCreation(graph_lose,run_time=10))#,ShowCreation(area_win,run_time=4))
        self.wait(3)
