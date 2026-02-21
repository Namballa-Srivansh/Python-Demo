import matplotlib.pyplot as plt

plt.style.use('default') # changing background of plot
# print(plt.style.available)

# X = [1, 2, 3, 4]
# Y = [5, 6, 7, 8]

# plt.plot(X, Y)
# plt.show() # Line Port

oscar_movies = [
    "The Dark Knight",
    "The Hurt Locker",
    "The King's Speech",
    "The Artist",
    "Argo"
]

years = [2000, 2009, 2010, 2011, 2012]
oscar_revenues = [1005, 170, 427, 133, 232] #in $M

# plt.plot(years, oscar_revenues)

# plt.title("Oscar Movies Revenue in each Year")
# plt.xlabel("Years")
# plt.ylabel("Revenues (in $M)")
# plt.show()

non_oscar_movies = ["Slumdog Millionaire", "Avatar", "Inception", "Hugo", "Lincoln"]
non_oscar_years = [2000, 2009, 2010, 2011, 2012]
non_oscar_revenue = [378, 2788, 829, 185, 275] # in $M

# plt.plot(years, oscar_revenues, "o--r", label="Oscar Movies") # o--r is format string fmt = [marker][line][color]
# plt.plot(years, non_oscar_revenue, "<-g", label="Non-Oscar Movies")

# plt.title("Oscar Movies vs Non-Oscar Movies Revenue")
# plt.xlabel("Year")
# plt.ylabel("Revenue (in $M)")
# plt.legend()
# plt.show()

# -----------------------------METHODS AND ATTRIBUTES------------------------------------------

# with plt.xkcd(): # cartoonish plot
#     plt.plot(years, oscar_revenues, label="Oscar Movies") 
#     plt.plot(years, non_oscar_revenue, label="Non-Oscar Movies")

#     plt.title("Oscar Movies vs Non-Oscar Movies Revenue")
#     plt.xlabel("Year")
#     plt.ylabel("Revenue (in $M)")
#     plt.legend()
#     # plt.grid()

#     plt.show()


plt.plot(oscar_movies, oscar_revenues)
plt.title("Movies Revenue")
plt.xlabel("Movies")
plt.ylabel("Revenue (in $M)")
plt.tight_layout() # prevent over lap of labels
plt.savefig("final_plot.png")
plt.show()