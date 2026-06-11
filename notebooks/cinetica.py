"""
modulo para hacer ajustes de cinéticas y graficar los resultados
"""
import numpy as np
import matplotlib.pyplot as plt

def exponetial_fit(x, a, b, c):
     return a * np.exp(-b * x) + c
    
def plot_ajuste(x,y, y_fit):
    fig, ax = plt.subplots(2,1, figsize=(7,4), sharex=True)
    ax[0].plot(x,y, '.')
    ax[0].plot(x, y_fit, '-')
    ax[1].plot(x, y-y_fit, '.')
    ax[1].axhline(0, alpha=0.7, c='C1')
    ax[0].set_ylabel("absorbance")
    ax[1].set_ylabel("error")
    ax[0].set_xlabel("time")
    ax[1].set_xlabel("time")
    ax[1].set_title("residuals")
    plt.tight_layout()
    plt.show()
    return fig

print("hola desde el modulo cinética")