import matplotlib.pyplot as plt
import json

filename = "data.json"

with open(filename, 'r') as file:
    data = json.load(file)

# Extracting data for plotting
years = [item['year'] for item in data]
multibacilar = [item['multibacilar'] for item in data]
paucibacilar = [item['paucibacilar'] for item in data]
ign_branco = [item['ign/branco'] for item in data]

# Convert counts to percentages
total = [m + p + b for m, p, b in zip(multibacilar, paucibacilar, ign_branco)]
multibacilar_perc = [m / t * 100 for m, t in zip(multibacilar, total)]
paucibacilar_perc = [p / t * 100 for p, t in zip(paucibacilar, total)]
ign_branco_perc = [b / t * 100 for b, t in zip(ign_branco, total)]

fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# Plotting
bars1 = ax.bar(years, multibacilar_perc, color='#4E79A7', label='Multibacilar')
bars2 = ax.bar(years, paucibacilar_perc, bottom=multibacilar_perc, color='#F28E2B', label='Paucibacilar')
bottom_for_ign_branco_perc = [i + j for i, j in zip(multibacilar_perc, paucibacilar_perc)]
bars3 = ax.bar(years, ign_branco_perc, bottom=bottom_for_ign_branco_perc, color='#E15759', label="Ignorado/\nBranco")

# Function to add labels on the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2,
                '{:.2f}%'.format(height),
                ha='center', va='center', color='black', fontsize=9)

# Adding labels
# add_labels(bars1)
# add_labels(bars3)
# add_labels(bars2)

ax.set_xlabel('Ano de diagnóstico')
ax.set_ylabel('Proporção (%)')

handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1], bbox_to_anchor=(1.05, 1))

plt.xticks(years, rotation=0)
plt.tight_layout()
plt.show()