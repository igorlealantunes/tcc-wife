import matplotlib.pyplot as plt
import json

filename = "data.json"

with open(filename, 'r') as file:
    data = json.load(file)

# Define labels for each category
labels = {
    'menor_de_15_anos': 'Menor de 15 anos',
    '15_a_29_anos': '15 a 29 anos',
    '30_a_59_anos': '30 a 59 anos',
    '60_anos_ou_mais': '60 anos ou mais',
}

# Extracting data for plotting
years = [item['ano'] for item in data]
categories = list(labels.keys())
categories = categories[::-1]  # Reverse to match the bar order (largest at the bottom)
category_data = {category: [item[category] for item in data] for category in categories}

# Calculate total for each year
totals = [sum(item[category] for category in categories) for item in data]

# Calculate percentages
percentages = {category: [(value / total) * 100 for value, total in zip(values, totals)] for category, values in category_data.items()}

# Plotting
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
colors = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#AF7AA1']
bottom = [0] * len(years)

for i, category in enumerate(categories):
    bars = ax.bar(years, percentages[category], bottom=bottom, color=colors[i % len(colors)], label=labels[category])
    bottom = [i + j for i, j in zip(bottom, percentages[category])]

# Adding labels on the bars
def add_labels(ax):
    for bar in ax.patches:
        height = bar.get_height()
        if height > 0:  # Only add labels to bars with positive height
            ax.annotate(f'{height:.2f}%',
                        (bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                        ha='center', va='center',
                        color='black', fontsize=9)

# add_labels(ax)

ax.set_xlabel('Ano de diagnóstico')
ax.set_ylabel('Proporção (%)')
ax.set_xticks(years)

# Retrieving and reversing the legend handles and labels
handles, labels = ax.get_legend_handles_labels()
# Reverse to match the bar order (largest at the bottom)
handles, labels = handles[::-1], labels[::-1]
plt.legend(handles, labels, bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
