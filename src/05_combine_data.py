# %%
#Importing required libraries
import pandas as pd
import geopandas as gpd
from pathlib import Path
# %%
## Setting up paths for easier access
directory_path = Path("..\..")

datasets_path = (
    directory_path
    / "data"
    / "interim"
)
energy_investment_path = (
    datasets_path
    / "interim_energy_inv"
    / "energy_investment.csv"
)
est_pop_path = (
    datasets_path
    / "interim_est_pop"
    / "est_pop.csv"
)
state_pship_path = (
    datasets_path
    / "interim_state_pship"
    / "state_pship.csv"
)
us_map_path = (
    datasets_path
    / "interim_us_map"
    / "us_map.geojson"
)
state_pship_df = pd.read_csv(state_pship_path)
est_pop_df = pd.read_csv(est_pop_path)
energy_investment_df = pd.read_csv(energy_investment_path)
us_map_df = gpd.read_file(us_map_path)
#%%
##Combining all columns to one dataframe
us_map_df["energy_inv_tot"] = energy_investment_df["total"]
us_map_df["energy_inv_per_cap"] = energy_investment_df["total"]/est_pop_df["2021"]
us_map_df["percent_rep"] = state_pship_df["Senate\nRep."]/state_pship_df["Total\nSenate"]
us_map_df["est_pop21"] = est_pop_df["2021"]
us_map_df["energy_inv_per_area"] = energy_investment_df["total"]/us_map_df["area"]
us_map_df.to_file(r"..\..\data\processed\processed_combined_data\data.geojson", driver="GeoJSON")

# %%
