# -*- coding: utf-8 -*-
# Author: jonathkd@stud.ntnu.no
# Date: 8/11/22
# %%
#This section always gets errors, i have studied and this is due to fact that the env.yml from blackboard is for python 3.8, but the program works regardless
#Importing required libraries
import pandas as pd

#Defining som variables for filtering later
drop_columns = ["County", "Congressional District", "Energy Type", 
                "Agency", "Program_Name", "Total Number of Investments",
                "Zip Code", "Description"]
us_states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

# %%
energy_investments_xl = (r"..\..\data\raw\dateset_provider_3\EnergyInvestments_DataDownloads.xlsx")
## Removing redudant columns and cleaning up data
energy_df = pd.read_excel(energy_investments_xl, sheet_name=6)
energy_df = energy_df.drop(columns=drop_columns, axis=1)
energy_df = energy_df.rename(columns={"State":"state","Year": "year", "Total Amount of Assistance": "total"})
#Filter out Puerto Rico and other "States"
energy_df = energy_df[energy_df["state"].isin(us_states)]
## Filtering for year 2021
energy_df = energy_df[energy_df["year"] == 2021]
energy_df.reset_index(drop=True, inplace=True)
## The sheet contains a list of every single investment, here i group them together to create a dataframe with 50 columns
energy_df = energy_df.groupby(["state", 'year']).sum().reset_index().reindex(columns=energy_df.columns)
energy_df = energy_df.drop(columns="year")
##Save as interim
energy_df.to_csv(r"..\..\data\interim\interim_energy_inv\energy_investment.csv")

# %%