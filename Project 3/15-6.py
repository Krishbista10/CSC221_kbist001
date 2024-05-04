import matplotlib.pyplot as plt
import random

def roll_dice():
    return random.randint(1, 10) + random.randint(1, 10)

num_rolls = 10000

results = [roll_dice() for _ in range(num_rolls)]

frequency = [results.count(i) for i in range(2, 21)]

plt.figure(figsize=(12, 6))
plt.bar(range(2, 21), frequency, color='coral', edgecolor='black')

plt.xlabel('Sum of Two Dice', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title(f'Frequency of Sum of Two 10-Sided Dice ({num_rolls} Rolls)', fontsize=16)

plt.xticks(range(2, 21, 2), rotation=45)
plt.yticks(range(0, max(frequency) + 500, 500))

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()