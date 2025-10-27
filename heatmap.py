import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Smart_Farming_Crop_Yield_2024.csv")
df_heatmap = df.select_dtypes(include="number")

plt.figure(figsize=(10,10))
sns.heatmap(
    df_heatmap.corr(),
    center=0,
    vmin=-1,
    vmax=1,
    cmap="vlag")

plt.xticks(rotation=45, ha="right", fontsize=8)
plt.yticks(rotation=0, fontsize=8)
plt.title("Mapa de calor de correlaciones de sensores para agricultura", fontsize=14, weight="bold", pad=12)
plt.show()
