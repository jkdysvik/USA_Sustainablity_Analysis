# -*- coding: utf-8 -*-
# Author: jonathkd@stud.ntnu.no
# Date: 8/11/22
# %%
#Import required libraries
#This section always gets errors, i have studied and this is due to fact that the env.yml from blackboard is for python 3.8, but the program works regardless
import geopandas as gpd

#Defining som variables for filtering later, especially inmportant in this dataframe due to excessive amounts of data and columns
column_filter = ["STATE_NAME", "STATE_ABBR", "SHAPE_Length", "SQMI", "geometry"]
column_names = ["state", "abbr", "length", "area", "geometry"]
us_states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
# %%
us_map_gj = (r"..\..\data\raw\dataset_provider_4\USA_states_(Generalized).geojson")
us_map_df = gpd.read_file(us_map_gj)
## Removing redudant columns and cleaning up data
us_map_df = us_map_df[us_map_df["STATE_NAME"].isin(us_states)]
us_map_df = us_map_df.sort_values(by=["STATE_NAME"])
us_map_df.reset_index(drop=True, inplace=True)
##Filter out the columns we dont need later
us_map_df = us_map_df.filter(column_filter)
us_map_df.columns = column_names
us_map_df.to_file(r"..\..\data\interim\interim_us_map\us_map.geojson", driver="GeoJSON")
