#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
step_list=[]

def game_core_v3(number):
    '''The function takes a hidden number and returns the number of attempts' '''    
    step_index = 1         # An auxiliary index is initialized for calculating the iteration step 
    guess_range=100
    step = guess_range     # The iteration step is initialized and set
    '''Creation of list with iteration steps'''
    while step >= 0.5:
        step = guess_range / step_index
        step_index=step_index*2
        step_list.append(round(step))
    
    count = 1
    predict = step_list[1]
    while number != predict:
        count += 1
        if number > predict: 
                predict += step_list[count]
        elif number < predict: 
                predict -= step_list[count]
    return(count) 


def score_game(game_core):
    '''The function starts the game 1000 times to see how quickly the game guesses the number'''
    count_ls = []
    np.random.seed(1)  # Commit RANDOM SEED, so your experiment is reproducible.
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# Run
score_game(game_core_v3)


# In[ ]:




