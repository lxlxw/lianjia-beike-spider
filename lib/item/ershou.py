#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构


class ErShou(object):
    def __init__(self, district, area, name, price, xiaoqu, danjia, floor, years, pattern, size, direction, tag):
        self.district = district
        self.area = area
        self.price = price
        self.name = name
        self.xiaoqu = xiaoqu
        self.danjia = str(danjia)
        self.floor = floor
        self.years = str(years)
        self.pattern = pattern
        self.size = str(size)
        self.direction = str(direction)
        self.tag = str(tag)

    def text(self):
        return self.district + "," + \
                self.area + "," + \
                self.name + "," + \
                self.price + "," + \
                self.xiaoqu + "," + \
                self.danjia + "," + \
                self.floor + "," + \
                self.years + "," + \
                self.pattern + "," + \
                self.size + "," + \
                self.direction + "," + \
                self.tag
