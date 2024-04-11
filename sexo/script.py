import matplotlib.pyplot as plt
import json

filename = "data.json"

with open(filename, 'r') as file:
    data = json.load(file)

# Update labels for the new categories
labels = {
    'feminino': 'Feminino',
    'masculino': 'Masculino',
    'ignorado_branco': "Ignorado/\nBranco"
}

# Extracting data for plotting
years = [item['ano_diagnostico'] for item in data]
categories = list(labels.keys())
category_data = {category: [item.get(category, 0) for item in data] for category in categories}

# Calculate total for each year
totals = [item['total'] for item in data]

percentages = {category: [(value / total) * 100 for value, total in zip(values, totals)] for
               category, values in category_data.items()}

# Function to add labels on the bars
def add_labels(ax, bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}%',
                    (bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                    ha='center', va='center',
                    color='black', fontsize=9)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
colors = ['#4E79A7', '#F28E2B', '#E15759']  # Colors for the categories
bottom = [0] * len(years)

for i, category in enumerate(categories):
    bars = ax.bar(years, percentages[category], bottom=bottom, color=colors[i % len(colors)], label=labels[category])
    # add_labels(ax, bars)
    bottom = [i + j for i, j in zip(bottom, percentages[category])]

ax.set_xlabel('Ano de diagnóstico')
ax.set_ylabel('Proporção (%)')
plt.xticks(years, rotation=0)

# Retrieving and reversing the legend handles and labels
handles, labels = ax.get_legend_handles_labels()
# Reverse to match the bar order (largest at the bottom)
handles, labels = handles[::-1], labels[::-1]
plt.legend(handles, labels, bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
