import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)
points = np.random.uniform(0, 100, size=(100000, 3))
np.savetxt("synthetic_cloud.xyz", points)

def filterby_bbox(points, xmin, xmax, ymin, ymax, zmin, zmax):
    mask = ((points[:, 0] >= xmin) & (points[:, 0] <= xmax) &
            (points[:, 1] >= ymin) & (points[:, 1] <= ymax) &
            (points[:, 2] >= zmin) & (points[:, 2] <= zmax))
    return points[mask]

filtered = filterby_bbox(points, 20, 50, 30, 70, 10, 40)
np.savetxt("bbox_filtered.xyz", filtered)

high_points = points[points[:, 2] > 80]
np.savetxt("high_points.xyz", high_points)

def filter_by_distance(points, center, radius):
    distances = np.linalg.norm(points - center, axis=1)
    return points[distances <= radius]

near_center = filter_by_distance(points, center=np.array([50, 50, 50]), radius=20)
np.savetxt("near_center.xyz", near_center)

def show_cloud(points, title="Point Cloud", ax=None, color='b', subsample=False):
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
    plot_points = points[::20] if subsample else points
    ax.scatter(plot_points[:, 0], plot_points[:, 1], plot_points[:, 2], s=0.3, c=color)
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_box_aspect([1,1,1])
    return ax

fig = plt.figure(figsize=(12, 10))
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
show_cloud(points, "Original Cloud", ax=ax1, color='lightgray', subsample=True)

ax2 = fig.add_subplot(2, 2, 2, projection='3d')
show_cloud(points, "", ax=ax2, color='lightgray', subsample=True)
show_cloud(filtered, "BBox Filtered", ax=ax2, color='red')

ax3 = fig.add_subplot(2, 2, 3, projection='3d')
show_cloud(points, "", ax=ax3, color='lightgray', subsample=True)
show_cloud(high_points, "High Points", ax=ax3, color='green')

ax4 = fig.add_subplot(2, 2, 4, projection='3d')
show_cloud(points, "", ax=ax4, color='lightgray', subsample=True)
show_cloud(near_center, "Near Center", ax=ax4, color='blue')

plt.tight_layout()
plt.savefig("segmentation_results.png", dpi=150)

print(f"Исходное облако:          {len(points)} точек")
print(f"BBox-фильтр:              {len(filtered)} точек ({len(filtered)/len(points)*100:.2f}%)")
print(f"Высокие точки (Z > 80):   {len(high_points)} точек ({len(high_points)/len(points)*100:.2f}%)")
print(f"Радиус 20 от (50,50,50):  {len(near_center)} точек ({len(near_center)/len(points)*100:.2f}%)")