import matplotlib.pyplot as plt

# Sample data of Messi's Ballon d'Or rankings over the years
years = [2009, 2010, 2011, 2012, 2015, 2019]
rankings = [1, 1, 1, 1, 2, 1]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(years, rankings, marker='o', linestyle='-')
plt.title("Lionel Messi's Ballon D'Or Rankings Over the Years")
plt.xlabel("Year")
plt.ylabel("Ranking")
plt.grid(True)
plt.savefig('special.png')
plt.show()
