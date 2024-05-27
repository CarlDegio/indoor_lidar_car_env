import numpy as np
from matplotlib import pyplot as plt
from shapely import LineString, Point, Polygon
from shapely.plotting import plot_polygon, plot_points

from map.map import Map
from util.constant import Colors


class Lidar:
    def __init__(self, radius=1.0, scan_angle=1.5 * np.pi, num=20):
        self.radius = radius
        self.scan_angle = scan_angle
        self.num = num

    def calc_intersection_points_and_distance(self, pos, angles, map: Map):
        distances = []
        points = []
        for angle in angles:
            scan_line = LineString([pos, pos + self.radius * np.array([np.cos(angle), np.sin(angle)])])
            intersections = map.global_map.intersection(scan_line)

            if isinstance(intersections, LineString):
                scan_segment = intersections
            else:
                scan_segment = intersections.geoms[0]

            pt = scan_segment.coords[1]
            distance = Point(pos).distance(Point(pt))
            points.append(pt)
            distances.append(distance)
        return points, distances

    def observe(self, pos, heading, map: Map):
        if not map.check_point_in_map(pos):
            raise ValueError("Lidar can't observe outside the map")

        # 逆时针观测，从负角到正角
        angles = np.linspace(heading - self.scan_angle / 2, heading + self.scan_angle / 2, self.num)
        points, distances = self.calc_intersection_points_and_distance(pos, angles, map)

        return distances

    def observe_with_render(self, pos, heading, map: Map):
        if not map.check_point_in_map(pos):
            raise ValueError("Lidar can't observe outside the map")

        fig = plt.figure(1, dpi=90)
        ax = fig.add_subplot(111)
        plot_polygon(map.global_map, ax=ax, add_points=False, color=Colors.GREEN)
        plot_points(map.global_map, ax=ax, color=Colors.GRAY, alpha=0.7)

        # 逆时针观测，从负角到正角
        angles = np.linspace(heading - self.scan_angle / 2, heading + self.scan_angle / 2, self.num)
        points, distances = self.calc_intersection_points_and_distance(pos, angles, map)

        for pt in points:
            ax.plot(*pt, 'ro')
            ax.plot([pos[0], pt[0]], [pos[1], pt[1]], 'r-')
        ax.set_aspect('equal', adjustable='box')  # equal aspect ratio
        plt.show()
        return distances


class SideLidar(Lidar):
    def __init__(self):
        super().__init__(radius=0.3, scan_angle=0.0, num=1)

    def observe(self, pos, heading, map: Map):
        heading = heading - np.pi / 2
        distance = super().observe(pos, heading, map)
        return distance


if __name__ == "__main__":
    map = Map()
    map.gen_example_map()
    lidar = Lidar()
    print(lidar.observe_with_render(np.array([0.7, 0.5]), 0, map))

    side_lidar = SideLidar()
    print(side_lidar.observe(np.array([0.7, 0.5]), 0, map))
