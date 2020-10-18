from manimlib.imports import *
import random
import sys  
import json

from myscenes.morpion_data import *


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
            FadeInFrom(l_t_actions[i],DOWN)
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

            self.play(FadeInFrom(l_t_actions[i],DOWN))
            self.wait()

            joueur = joueur.copy()
            self.play(Write(joueur.move_to( 5 * LEFT + 2 * DOWN)))      

            pos = l_pos[i]

            self.play(ApplyMethod(l_t_actions[i][1][pos - 1].set_color,GREEN))
            self.play(ApplyMethod(l_t_actions[i][1][pos - 1].set_width,0.3))
            self.play(ApplyMethod(l_t_actions[i][1][pos - 1].set_width,0.15))
            self.play(ApplyMethod(l_t_actions[i][1][pos - 1].set_width,0.3))      

            self.play(ApplyMethod(joueur.move_to, 5 * LEFT + POSITIONS[pos] ))      





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