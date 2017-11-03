import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
plt.figure(1)
# red dashes, blue squares and green triangles
plt.subplot(311)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, np.exp(t), 'r--')
# plt.subplot(312)
# t = np.arange(0., 5., 0.001)
# l = [0, 5]
# plt.plot(t, np.sin(2*np.pi*t), 'r-', [0, 5], [0, 0], '-')
# plt.subplot(313)
# t = np.arange(-1., 1., 0.01)
# r = 1
# plt.plot(t, np.sqrt(1-t**2), 'g--',t, -np.sqrt(1-t**2), 'g--')
plt.show()