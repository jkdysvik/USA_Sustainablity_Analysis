# -*- coding: utf-8 -*-
# Author: jonathkd@stud.ntnu.no
# Date: 8/11/22
# %%
#This section always gets errors, i have studied and this is due to the fact that the env.yml from blackboard is for python 3.8, but the program works regardless
import pandas as pd

# %%
##Extracting manually input data from auxiliary
state_partisan_xl = (r"..\..\data\auxiliary\auxiliary_state_pship\State-Partisan-Composition-Table-June-2022.xlsx")
## Simply reading it to csv
state_partisan_df = pd.read_excel(state_partisan_xl, sheet_name=1)
state_partisan_df.to_csv(r"..\..\data\interim\interim_state_pship\state_pship.csv")

# %%
