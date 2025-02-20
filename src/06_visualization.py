#%%
#Importing required libraries
import geopandas as gpd
from pathlib import Path
import matplotlib.pyplot as plt

#Setting up paths for easier access
directory_path = Path("..\..")

processed_data = (
    directory_path
    / "data"
    / "processed"
)

df_path = (
    processed_data
    / "processed_combined_data"
    / "data.geojson"
)

print(df_path)
df = gpd.read_file(df_path)

# %%
##Plotting engergy investmet per capita, percentile scheme with k=5 worked great in this case
fig, ax = plt.subplots(figsize=(12,6))
df.plot(column=df["energy_inv_per_cap"], legend=True, ax=ax, scheme="percentiles", k=5)
ax.set_axis_off()
ax.set_title("Energy investment per capita($)")
ax.title.set_size(20)
fig.savefig('../../visualisations/plot_eninv_percap.png')
# %%
##Plotting investment per area, a bit of trouble with the visualisation here. Struggling with winding a scheme that fits well do to de large gap
fig2, ax2 = plt.subplots(figsize=(12,6))
##Quantiles does the trick somewhat, but doesnt justify the incredible large bin at the top
df.plot(column=df["energy_inv_per_area"], scheme="quantiles", k=7, legend=True, ax=ax2)
ax2.set_axis_off()
ax2.set_title("Energy investment per square mile ($/sqmi)")
ax2.title.set_size(20)
fig2.savefig('../../visualisations/plot_eninv_area.png')
# %%
##Plotting the percentage of republican senate seats, using cmap seismic to emphasize the two parties
fig3, ax3 = plt.subplots(figsize=(12,6))
df.plot(column=df["percent_rep"], scheme="equal_interval", k=4, ax=ax3, cmap="seismic", legend=True)
ax3.set_axis_off()
ax3.set_title("Senate seats(% rep seats)")
ax3.title.set_size(20)
fig3.savefig('../../visualisations/plot_percent_rep.png')

# %%
