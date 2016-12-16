import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt


# Generate some random points for the demo.
np.random.seed(4321)
pts = 0.1 + 0.8*np.random.rand(15, 2)
print pts

ch = ConvexHull(pts)

# hull_indices = ch.vertices   # This will work in the scipy 0.13
hull_indices = np.unique(ch.simplices.flat)
hull_pts = pts[hull_indices, :]
print hull_pts

plt.plot(pts[:, 0], pts[:, 1], 'ko', markersize=10)
plt.plot(hull_pts[:, 0], hull_pts[:, 1], 'ro', alpha=.25, markersize=20)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()