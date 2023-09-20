# importeer alle nodige libraries

import numpy as np
import matplotlib.pyplot as plt

def calculate_mandelbrot(c: complex, max_iter: int) -> int:
    """
    Calculate the diverging index for a given complex number c in the Mandelbrot set.
    
    Args:
        c (complex): The complex number for which we want to calculate the diverging index.
        max_iter (int): The maximum number of iterations to check for divergence.
        
    Returns:
        int: The diverging index (or 0 if it does not diverge).
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return 0

def generate_mandelbrot_image(width: int, height: int, x_range: tuple, y_range: tuple, max_iter: int) -> np.ndarray:
    """
    Generate a Mandelbrot image.

    Args:
        width (int): Width of the image.
        height (int): Height of the image.
        x_range (tuple): Tuple containing the minimum and maximum x values for the range.
        y_range (tuple): Tuple containing the minimum and maximum y values for the range.
        max_iter (int): The maximum number of iterations to check for divergence.

    Returns:
        np.ndarray: A numpy array representing the Mandelbrot image.
    """
    x_min, x_max = x_range
    y_min, y_max = y_range
    image = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            x = x_min + (x_max - x_min) * j / (width - 1)
            y = y_min + (y_max - y_min) * i / (height - 1)
            c = complex(x, y)
            image[i, j] = calculate_mandelbrot(c, max_iter)

    return image

def plot_mandelbrot_image(image: np.ndarray, colormap='hot'):
    """
    Visualize the Mandelbrot image using a specified colormap.

    Args:
        image (np.ndarray): A numpy array representing the Mandelbrot image.
        colormap (str): The name of the colormap to use (e.g., 'hot', 'viridis', 'jet', etc.).
    """
    plt.imshow(image, cmap=colormap, extent=[-1.5, 0.5, -1, 1])
    plt.colorbar()
    plt.title('Mandelbrot Set')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.show()

# Example usage with a different colormap (e.g., 'viridis'):
if __name__ == '__main__':
    mandelbrot_image = generate_mandelbrot_image(200, 200, (-1.5, 0.5), (-1, 1), max_iter=100)
    plot_mandelbrot_image(mandelbrot_image, colormap='twilight_shifted')