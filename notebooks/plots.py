import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0, 2*np.pi, 100) 
f = np.sin(x)**2
g = np.sin(x)*np.cos(2*x)
plt.plot(x, f, linewidth=5,alpha=0.7, label="$\sin^2(x)$")
plt.plot(x, g, linewidth=5, alpha=0.7, label = "$\sin(x) \cos(2x)$")
plt.legend()
plt.show()
plt.savefig("plots.png")