# -*- coding: utf-8 -*-
"""
Proj: pyecharts
Created on:   2020/6/29 18:15
@Author: RAMSEY

"""
"""
快速了解pyecharts中的一些基本图形
1.Bar
"""

from pyecharts.charts.basic_charts.bar import Bar
from pyecharts import options as opts


def plot_bar():
    x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋"]
    y1 = [5, 20, 36, 10, 75]
    y2 = [10, 25, 8, 60, 20]

    bar = Bar(init_opts=opts.InitOpts(width='1000px',height='600px'))
    # x轴数据
    bar.add_xaxis(xaxis_data=x)
    # y轴数据
    bar.add_yaxis(series_name="商家A", y_axis=y1)
    bar.add_yaxis(series_name="商家B", y_axis=y2)

    # 导出绘图html文件，可直接用浏览器打开
    bar.render('柱形图示范.html')


if __name__ == '__main__':
    # 1.绘制柱状图
    plot_bar()
