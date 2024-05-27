import matplotlib.pyplot as plt
from shapely.geometry import MultiPolygon
from shapely.plotting import plot_polygon, plot_points

from figures import SIZE, BLUE, GRAY, RED, set_limits

fig = plt.figure(1, figsize=SIZE, dpi=90)

# 1: valid multi-polygon
ax = fig.add_subplot(121)

a = [(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]
b = [(1, 1), (1, 2), (2, 2), (2, 1), (1, 1)]

multi1 = MultiPolygon([[a, []], [b, []]])

plot_polygon(multi1, ax=ax, add_points=False, color=BLUE)
plot_points(multi1, ax=ax, color=GRAY, alpha=0.7)

ax.set_title('a) valid')

set_limits(ax, -1, 3, -1, 3)

# 2: invalid self-touching ring
ax = fig.add_subplot(122)

from shapely.geometry import Polygon
from shapely.ops import unary_union

# 创建多个多边形
polygon1 = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
polygon2 = Polygon([(1, 0), (2, 0), (2, 1), (1, 1)])
polygon3 = Polygon([(0, 1), (1, 1), (1, 2), (0, 2)])

# 将这些多边形放在一个列表中
polygons = [polygon1, polygon2, polygon3]

# 使用 unary_union 合并多边形
merged_polygon = unary_union(polygons)

print(merged_polygon)

plot_polygon(merged_polygon, ax=ax, add_points=False, color=RED)
plot_points(merged_polygon, ax=ax, color=GRAY, alpha=0.7)

ax.set_title('b) invalid')

set_limits(ax, -1, 3, -1, 3)

plt.show()