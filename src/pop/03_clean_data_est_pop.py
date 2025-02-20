# -*- coding: utf-8 -*-
# Author: jonathkd@stud.ntnu.no
# Date: 8/11/22
# %%
#Import required libraries
#This section always gets errors, i have studied and this is due to the fact thatenv.yml from blackboard is for python 3.8, but the program works regardless
import pandas as pd
#Defining som variables for filtering later

us_states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

column_names = ["state", "est", "2020", "2021"]
column_drops = ["est","2020"]
# %%
##Removing reduntant columns and cleaning up data
est_pop_xl = (r"..\..\data\raw\dataset_provider_2\NST-EST2021-POP.xlsx")
est_pop_df = pd.read_excel(est_pop_xl)
est_pop_df.columns = column_names
est_pop_df = est_pop_df[est_pop_df.state.str.startswith(".", na=False)]
##Every State has a "." as its first ltter, removing it to make things more clean and easier to work with
est_pop_df["state"] = est_pop_df["state"].map(lambda x: str(x)[1:])
est_pop_df = est_pop_df[est_pop_df["state"].isin(us_states)]
est_pop_df.reset_index(inplace=True, drop=True)
est_pop_df = est_pop_df.drop(columns=column_drops)
## Saving as csv in interim data
est_pop_df.to_csv(r"..\..\data\interim\interim_est_pop\est_pop.csv")



# %%
