# importeer alle nodige libraries
import numpy as np
import matplotlib.pyplot as plt

# maak verschillende functies

def calculate_mandelbrot(c) -> int:
    """
    Bereken de diverging index voor een gegeven complex getal c.    
    Args:
        complexe getal c.
        
    Returns:
        int: De diverging index.
    """
    a = 0
    for n in range(100):
        if abs(a) > 2:
            return n
        a = a**2 + c
    return 0

def draw_mandel(width):
    """
    Generaten van een Mandelbrot image.

    Args:
        width: Breedte en hoogte van het plaatje.

    Returns:
        Een numpy array voor het Mandelbrot plaatje met coördinaten.
    """
    x_min, x_max = (-1.5, 0.5)
    y_min, y_max = (-1, 1)
    image = np.zeros((width, width))

    for i in range(width):
        for j in range(width):     
            x = x_min + (x_max - x_min) * j / (width - 1)
            y = y_min + (y_max - y_min) * i / (width - 1)
            c = complex(x, y)
            image[i, j] = calculate_mandelbrot(c)

    return image

def plot_mandelbrot_image(image):
    """
    Plaatje maken met matplotlib :)

    Args:
        De coördinaten array.
    Output:
        Mandelbrot plaatje met mooie kleuren, voor andere mooie kleuren: twilight_shifted ;)
    """
    plt.imshow(image, cmap='gnuplot2', extent=[-1.5, 0.5, -1, 1])
    plt.title('Mandelbrot Plaatje')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.show()


mandelbrot_image = draw_mandel(200)
plot_mandelbrot_image(mandelbrot_image)