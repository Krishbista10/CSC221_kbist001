import matplotlib.pyplot as plt
from random_walk import RandomWalk

def simulate_particle_path():
    while True:
        rw = RandomWalk(5000)
        rw.fill_walk()

        fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

        plt.style.use('dark_background')

        ax.plot(rw.x_values, rw.y_values, c='cyan', linewidth=3, alpha=0.7, zorder=1)

        ax.scatter(0, 0, c='lime', edgecolors='black', s=120, zorder=2)
        ax.scatter(rw.x_values[-1], rw.y_values[-1], c='magenta', edgecolors='black', s=120, zorder=2)

        ax.set_title("Particle Path Simulation", fontsize=20, color='white')
        ax.set_xlabel("X", fontsize=16, color='white')
        ax.set_ylabel("Y", fontsize=16, color='white')

        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(False)

        fig.patch.set_facecolor('black')

        plt.show()

        keep_running = input("Simulate another particle path? (y/n): ")
        if keep_running.lower() == 'n':
            break

simulate_particle_path()