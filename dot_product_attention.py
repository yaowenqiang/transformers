import matplotlib.pyplot as plt
import numpy as np

hello = [0.71, 0.14, 0.51]
hi = [0.69, 0.15, 0.48]
tomato = [0.16, 0.59, 0.49]

fig = plt.figure(figsize=(16,12))
ax = fig.add_subplot(projection='3d')

xs = [hello[0], hi[0], tomato[0]]
ys = [hello[1], hi[1], tomato[1]]
zs = [hello[2], hi[2], tomato[2]]

ax.scatter(xs, ys, zs, s=100)

ax.set_xlim((0, 1))
ax.set_ylim((0, 1))
ax.set_zlim((0, 1))

#plt.show()


a = np.array(hello)
b = np.array(hi)
c = np.array(tomato)

print(np.matmul(a, b.T))
print(np.dot(a, b.T))
