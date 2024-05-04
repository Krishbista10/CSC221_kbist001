import matplotlib.pyplot as plt
import numpy as np


cubic_nums_5000 = [i**3 for i in range(1, 5001)]
x = np.arange(1, 5001)  

plt.figure(figsize=(10, 6))
plt.scatter(x, cubic_nums_5000, c=cubic_nums_5000, cmap='viridis', s=5)  
plt.colorbar() 
plt.title('First 5,000 Cubic Numbers with Colormap')
plt.xlabel('Index')
plt.ylabel('Cubic Number')
plt.show()