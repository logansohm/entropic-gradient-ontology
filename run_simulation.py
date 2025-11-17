import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

phi_inverse = (np.sqrt(5) - 1) / 2

def dxdt(x, t):
    return (1 - x) - x**2

t = np.linspace(0, 50, 5000)
x0 = 1.0
x = odeint(dxdt, x0, t).flatten()

final_x = x[-1]
error = abs(final_x - phi_inverse)

print("Final x:", final_x)
print("Error vs φ^-1:", error)

plt.plot(t, x)
plt.axhline(phi_inverse, color='red', linestyle='--', label=f"φ^-1 = {phi_inverse:.3f}")
plt.legend()
plt.xlabel("Time")
plt.ylabel("x(t)")
plt.title("Convergence to φ^-1 = 0.618")
plt.grid(True)
plt.savefig("convergence.png")
plt.show()
