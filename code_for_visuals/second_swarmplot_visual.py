#import required modules
import matplotlib.pyplot as plt
import seaborn as sns

# Plot the swarm plot with custom colors
fig, ax = plt.subplots(figsize=(20, 13))

#dat
data = df['time_to_close'].values

chart = sns.swarmplot(y = data[normal_mask], ax = ax, color = 'blue', size =6.5)
mean_without_outliers = data[normal_mask].mean()

# Annotate the mean with a labeled line
chart.axhline(mean_without_outliers, color="black", linestyle="-", )
annotation = plt.text(0, mean_without_outliers, f'Mean: {mean_without_outliers:.2f} Days', ha='center', va='bottom', fontsize=18, color='red')

# Add a white border to the annotation text
white_border = withStroke(linewidth=4, foreground='white')
annotation.set_path_effects([white_border])





#add labels and titles
plt.title('Distribution of Time to Close Without Outliers  (All Locations)', size=24)
plt.ylabel('Time to Close (Days)',size = 18)
plt.yticks(fontsize = 18)

plt.show()
