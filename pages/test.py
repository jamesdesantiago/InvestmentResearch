import streamlit as st
import json
import matplotlib.pyplot as plt

# Load data from a JSON file or directly from a JSON string
# Assuming the JSON data is stored in a file named 'data.json'
# with open('data.json', 'r') as file:
#     data = json.load(file)

# For the sake of example, let's assume we directly use the provided JSON data
json_data = """
{
  "priceIndexData": [
    {"x": {"label": "2019-01-01", "value": "2019-01-01"}, "y": {"max": {"label": "1,000", "value": 1000.0}, "mean": {"label": "1,000", "value": 1000.0}, "min": {"label": "1,000", "value": 1000.0}}},
    {"x": {"label": "2019-01-02", "value": "2019-01-02"}, "y": {"max": {"label": "1,000", "value": 999.6742}, "mean": {"label": "1,000", "value": 999.6742}, "min": {"label": "1,000", "value": 999.6742}}},
    {"x": {"label": "2019-01-03", "value": "2019-01-03"}, "y": {"max": {"label": "999", "value": 998.93896}, "mean": {"label": "999", "value": 998.93896}, "min": {"label": "999", "value": 998.93896}}},
    // Add more data points as needed
  ]
}
"""

# Parse the JSON data
data = json.loads(json_data)

# Extract priceIndexData
price_index_data = data['priceIndexData']

# Initialize lists to store the extracted values
dates = []
max_values = []
mean_values = []
min_values = []

# Extract values from the data
for item in price_index_data:
    dates.append(item['x']['label'])
    max_values.append(item['y']['max']['value'])
    mean_values.append(item['y']['mean']['value'])
    min_values.append(item['y']['min']['value'])

# Create a plot
plt.figure(figsize=(10, 5))
plt.plot(dates, max_values, label='Max Price Index')
plt.plot(dates, mean_values, label='Mean Price Index')
plt.plot(dates, min_values, label='Min Price Index')
plt.xlabel('Date')
plt.ylabel('Price Index')
plt.title('Price Index Data Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(plt)
