# 2) Create dictionary to store player name and runs scored of at least 5 players. 
#    Display it. Now convert this dictionary ‌into Series object and print it.

import pandas as pd
dict={}
for i in range(5):
    player_name=input("Enter player name:")
    runs_scored=int(input("Enter sccored runs:"))
    dict[player_name]=runs_scored
dict1=pd.Series(dict)
print(dict1)