import matplotlib.pyplot as plt

criculo1 = plt.Circle((0, 0), 1, color='r')
criculo2 = plt.Circle((0, 0), 0.2, color='blue')
fig, ax = plt.subplots()
ax.add_patch(criculo1)
ax.add_patch(criculo2)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal', 'box')
plt.show()