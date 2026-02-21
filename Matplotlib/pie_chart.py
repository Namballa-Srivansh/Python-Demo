#  Pie Chart - A pie chart is a circular chart divided into slices to show relative proportions of a whole
#              1.Each slice = a category
#              2.Size of slice = value of that category relative to total

# Prefferd for only Few Categories (5-6)

import matplotlib.pyplot as plt

expenses = ["Salaries", "Rent", "Marketing", "R&D", "Miscellaneous"]
amounts = [500, 150, 120, 100, 50]

# colors = ["red", "black", "green", "blue", "yellow"]
explode = [0, 0, 0, 0.2, 0]

plt.style.use("default")
plt.pie(amounts, labels=expenses, autopct="%1.1f%%",
        wedgeprops={
            "edgecolor" : "black",
            "linewidth" : 1,
            "linestyle" : "--",
            # "fill" : False 
        },
        explode=explode, # highlights specific slice with the given data
        startangle=0, # rotate vertically given any angle in anti-clockwise
        shadow=True # Creates shadow for 3D effect
        
    ) # autopct used to show percentage on pie chart
# Wedgeprops are used to design piechart 
plt.show()  