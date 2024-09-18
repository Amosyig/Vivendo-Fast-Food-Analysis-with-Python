# Vivendo-Fast-Food-Analysis-with-Python



![22892980_6683857](https://github.com/user-attachments/assets/ea0354a2-5072-40ac-9674-847591f412f0)


## Introduction
Data on the  food claims at Vivendo Restaurants across its four locations was analyzed using Pandas, Matplotlib, Seaborn, and NumPy.
The goal was to assist the manager in improving response times, addressing issues more efficiently, and closing food claims more quickly.


## Problem statement

This report answers the following business questions:

1. What are the total food claims by location?
2. What is the distribution of the total time it takes to close food claims?
3. How does each of the 4 locations differ in the time taken to close food claims?


## Skills/ concepts demonstrated:
- Pandas Data Cleaning & Transformation
- Matplotliib & Seaborn Data Visualization



## Python Visualization & Analysis:
![total_food_claims_per_location](https://github.com/user-attachments/assets/90b87747-23fe-445e-afb9-a072d31e67c7)

Recife has the highest total food claims, with 885, among all four locations.



![distribution_time_to_close_per_location](https://github.com/user-attachments/assets/cda19a87-b043-4343-a19c-5da1fcbf2615)

 The average time to close a food claim across these locations is 185.57 days, though this is skewed by outliers, with most claims taking between 120 and 250 days.
 

![distribution_time_without_outliers](https://github.com/user-attachments/assets/7f6acbf8-0850-4c74-9cdc-869c3712745c)

Without these outliers, the average time decreases to 177.67 days, an improvement of 7.9 days. 


![time_to_close_per_location](https://github.com/user-attachments/assets/fc2b07c0-07d8-4272-8f53-73445d363de3)

By location, the average time to close a claim is consistent: 184.61 days in Recife, 187.17 in Sao Luis, 185.31 in Fortaleza, and 185.93 in Natal.


![total_counts_vs_total_outliers](https://github.com/user-attachments/assets/32eaa577-e940-45fb-8b92-fc6592401b19)

The key difference is the proportion of outliers—Recife, which accounts for 45% of all claims, has the highest number of extreme values, followed by Sao Luis.


## Conclusion and Recommendations:

Efforts to improve response and resolution times for food claims should prioritize the Recife location. Addressing the issues there is likely to reduce the frequency of outlier 'time_to_claim' values, leading to a significant overall improvement in the time it takes to address food claims across all four locations.

This is a link to a medium post for more details: 

https://www.datascienceportfol.io/yole_amos/projects/3

Thanks!
