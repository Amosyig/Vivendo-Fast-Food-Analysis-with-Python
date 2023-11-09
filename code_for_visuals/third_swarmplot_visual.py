#data 
data = df['time_to_close'].values

# Create the figure and set the background color
fig, ax = plt.subplots(figsize=(23, 13))
#fig.set_facecolor('lightgray')  # Set the background color of the entire figure

# Create the violin plot


# Annotate values that are considered outliers with small circles
outlier_radius = 0.1  # Adjust the size of the circles as needed

# Define custom colors for the gradient fill with increased opacity (alpha)
gradient_colors = ['blue']  # Use your preferred gradient colors

# Define annotation color
annotation_color = 'black'



# Calculate the quartiles and interquartile range
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

# Define the lower and upper bounds for identifying outliers
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr



# Create a list to identify outliers
normal_mask = (data < upper_bound)
outlier_mask = (data > upper_bound)

category_order = all_locations

colors = {'Recife': 'steelblue', 'Sao Luis': 'skyblue', 'Fortaleza': 'lightblue', 'Natal':'cornflowerblue'}


# Plot the swarm plot with custom colors
chart = sns.swarmplot(x = df['location'][normal_mask], y = data[normal_mask], ax = ax, size =5, order=category_order, palette = colors)
chart = sns.swarmplot(x = df['location'][outlier_mask], y=data[outlier_mask], color='gray', ax = ax, size = 5, order=category_order)





data = df[['time_to_close', 'location']]
# Calculate the mean sepal length for each category
for each in all_locations:
    subset = data[data['location'] == each]
    mean_per_location = subset["time_to_close"].mean()

    # Annotate the mean with a labeled line for each category
    #plt.axhline(mean_per_location, color="black", linestyle="-")
    annotation = plt.text(all_locations.index(each), mean_per_location, f'Mean: {mean_per_location:.2f} Days', ha='center', va='bottom', fontsize=20, color='red')
    # Add a white border to the annotation text
    white_border = withStroke(linewidth=4, foreground='white')
    annotation.set_path_effects([white_border])


# Create a custom legend
legend_gray = plt.Line2D([0], [0], marker='o', color='lightgray', label='Outlier Values', markerfacecolor='gray', markersize=20)
#legend_blue = plt.Line2D([0], [0], marker='o', color='w', label='Normal Values', markerfacecolor='steelblue', markersize=30)

# Add the legend at the top right of the visual
plt.legend(handles=[legend_gray], loc='upper right', handlelength = 10, handleheight = 7, fontsize = 20, frameon = False)


# Customize the plot
# Add labels and title
plt.title('Distribution of Time to Close by Location', size=28)
plt.ylabel('Time to Close (Days)', size = 18)
plt.xlabel('Location', size = 18)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
# Show the plot
plt.show()
