import matplotlib.pyplot as plt
from random import choice

class ParticleWalk:
    """A class to generate and visualize particle walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determine the direction and distance for a step."""
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance
        return step

    def fill_walk(self):
        """Calculate all the points in the walk."""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def plot_walk(self, title, bg_color='light'):
        """Plot the particle walk and customize the plot."""
        plt.style.use('dark_background' if bg_color == 'dark' else 'classic')
        fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

        ax.plot(self.x_values, self.y_values, c='skyblue', linewidth=2, alpha=0.7, zorder=1)
        ax.scatter(0, 0, c='lime', edgecolors='black', s=100, zorder=2)
        ax.scatter(self.x_values[-1], self.y_values[-1], c='magenta', edgecolors='black', s=100, zorder=2)

        ax.set_title(title, fontsize=20, color='white' if bg_color == 'dark' else 'black')
        ax.set_xlabel("X", fontsize=16, color='white' if bg_color == 'dark' else 'black')
        ax.set_ylabel("Y", fontsize=16, color='white' if bg_color == 'dark' else 'black')

        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(False)

        if bg_color == 'dark':
            fig.patch.set_facecolor('black')

        plt.show()

pw = ParticleWalk()
pw.fill_walk()
pw.plot_walk("Particle Walk Simulation", bg_color='dark')