import numpy as np
from matplotlib import pyplot as plt
from shapely import Polygon, LineString, Point, unary_union
from shapely.plotting import plot_polygon, plot_points
from util.constant import Colors


class Map:
    def __init__(self):
        self.global_map = Polygon()
        self.map_blocks = []

    def gen_example_map(self):
        """
        生成一个简单的地图
        :return: Polygon
        """
        map_block1 = MapBlock(coord=np.array([(-2, -0.8), (-2, 1), (2, 1), (2, -0.8)]))
        map_block2 = MapBlock(coord=np.array([(-4, -2), (-4, 2), (-1, 2), (-1, -2)]))
        map_block3 = MapBlock(coord=np.array([(1.5, -1), (1.5, 2), (3.5, 2), (3.5, -1)]))
        self.global_map = unary_union([map_block1.polygon, map_block2.polygon, map_block3.polygon])
        self.map_blocks = [map_block1, map_block2, map_block3]
        return self.global_map

    def draw_global_map(self):
        fig = plt.figure(1, dpi=90)
        ax = fig.add_subplot(111)
        plot_polygon(self.global_map, ax=ax, add_points=False, color=Colors.GREEN)
        plot_points(self.global_map, ax=ax, color=Colors.GRAY, alpha=0.7)
        plt.show()

    def check_point_in_map(self, point: Point | np.ndarray | list):
        """
        检查点是否在地图内
        :param point: Point|np.ndarray|list
        :return: bool
        """
        if isinstance(point, (np.ndarray, list)):
            point = Point(point)
        return self.global_map.contains(point)


class MapBlock:
    """
    以方形房间为基础
    """

    def __init__(self, coord=np.array([(-1, -1), (-1, 1), (1, 1), (-1, 1)])):
        self.coord = coord
        self.polygon = Polygon(coord)

    def find_edge(self, which):
        minx, miny, maxx, maxy = self.polygon.bounds
        if which == "left":
            return LineString([(minx, miny), (minx, maxy)])

        elif which == "right":
            return LineString([(maxx, miny), (maxx, maxy)])

        elif which == "top":
            return LineString([(minx, maxy), (maxx, maxy)])

        elif which == "bottom":
            return LineString([(minx, miny), (maxx, miny)])

        else:
            raise ValueError("which must be 'left', 'right', 'top', or 'bottom', unknown value: {}".format(which))

    def find_corner_point(self, which):
        minx, miny, maxx, maxy = self.polygon.bounds

        if which == "left_top":
            return Point((minx, maxy))

        elif which == "left_bottom":
            return Point((minx, miny))

        elif which == "right_top":
            return Point((maxx, maxy))

        elif which == "right_bottom":
            return Point((maxx, miny))

        else:
            raise ValueError("which must be 'left_top', 'left_bottom', 'right_top', or 'right_bottom', "
                             "unknown value: {}".format(which))


if __name__ == "__main__":
    map = Map()
    map.gen_example_map()
    print(map.check_point_in_map(np.array([0.7,0.99])))
    map.draw_global_map()
