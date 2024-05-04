import matplotlib.pyplot as plt


cubic_nums_5 = [i**3 for i in range(1, 6)]
plt.plot(cubic_nums_5)
plt.title('First 5 Cubic Numbers')
plt.xlabel('Index')
plt.ylabel('Cubic Number')
plt.show()

cubic_nums_5000 = [i**3 for i in range(1, 5001)]
plt.figure(figsize=(10, 6))  
plt.plot(cubic_nums_5000)
plt.title('First 5,000 Cubic Numbers')
plt.xlabel('Index')
plt.ylabel('Cubic Number')
plt.show()