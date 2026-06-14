import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the geospatial sales and demand dataset
try:
    df = pd.read_csv('sales_location_data.csv')
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: 'sales_location_data.csv' not found. Please ensure it is in the same folder.")
    exit()

# 2. Identify high demand but low current sales regions (Potential Expansion Areas)
# Criteria: Demand Score > 70 and Current Sales < 50,000
df['Expansion_Priority'] = 'Low'
df.loc[(df['Demand_Score'] > 70) & (df['Current_Sales'] < 50000), 'Expansion_Priority'] = 'HIGH'

print("--- Geolocation Expansion Analysis ---")
print(df[['Region', 'Latitude', 'Longitude', 'Demand_Score', 'Current_Sales', 'Expansion_Priority']])

# 3. Visualize the geographical regions
plt.figure(figsize=(10, 6))

# Plot regular regions
regular_regions = df[df['Expansion_Priority'] == 'Low']
plt.scatter(regular_regions['Longitude'], regular_regions['Latitude'], 
            s=regular_regions['Demand_Score']*3, c='blue', alpha=0.5, label='Stable Market')

# Highlight expansion opportunities
high_priority = df[df['Expansion_Priority'] == 'HIGH']
plt.scatter(high_priority['Longitude'], high_priority['Latitude'], 
            s=high_priority['Demand_Score']*5, c='red', alpha=0.8, edgecolors='black', label='HIGH Opportunity (High Demand / Low Presence)')

# Annotate region names
for i, txt in enumerate(df['Region']):
    plt.annotate(txt, (df['Longitude'].iloc[i]+0.1, df['Latitude'].iloc[i]+0.1), fontsize=9)

plt.title('Geospatial Analysis: Optimal Areas for Business Expansion', fontsize=14, fontweight='bold')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left')
plt.tight_layout()

# Save the map visualization
plt.savefig('geospatial_expansion_map.png')
print("\nVisualization saved as 'geospatial_expansion_map.png'!")
