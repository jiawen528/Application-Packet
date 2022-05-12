#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Craps賭博遊戲
玩家搖兩骰子 如果第一次搖出7點或11點 玩家勝
如果搖出2點 3點 12點 莊家勝 

其他情況遊戲繼續

玩家再次搖骰子 如果搖出7點 莊家勝
如果搖出第一次搖的點數 玩家勝
否則遊戲繼續 玩家繼續搖骰子
玩家進入遊戲時有1000元的賭注 
全部輸光遊戲結束

"""

from random import randint    #從隨機亂數模組(random)中匯入一個隨機整數(randint)
start = True
while start:
    money = 1000
    while money > 0:
        print('你的總資產為:',money)
        while True:
            debt = int(input('請下注:'))    #自定義下注金額
            if 0 < debt <= money:
                print('您的下注金額為:',debt)
                break
            else:
                print('您的下注金額不合理')
                
        craps1 = randint(1,6)    #定義骰子1    
        craps2 = randint(1,6)    #定義骰子2
        first_play = craps1 + craps2    #點數需為兩骰子之和
        print('玩家搖出了%d點' %first_play)
            
        if first_play ==7 or first_play == 11:
            print('玩家勝！')
            money += debt
            
        elif first_play ==2 or first_play==3 or first_play==12:
            print('莊家勝！')
            money -= debt
            
        else: keep_go_on = True
            
    while keep_go_on:
        craps1 = randint(1,6)
        craps2 = randint(1,6)
        new = craps1 + craps2  
        print('玩家搖出了%d點' % new)
            
        if new ==7:
            print('莊家勝！')
            money -= debt
            
        elif new == first_play:
            print('玩家勝！')
            money+= debt
            
        else: keep_go_on = False
        print('你破產了, 遊戲結束!')
            



