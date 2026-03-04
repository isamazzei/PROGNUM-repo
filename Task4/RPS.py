#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

#asks user to choose
print("input P for paper, R for rocks, and S for scissors")
user = input("Your choice: ").upper()

#the computer chooses
options = ["R", "P", "S"]
computer = np.random.choice(options)
print("Computer choice:", computer)

#judges who wins
if user == computer:
    print("It's a tie")
elif (user == "R" and computer == "S"): 
    print("You win")
elif (user == "P" and computer == "R"):
    print("You win")   
elif(user == "S" and computer == "P"):
    print("You win")
elif user in options:
    print("You lose")
else:
    print("Invalid input! Please choose R, P or S.")
    


# In[ ]:





# In[ ]:




