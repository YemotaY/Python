import numpy as np
import time
from scipy.signal import convolve2d
from multiprocessing import Pool
import matplotlib.pyplot as plt

"""
Anpassbare Parameter:
num_simulations: Die Anzahl der zufällig generierten Muster.
size: Die Größe des Gitters (z.B. 50x50).
steps: Die Anzahl der Simulationsschritte.
time_threshold: Der Schwellenwert für die maximale Laufzeit.
point_threshold: Der Schwellenwert für die minimal erforderliche Punktzahl.
"""

def step(grid):
    """Berechnet den nächsten Schritt des Spiels mit Hilfe von Convolution."""
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    neighbor_count = convolve2d(grid, kernel, mode='same', boundary='wrap', fillvalue=0)
    return (neighbor_count == 3) | ((grid == 1) & (neighbor_count == 2))

def run_game_of_life(grid, steps=100):
    """Simuliert das Game of Life für eine gegebene Anzahl an Schritten."""
    for _ in range(steps):
        grid = step(grid)
    return grid

def measure_time_and_points(grid, steps=100):
    """Misst die Zeit und die Punktzahl des Gitters nach den Simulationen."""
    start_time = time.time()
    final_grid = run_game_of_life(grid, steps)
    elapsed_time = time.time() - start_time
    points = np.sum(final_grid)  # Lebende Zellen
    return elapsed_time, points, final_grid

def export_grid_as_image(grid, filename="grid_export.png"):
    """Exportiert das Gitter als Bilddatei."""
    plt.imshow(grid, cmap='binary')
    plt.axis('off')  # Achsen ausblenden
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    print(f"Grid exported as {filename}")

def simulate_and_compare(num_simulations=10, size=50, steps=100, time_threshold=10, point_threshold=10):
    """Simuliert mehrere zufällige Gitter und vergleicht deren Laufzeit und Punktzahl."""
    grids = [np.random.randint(2, size=(size, size)) for _ in range(num_simulations)]
    
    long_running_grids = []
    for i, grid in enumerate(grids):
        elapsed_time, points, final_grid = measure_time_and_points(grid, steps)
        print(f"Simulation {i + 1}: Time={elapsed_time:.2f}s, Points={points}")
        
        if elapsed_time > time_threshold and points < point_threshold:
            print(f"Long running grid detected! Exporting...")
            filename = f"grid_{i + 1}_export.png"
            export_grid_as_image(final_grid, filename)
            long_running_grids.append((elapsed_time, points, final_grid))
    
    return long_running_grids

if __name__ == "__main__":
    # Beispielaufruf der Simulation mit 10 zufälligen Mustern und einer maximalen Laufzeit von 10 Sekunden
    long_running_grids = simulate_and_compare(num_simulations=1000, size=50, steps=100, time_threshold=50, point_threshold=20)
