#import matplotlib.pyplot & seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# set the default style
sns.set()

# Create a new figure with a specified size
plt.figure(figsize=(12, 7))

# Define a list of colors for the bars and reverse the order
colors = ['cornflowerblue', 'lightblue', 'skyblue', 'steelblue']
colors.reverse()

# Define a list of locations
all_locations = ['Recife', 'Sao Luis', 'Fortaleza', 'Natal']

# Define the values (counts of food claims) for each location
values = [885, 517, 311, 287]

# Create a bar chart with locations on the x-axis and values on the y-axis, using specified colors
plt.bar(all_locations, values, color=colors)

# Calculate the total sum of values
total = sum(values)

# Iterate through each bar in the bar chart
for rect in plt.gca().patches:
    # Get the height of the current bar
    height = rect.get_height()
    
    # If the height is greater than 0, annotate the bar with its value
    if height > 0:
        plt.gca().annotate(f'{height}  ', xy=(rect.get_x() + rect.get_width() / 2, height),
                           xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')

# Set the title of the chart
plt.title('Total Food Claims by Location', size=18)

# Label the y-axis
plt.ylabel('Count of Food Claims')

# Label the x-axis
plt.xlabel('Location')

# Show the bar chart
plt.show()
