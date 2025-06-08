import matplotlib.pyplot as plt

coords = []
with open("mouse_movements.txt") as f:
    for line in f:
        try:
            x, y = map(int, line.strip().split(","))
            coords.append((x, y))
        except:
            continue

xs, ys = zip(*coords)
plt.plot(xs, ys, '.', markersize=1)
plt.gca().invert_yaxis()
plt.axis('equal')
plt.axis('off')
plt.show()
