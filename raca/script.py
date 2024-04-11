import matplotlib.pyplot as plt
import json

filename = "data.json"

with open(filename, 'r') as file:
    data = json.load(file)

# Define labels for each category in the new dataset
labels = {
    'branca': 'Branca',
    'preta': 'Preta',
    'amarela': 'Amarela',
    'parda': 'Parda',
    'indigena': 'Indígena',
    'ign_branco': "Ignorado/\nBranco"
}

# Extracting data for plotting
years = [item['ano_diagnostico'] for item in data]
categories = list(labels.keys())
category_data = {category: [item[category] for item in data] for category in categories}

# Calculate total for each year to get the percentages later
totals = [sum(item[category] for category in categories) for item in data]


# for year, total in zip(years, totals):
#     print(f"Year: {year}")
#     print(f"Total: {total}")
#     for category in categories:
#         percentage = (category_data[category][years.index(year)] / total) * 100.0 if total > 0 else 0
#         print(f"{category}: {category_data[category][years.index(year)]}" + f" ({percentage:.2f}%)")
#     print("\n")




# Calculate percentages
percentages = {category: [(value / total) * 100.0 if total > 0 else 0 for value, total in zip(values, totals)] for category, values in category_data.items()}

# Calculate total for each category and sort categories by total
category_totals = {category: sum(values) for category, values in category_data.items()}
sorted_categories = sorted(category_totals, key=category_totals.get, reverse=True)

# Function to add labels on the bars
def add_labels(bars, heightOffset=0):
    for index, bar in enumerate(bars):
        height = bar.get_height() + heightOffset
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2,
                '{:.2f}%'.format(height),
                ha='center', va='center', color='black', fontsize=9)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
colors = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#AF7AA1']
bottom = [0] * len(years)

for category, color in zip(sorted_categories, colors):
    bars = ax.bar(years, percentages[category], bottom=bottom, color=color, label=labels[category])

    add_labels(bars, 0)
    bottom = [i + j for i, j in zip(bottom, percentages[category])]

ax.set_xlabel('Ano de diagnóstico')
ax.set_ylabel('Proporção (%)')
plt.xticks(years, rotation=0)
handles, labels = ax.get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1], bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()