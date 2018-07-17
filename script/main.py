# -*- coding:utf-8 -*-
import numpy as np
from thrall.amap import session
from thrall.amap.consts import ExtensionFlag
from gistool import *


def get_city_polylines(keywords: str):
    """

    :param keywords: 地名关键词
    规则：只支持单个关键词语搜索关键词支持：行政区名称、citycode、adcode
    :return:
    """
    result = session.district(keywords, sub_district=0, extensions=ExtensionFlag(1))
    raw_polylines = result.data[0].polyline.split("|") if result.data else []

    return [
        Point.from_lnglat_str(polyline)
        for raw_polyline in raw_polylines
        for polyline in raw_polyline.split(";")
    ]


def get_city_cells(_polylines: [Point]):
    """

    :param _polylines:
    :return:
    """
    sorted_polylines_by_longitude = sorted(_polylines, key=lambda kv: kv.longitude)
    left = sorted_polylines_by_longitude[0]
    right = sorted_polylines_by_longitude[-1]

    sorted_polylines_by_latitude = sorted(_polylines, key=lambda kv: kv.latitude)
    bottom = sorted_polylines_by_latitude[0]
    top = sorted_polylines_by_latitude[-1]
    # print(sorted_polylines_by_longitude)
    # print(sorted_polylines_by_latitude)
    # print(left, right, top, bottom)
    # print(calculate_distance_km_between_two_point(left, right))

    longitude_precision = convert_distance_to_lnglat(
        Point(0, 0), distance=Cell.CELL_RADIUS * math.sqrt(3), angle=0).longitude
    latitude_precision = convert_distance_to_lnglat(
        Point(0, 0), distance=Cell.CELL_RADIUS * 3, angle=90).latitude
    # print(left.longitude, right.longitude + longitude_precision, longitude_precision)
    # print(bottom.latitude, top.latitude + latitude_precision, latitude_precision)

    return [
        Cell(Point(i, j))
        for i in np.arange(left.longitude, right.longitude + longitude_precision, longitude_precision)
        for j in np.arange(bottom.latitude, top.latitude + latitude_precision, latitude_precision)
    ]


if __name__ == "__main__":
    city_name = "上海"  # it has to be chinese keyword

    polylines = get_city_polylines(city_name)
    # print(*polylines, sep="\n")

    cells = get_city_cells(polylines)
    # print(*cells, sep="\n")
