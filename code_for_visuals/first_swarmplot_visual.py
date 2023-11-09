#import required modules
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patheffects import withStroke


#create a new figure with a specific size: 20 by 13
fig, ax = plt.subplots(figsize=(20, 13))

outlier_radius = 0.1  
gradient_colors = ['blue'] 
annotation_color = 'black'

#data values of dataframe
data = df['time_to_close'].values

# Calculate the quartiles and interquartile range
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

# Define the upper bounds for identifying outliers
upper_bound = q3 + 1.5 * iqr

# Create a list to identify outliers
normal_mask = (data < upper_bound)
outlier_mask = (data > upper_bound)

# Plot the swarm plot with custom colors
chart = sns.swarmplot(y = data[normal_mask], ax = ax, color = 'blue', size =6.5)
chart = sns.swarmplot(y=data[outlier_mask], color='gray', ax = ax, size = 6.5)

# Calculate the mean sepal length
mean_all= data.mean()

# Annotate the mean with a labeled line
chart.axhline(mean_all, color="black", linestyle="-", )
annotation = plt.text(0, mean_all, f'Mean: {mean_all:.2f} Days', ha='center', va='bottom', fontsize=18, color='red', fontweight= 'bold')

# Add a white border to the annotation text
white_border = withStroke(linewidth=4, foreground='white')
annotation.set_path_effects([white_border])

# Create a custom legend
legend_gray = plt.Line2D([0], [0], marker='o', color='w', label='Gray', markerfacecolor='gray', markersize=10)
legend_blue = plt.Line2D([0], [0], marker='o', color='w', label='Blue', markerfacecolor='blue', markersize=10)

# Add the legend at the top right of the visual
plt.legend(handles=[legend_gray, legend_blue], loc='upper right')

# Create a custom legend
legend_gray = plt.Line2D([0], [0], marker='o', color='w', label='Outlier Values', markerfacecolor='gray', markersize=30)
legend_blue = plt.Line2D([0], [0], marker='o', color='w', label='Normal Values', markerfacecolor='blue', markersize=30)

# Add the legend at the top right of the visual
plt.legend(handles=[legend_gray, legend_blue], loc='upper right', handlelength = 8, handleheight = 5, fontsize = 20, frameon = False)

# Add labels and title
plt.title('Distribution of Time to Close (All Locations)', size=24)
plt.ylabel('Time to Close (Days)' ,size = 18)
plt.yticks(fontsize = 18)

# Show the plot
plt.show()
