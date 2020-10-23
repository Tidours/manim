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



class Sc7_9_11(Scene): #PARTIE EXEMPLE EN AJOUTANT LES RECOMPENSES
  
    def construct(self):


        l_t_actions = l_t_actions2.copy()

        #TABLE ETATS , RECTANGLE DE SURBRILLANCE
        self.add(t_etats.move_to(2 * LEFT),rect,l_t_morp[0])
        self.play(Write(group_letters_2.move_to(5 * LEFT + 0.3 * UL )))

        for i in range(9):
            self.play(ApplyMethod(group_letters_2[i].move_to, i * 0.85 * RIGHT + 0.9 * UP),run_time=0.1)
        self.wait()


                    #EVALUER LES ACTIONS POSSIBLES

        joueur = TextMobject("O",color = DARK_BLUE).move_to( 5 * LEFT + 2 * DOWN)
        self.play(Write(joueur))     

        for i in range(1,3):

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
            self.play(ApplyMethod(l_t_actions[i][1][pos - 1].set_width,0.8))
            self.play(ApplyMethod(l_t_actions[i][1][pos - 1].set_color,BLUE))
            self.play(ApplyMethod(l_t_actions[i][1][pos - 1].set_width,0.6))
 
            self.play(ApplyMethod(joueur.move_to, 5 * LEFT + POSITIONS[pos] ))  

            if i == 2 : #affichage de l'état précédent en haut à droite
                precedent_group = VGroup(l_t_actions[i].copy(),Table.get_table([["1"]]).move_to(2 * LEFT),TextMobject("Etat précédent",text_color = RED).move_to(DR))
                self.play(FadeInFrom(precedent_group.scale(0.7).move_to(3 * UR ),LEFT))
                reward_bottom = TextMobject("+1").move_to(4 * LEFT + 3 * DOWN)
                reward = TextMobject("1").move_to(4 * LEFT + 3 * DOWN)
                self.play(Write(reward_bottom))

                if REWARDS_TO_DISPLAY == "CURRENT" :
                    self.play( FadeOut( precedent_group[0][1][l_pos[i - 1] - 1]),ApplyMethod(reward.move_to,precedent_group[0][1][l_pos[i - 1] - 1]))
                    self.play(FadeOut(precedent_group))

                if REWARDS_TO_DISPLAY == "BOTH" :
                    equation_reward = TexMobject("R", "+", "R suivante").move_to(2 * UR)
                    equation_result = TexMobject("1,4").move_to(equation_reward)
                    self.play(Write(equation_reward))
                    reward_suivante = l_t_actions[i][1][pos - 1].copy()



                    self.play(ApplyMethod(reward.move_to,equation_reward[0]), FadeOut( equation_reward[0]))
                    
                    self.play(ApplyMethod(reward_suivante.move_to,equation_reward[2]),FadeOut(equation_reward[2]))
                    

                    self.play(Transform(VGroup(equation_reward[1],reward,reward_suivante),equation_result))
                    self.play( FadeOut( precedent_group[0][1][l_pos[i - 1] - 1]),ApplyMethod(equation_result.move_to,precedent_group[0][1][l_pos[i - 1] - 1]))




                #self.play()
                #self.play(ApplyFunction(f_anim_UR_shrink,precedent_group))
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
        group_actions = VGroup()
        for i in range(14):
            if i != 9 : group_actions.add(Table.get_table([["1","1","1","1","1","1","1","1","1"]]).move_to(( i + 0.5) * DOWN + 3 * RIGHT).scale(0.75))

        group_etats_actions.add(t_etats_1,group_actions)
        

        self.add(t_etats_1)

        self.play(Write(group_actions))
        self.wait()


        def f_anim_1(vg):
          vg.move_to(2 * LEFT )
          vg.scale(0.5)
          return vg

        self.play(ApplyFunction(f_anim_1,group_etats_actions))
 
        self.wait()






class Sc10(Scene): #AU MORPION, ON N'A DE RECOMPENSE QUA LA FIN DE LA PARTIE. CERTAINES ACTIONS NE DONNENT PAS DE RECOMPENSES DIRECTEMENT MEME SI ELLES SONT BONNES SUR LE LONG TERME


    def construct(self):

      self.add(l_t_morp[0].move_to((0,0,0)))
      eq = TexMobject("R").move_to(2 * DOWN)
      eq2 = TexMobject("R", "+", "R^{+1}").move_to(eq)
      self.play(Write(eq))
      self.play(Transform(eq,eq2))


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