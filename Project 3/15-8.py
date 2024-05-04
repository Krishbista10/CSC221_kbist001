import matplotlib.pyplot as plt
import numpy as np

rolls_1 = np.random.randint(1, 11, size=10000)
rolls_2 = np.random.randint(1, 11, size=10000)

sums = rolls_1 + rolls_2

plt.figure(figsize=(12, 6))
plt.hist(sums, bins=np.arange(1.5, 21.5, 1), color='olive', edgecolor='black', align='mid', density=True)

plt.title('Summing Two Ten-Sided Dice 10000 Times', fontsize=16)
plt.xlabel('Sum of Two Dice', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

plt.xticks(np.arange(2, 21, 2), rotation=45)
plt.yticks(np.arange(0, 0.21, 0.02))

plt.grid(axis='y', linestyle='-', alpha=0.7)

plt.tight_layout()

plt.show()