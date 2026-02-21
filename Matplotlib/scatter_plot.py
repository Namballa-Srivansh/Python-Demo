# A Scatter plot shows the relationship between two variables by plotting points on a 2D plane.
# Used for - Corelation, Outliers, Clusters

import matplotlib.pyplot as plt

# people = ["Person A", "Person B", "Person C", "Person D", "Person E"
#           "Person F", "Person G", "Person H", "Person I", "Person J"]

# age = [22, 25, 30, 35, 40, 45, 50, 55, 60, 65]
# bp = [110, 115, 120, 122, 125, 130, 135, 123, 145, 150]

# colors = ["green" if x < 135 else "red" for x in bp]

# plt.scatter(age, bp, color=colors, s=bp, alpha=0.5)
# plt.scatter(age, bp, s=bp, cmap="OrRd", c=bp) # color map provise spectrum of color and c is used to show the brightness by the values by using colormap 
# plt.title("Age Vs BP")
# plt.xlabel("Age")
# plt.ylabel("Blood Pressure")
 
# plt.grid()
# plt.colorbar(label="BP")

# Annotations - shows the value which point represent plt.annotate("text", xy(x_point, y_point), xytext=(x_text, y_text))

# for i in range(len(people)):
#     plt.annotate(people[i], xy=(age[i], bp[i]), xytext=(age[i] + 1, bp[i] + 1))

# plt.xlim(min(age), max(age) + 10)
# plt.ylim(min(bp), max(bp) + 5)
# plt.show()

# -----------------------------------------COMPARISON OF MULTIPLE DATA-------------------------

cities = ["City A", "City B", "City C", "City D", "City E"]

# Winter Temperatures (C) vs Humidity(%)
winter_temp = [5, 2, 10, 0, 7]
winter_humidity = [80, 75, 65, 85, 70]

# Summer Temperature (C) vs Humidity(%)
summer_temp = [25, 30, 28, 35, 27]
summer_humidity = [60, 50, 55, 45, 65]

plt.scatter(winter_temp, winter_humidity, label="Winter")
plt.scatter(summer_temp, summer_humidity, label="Summer")

plt.title("Summer vs Winter Data")
plt.xlabel("Temperature (C)")
plt.ylabel("Humidity (%)")
plt.legend()

plt.show()
