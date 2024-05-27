import numpy as np

def test_map_block_find_edge():
    from map.map import MapBlock
    from shapely import LineString

    block = MapBlock(np.array([[-1,-1],[-1,1],[1,1],[1,-1]]))
    edge = block.find_edge("top")
    expected = LineString([[1,1],[-1,1]])
    assert edge.equals(expected)

def test_map_block_find_corner_point():
    from map.map import MapBlock
    from shapely import Point

    block = MapBlock(np.array([[-1,-1],[-1,1],[1,1],[1,-1]]))
    corner = block.find_corner_point("top_right")
    expected = Point(1,1)
    assert corner.equals(expected)