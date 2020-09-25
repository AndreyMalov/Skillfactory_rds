#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
def game_core_v4(number):       
    '''The function takes a hidden number and returns the number of attempts' '''    
    guess_range = 100                         # The range of the hidden number is initialized and set
    step_index = 2                            # An auxiliary index is initialized for calculating the iteration step
    count = 1                               
    predict = guess_range / step_index        
    step = predict                          

    while number != predict:
        count += 1
        '''The next iteration step is calculated. If, according to calculations, it is less than 1, (i.e. 0), then we assign 1'''
        step_index = (step_index*2)
        step = round(guess_range / step_index) if step >= 1 else 1

        if number > predict:      
                predict += step   
        elif number < predict: 
                predict -= step   
    return(count)                 


def score_game(game_core):
    '''The function starts the game 1000 times to see how quickly the game guesses the number'''
    count_ls = []
    np.random.seed(1)  # Commit RANDOM SEED, so your experiment is reproducible.
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")   
    return(score)

# Run
score_game(game_core_v4)


# In[ ]:





# In[ ]:




