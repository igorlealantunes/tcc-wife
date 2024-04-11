import matplotlib.pyplot as plt
import json

filename = "data.json"

with open(filename, 'r') as file:
    data = json.load(file)

# Define labels for each category
labels = {
    'analfabeto': 'Analfabeto',
    'fundamental_completo_e_incompleto': "Fundamental Completo\ne Incompleto",
    'medio_completo_e_incompleto': 'Médio Completo\ne Incompleto',
    'superior_completo_e_incompleto': 'Superior Completo\ne Incompleto',
    'ign_branco': 'Ignorado/Branco',
    'nao_se_aplica': 'Não se aplica'
}

# Extracting data for plotting
years = [item['ano_diagnostico'] for item in data]
categories = list(labels.keys())
category_data = {category: [item[category] for item in data] for category in categories}

# Calculate total for each year
totals = [sum(item[category] for category in categories) for item in data]

# Calculate percentages
percentages = {category: [(value / total) * 100 for value, total in zip(values, totals)] for category, values in category_data.items()}

# Calculate total for each category and sort categories by total
category_totals = {category: sum(values) for category, values in category_data.items()}
sorted_categories = sorted(category_totals, key=category_totals.get, reverse=True)

# Function to add labels on the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2,
                '{:.2f}%'.format(height),
                ha='center', va='center', color='black', fontsize=9)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
colors = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#AF7AA1']
bottom = [0] * len(years)

for category, color in zip(sorted_categories, colors):
    bars = ax.bar(years, percentages[category], bottom=bottom, color=color, label=labels[category])
    # add_labels(bars)
    bottom = [i + j for i, j in zip(bottom, percentages[category])]

ax.set_xlabel('Ano de diagnóstico')
ax.set_ylabel('Proporção (%)')
plt.xticks(years)
handles, labels = ax.get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1], bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()