# -*- coding: utf-8 -*-
"""
Proj: pyecharts
Created on:   2020/6/29 18:15
@Author: RAMSEY

"""

import pandas as pd
from pyecharts.charts.basic_charts.bar import Bar
from pyecharts.charts.basic_charts.line import Line
from pyecharts.charts.basic_charts.scatter import Scatter
from pyecharts import options as opts

"""
快速了解pyecharts中的一些基本图形
1.柱状图:Bar
2.折线图:Line
"""


def plot_bar():
    """
    绘制柱状图:
        Bar
    :return:
    """
    # 初始化数据来源
    x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋"]
    y1 = [5, 20, 36, 10, 75]
    y2 = [10, 25, 8, 60, 20]

    #  初始化柱状图
    bar = Bar(init_opts=opts.InitOpts(width='1000px', height='600px'))

    # x轴数据
    bar.add_xaxis(xaxis_data=x)
    # y轴数据
    bar.add_yaxis(series_name="商家A", y_axis=y1)
    bar.add_yaxis(series_name="商家B", y_axis=y2)

    # 导出绘图html文件，可直接用浏览器打开
    bar.render('柱状图示范.html')


def plot_line():
    """
    绘制折线图:
        line
    :return:
    """

    # 初始化数据来源
    x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋"]
    y1 = [5, 20, 36, 10, 75]
    y2 = [10, 25, 8, 60, 20]

    # 初始化折线图
    line = Line(init_opts=opts.InitOpts(width="900px", height="500px"))

    # x轴数据
    line.add_xaxis(xaxis_data=x)

    # y轴数据
    line.add_yaxis(series_name='商家A', y_axis=y1)
    line.add_yaxis(series_name='商家B', y_axis=y2)

    # 导出绘图html文件，可直接用浏览器打开
    line.render('折线图示范.html')


def plot_scatter():
    """
    绘制散点图:
        scatter
    :return:None
    """

    # 初始化数据来源:
    # 男孩和女孩的体重(kg)和身高(cm)
    # 1.男孩
    boy_weight_height = pd.DataFrame()
    boy_weight_height['weight'] = [56, 67, 65, 70, 57, 60, 80, 85, 76, 64]
    boy_weight_height['height'] = [162, 170, 168, 172, 168, 172, 180, 176, 178, 170]
    # 2.女孩
    girl_weight_height = pd.DataFrame()
    girl_weight_height['weight'] = [50, 62, 60, 70, 57, 45, 62, 65, 70, 56]
    girl_weight_height['height'] = [155, 162, 165, 170, 166, 158, 160, 170, 172, 165]

    # 初始化散点图
    scatter = Scatter(init_opts=opts.InitOpts(width="900px", height="500px"))

    # 添加数据
    scatter.add_xaxis(xaxis_data=boy_weight_height['weight'])
    scatter.add_yaxis(series_name='男孩', y_axis=boy_weight_height['height'])
    scatter.add_xaxis(xaxis_data=girl_weight_height['weight'])
    scatter.add_yaxis(series_name='女孩', y_axis=girl_weight_height['height'])

    # 设置图形显示属性
    scatter.set_global_opts(title_opts=opts.TitleOpts(title='不同性别身高体重分布'))

    # 绘制散点图
    scatter.render('散点图示范.html')


if __name__ == '__main__':
    # 1.绘制柱状图
    # plot_bar()
    # 2.绘制折线图
    # plot_line()
    # 3.绘制散点图
    plot_scatter()
