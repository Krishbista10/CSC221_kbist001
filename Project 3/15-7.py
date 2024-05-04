import matplotlib.pyplot as plt
import random

def roll_dice():
    return random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8)

num_rolls = 10000

results = [roll_dice() for _ in range(num_rolls)]

frequency = [results.count(i) for i in range(3, 25)]

plt.figure(figsize=(12, 6))
plt.bar(range(3, 25), frequency, color='gold', edgecolor='black')

plt.xlabel('Sum of Three Dice', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title(f'Frequency of Sum of Three 8-Sided Dice ({num_rolls} Rolls)', fontsize=16)

plt.xticks(range(3, 25, 3), rotation=45)
plt.yticks(range(0, max(frequency) + 200, 200))

plt.grid(axis='y', linestyle='-', alpha=0.7)

plt.show()