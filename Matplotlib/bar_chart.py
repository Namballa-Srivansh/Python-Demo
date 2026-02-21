import matplotlib.pyplot as plt
import numpy as np

oscar_movies = [
    "The Dark Knight",
    "The Hurt Locker",
    "The King's Speech",
    "The Artist",
    "Argo"
]

years = [2000, 2009, 2010, 2011, 2012]
oscar_revenues = [1005, 170, 427, 133, 232] #in $M

# plt.bar(years, oscar_revenues, color="Red")
# plt.title("Revenue in each year of oscar movies")
# plt.xlabel("Years")
# plt.ylabel("Revenue (in $M)")
# for i in range(len(years)):
#     plt.text(years[i], oscar_revenues[i] + 10, str(oscar_revenues[i]), ha="center") # create values or labels for bar (x-axis pos, y-axis pos, text, alignment)

# plt.ylim(0, max(oscar_revenues) + 100) # sets the limit or can increase the limit or size of the graph
# plt.show()

# ---------------------------------------------COMPARING 2 SETS OF DATA------------------------------------------

non_oscar_movies = [
    "Slumdog Millionaire", 
    "Avatar", 
    "Inception", 
    "Hugo", 
    "Lincoln"
]
non_oscar_revenue = [378, 2788, 829, 185, 275] # in $M

# We customise width. Width controls how thick each bar is. Usually ranges from 0 to 1.
# [Default val is 0.8]
# We do this because the bars overlaps with each other because the x - axis data is same for both graphs

# x = np.arange(len(years))

# width = 0.4
# plt.bar(x - width / 2, oscar_revenues, width, label="Oscar Movies") #Shifting the bar to LEFT
# plt.bar(x + width / 2, non_oscar_revenue, width, label="Non-Oscar Movies") # Shifting the bar to RIGHT

# plt.title("Oscar vs Non-Oscar Movies Revenue")
# plt.xlabel("Year")
# plt.ylabel("Revenue($M)")
# plt.legend()

# plt.xticks(x, years) # replaces label i.e x with years

# plt.show()

# ----------------------------------HORIZONTAL CHART-------------------------------------------

plt.barh(oscar_movies, oscar_revenues)
plt.xlabel("Revenue ($M)")
plt.ylabel("Movies")
plt.show()