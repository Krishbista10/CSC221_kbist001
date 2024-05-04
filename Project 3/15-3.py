import matplotlib.pyplot as plt
from random_walk import RandomWalk

def simulate_pollen_grain():
    while True:
        rw = RandomWalk(5000)
        rw.fill_walk()

        fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

        ax.plot(rw.x_values, rw.y_values, linewidth=1, color='blue')

        ax.scatter(0, 0, c='green', edgecolors='none', s=100)
        ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

        ax.set_xticks([])
        ax.set_yticks([])

        ax.set_title("Pollen Grain Path on Water Drop")
        ax.set_xlabel("X-Value")
        ax.set_ylabel("Y-Value")

        plt.show()

        keep_running = input("Simulate another pollen grain path? (y/n): ")
        if keep_running.lower() == 'n':
            break

simulate_pollen_grain()