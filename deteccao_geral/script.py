import matplotlib.pyplot as plt
import json

filename = "data.json"

with open(filename, 'r') as file:
    data = json.load(file)

for item in data:
    total_population = sum(detail['population'] for detail in item['details'])
    total_diagnoses = sum(detail['diagnoses'] for detail in item['details'])
    item['details'].append({
        'region': 'brasil',
        'population': total_population,
        'diagnoses': total_diagnoses
    })

regions_trans = {
    'centro_oeste': 'Centro-Oeste',
    'nordeste': 'Nordeste',
    'norte': 'Norte',
    'sudeste': 'Sudeste',
    'sul': 'Sul',
    'brasil': 'Brasil'
}

years = sorted(set([item["year"] for item in data]))
regions = sorted(set([regions_trans[detail["region"]] for item in data for detail in item["details"]]))

cases_per_100k = {region: [] for region in regions}
for year in years:
    for item in data:
        if item["year"] == year:
            for detail in item["details"]:
                region = regions_trans[detail["region"].lower()]
                cases_per_100k[region].append((detail["diagnoses"] / detail["population"]) * 100_000)

colors = {
    'Centro-Oeste': '#4E79A7',
    'Nordeste': '#F28E2B',
    'Norte': '#E15759',
    'Sul': '#F7DB4F',
    'Sudeste': '#59A14F',
    'Brasil': '#AF7AA1',
}

fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# Calculate average for each region
averages = {region: sum(values) / len(values) for region, values in cases_per_100k.items()}

# Sort the regions by their averages
sorted_regions = sorted(averages, key=averages.get, reverse=True)

# Plot each region with its corresponding color
for region in sorted_regions:
    values = cases_per_100k[region]
    ax.plot(years, values, marker='o', label=region, color=colors[region])

ax.set_xlabel("Ano de diagnóstico", fontsize=10, labelpad=10)
ax.set_ylabel("Taxa de detecção geral por 100 mil habitantes", fontsize=10, labelpad=10)
ax.legend(title="")
plt.xticks(years)
plt.grid(visible=True)

plt.show()