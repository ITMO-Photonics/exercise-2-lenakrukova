import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5.,5.,500)
def f(x):
    return np.sqrt(np.abs(x))*np.sin(x*x)
fig,ax=plt.subplots()
ax.plot(x,f(x))
plt.show()
 
