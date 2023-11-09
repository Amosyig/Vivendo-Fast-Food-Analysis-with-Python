#import required modules
import matplotlib.pyplot as plt
import seaborn as sns

#set figure with specified size: 23 by 13
fig, ax = plt.subplots(figsize=(23, 13))

#data subset to be used 
data = df[['time_to_close', 'location']]

# Calculate the total observations  for each location 
total_observations = []
for each in all_locations:
    subset = data[data['location'] == each]
    count_per_location = subset["time_to_close"].count()
    total_observations.append(count_per_location)

#calculate the total outliers for each location
outliers = []
for each in all_locations:
    subset = data_outlier['time_to_close'].loc[data_outlier['location'] == each]
    outliers_per_location = subset.count()
    outliers.append(outliers_per_location)

# Define the categories
categories = all_locations

colors = ['cornflowerblue', 'lightblue', 'skyblue', 'steelblue']
colors.reverse()

# Create a stacked segmented bar chart
plt.bar(categories, total_observations, label='Total Observations', color = colors)
plt.bar(categories, outliers, color='grey', label='Outliers', bottom=total_observations)

# Add annotations to each box section
for i, (total, outlier) in enumerate(zip(total_observations, outliers)):
    annotation = plt.annotate(f'Total: {total}', (i, total / 2), ha='center', va='center', color='black', size = 20)
    white_border = withStroke(linewidth=4, foreground='white')
    annotation.set_path_effects([white_border])
    annotation = plt.annotate(f'({(total/sum(total_observations))*100} %)', (i, total / 2.5), ha='center', va='center', color='black', size = 16)
    
    white_border = withStroke(linewidth=4, foreground='white')
    annotation.set_path_effects([white_border])
    annotation = plt.annotate(f'Outliers: {outlier}', (i, total + (outlier / 2)), ha='center', va='center', color='black', size = 20)
    white_border = withStroke(linewidth=4, foreground='white')
    annotation.set_path_effects([white_border])
# Customize the plot
plt.title('Total Food Claims  Vs. Total Outlier Values of Time to Close By Location', size = 28)
plt.xlabel('Location', size = 20)
plt.ylabel('Count', size = 20)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)


# Show the plot
plt.show()
