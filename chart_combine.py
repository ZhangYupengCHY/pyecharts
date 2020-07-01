# -*- coding: utf-8 -*-
"""
Proj: pyecharts
Created on:   2020/7/1 9:35
@Author: RAMSEY

"""
import os

from pyecharts.charts.basic_charts.bar import Bar
from pyecharts.charts.basic_charts.line import Line
from pyecharts.charts.composite_charts.grid import Grid
from pyecharts.charts.composite_charts.page import Page
from pyecharts.charts.composite_charts.timeline import Timeline
from pyecharts import options as opts
from random import randint

"""
图表组合:
    主要有四种方式:Grid,tab,Page,Timeline
    1.Grid
    2.Page
    3.Timeline
"""


def plot_grid():
    """
    使用Grid来绘制组合图
    子图的宽高是自适应画板(Grid)的宽高
    子图的位置用grid_opts中pos选项来调节:
        当两个子图为pos_left与pos_right时,此时为左右排列
        当两个子图为pos_top与pos_bottom时,此时为上下排列
    :return: html
    """
    # 1.首先绘制一个柱状图
    # 初始化数据来源
    x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋"]
    y1 = [5, 20, 36, 10, 75]
    y2 = [10, 25, 8, 60, 20]

    #  初始化柱状图
    bar = Bar(init_opts=opts.InitOpts(width='200px', height='100px'))

    # x轴数据
    bar.add_xaxis(xaxis_data=x)
    # y轴数据
    bar.add_yaxis(series_name="商家A", y_axis=y1)
    bar.add_yaxis(series_name="商家B", y_axis=y2)

    # 设置配置
    bar.set_global_opts(title_opts=opts.TitleOpts(title='柱状图:商家货物销量'))

    # 2.绘制一个折线图
    # 初始化数据来源
    x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋"]
    y1 = [5, 20, 36, 10, 75]
    y2 = [10, 25, 8, 60, 20]

    # 初始化折线图
    line = Line(init_opts=opts.InitOpts(width="100px", height="100px"))

    # x轴数据
    line.add_xaxis(xaxis_data=x)

    # y轴数据
    line.add_yaxis(series_name='商家A', y_axis=y1)
    line.add_yaxis(series_name='商家B', y_axis=y2)

    # 设置配置
    line.set_global_opts(title_opts=opts.TitleOpts(title='折线图:商家货物销量', pos_top='50%'))

    # 初始化组合图:Grid
    grid = Grid(init_opts=opts.InitOpts(width='600px', height='400px'))
    # 利用grid_bottom,grid_top,grid_left,grid_right四个参数控制子图的相对位置
    grid.add(bar, grid_opts=opts.GridOpts(pos_right='60%'))
    grid.add(line, grid_opts=opts.GridOpts(pos_left='60%'))
    grid.render('组合图Grid示范图.html')


def plot_pages():
    """
    Pages可以将多张图表按顺序展示在一张网页中，适合制作图形化报表。
    Pages中的图表可以是Grid,Overlap或Timeline.
    使用Pages来绘制组合图
    子图是自己本身的宽高
    :return:html
    """
    # 1.首先绘制一个柱状图
    # 初始化数据来源
    x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋"]
    y1 = [5, 20, 36, 10, 75]
    y2 = [10, 25, 8, 60, 20]

    #  初始化柱状图
    bar = Bar(init_opts=opts.InitOpts(width='600px', height='400px'))

    # x轴数据
    bar.add_xaxis(xaxis_data=x)
    # y轴数据
    bar.add_yaxis(series_name="商家A", y_axis=y1)
    bar.add_yaxis(series_name="商家B", y_axis=y2)

    # 设置配置
    bar.set_global_opts(title_opts=opts.TitleOpts(title='柱状图:商家货物销量'))

    # 2.绘制一个折线图
    # 初始化数据来源
    x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋"]
    y1 = [5, 20, 36, 10, 75]
    y2 = [10, 25, 8, 60, 20]

    # 初始化折线图
    line = Line(init_opts=opts.InitOpts(width="500px", height="200px"))

    # x轴数据
    line.add_xaxis(xaxis_data=x)

    # y轴数据
    line.add_yaxis(series_name='商家A', y_axis=y1)
    line.add_yaxis(series_name='商家B', y_axis=y2)

    # 设置配置
    line.set_global_opts(title_opts=opts.TitleOpts(title='折线图:商家货物销量'))

    # 初始化pages
    pages = Page(page_title='多图', layout=opts.PageLayoutOpts())

    # 添加图形系列
    pages.add(bar, line, line)

    # 输出pages
    pages.render('组合图pages示范图.html')


def plot_timeline():
    """
    Timeline可以将多个图表制作成动画。
    :return:
    """
    # 初始化多组数据
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    year = 5
    start_year = 2018
    num = len(attr)
    # 初始化时间线图形
    timeline = Timeline(init_opts=opts.InitOpts(width='600px', height='400px'))

    # 时间轴添加配置项
    timeline.add_schema(is_auto_play=False, is_loop_play=True, is_timeline_show=True, control_position='right',
                        itemstyle_opts=opts.ItemStyleOpts(color='blue', opacity=0.8),play_interval=1000)

    for i in range(5):
        year_sales1 = [randint(10, 100) for _ in range(num)]
        year_sales2 = [randint(200, 500) for _ in range(num)]
        # 初始化
        bar_temp = Bar(init_opts=opts.InitOpts())
        # 加载数据
        bar_temp.add_xaxis(xaxis_data=attr)
        bar_temp.add_yaxis(series_name=f'{start_year+i}年净销售额',y_axis=year_sales1)
        bar_temp.add_yaxis(series_name=f'{start_year+i}年实际销售额',y_axis=year_sales2)
        # bar配置项
        bar_temp.set_global_opts(title_opts=opts.TitleOpts(title=f'{start_year + i} 销售额情况'))

        # 时间轮播图添加图形
        timeline.add(bar_temp, f'{start_year + i}年营业额')

    # 输出时间线轮播图
    timeline.render('组合图时间线轮播图.html')


if __name__ == '__main__':
    pass
    # 1.使用Grid绘制组合图
    # plot_grid()
    # 2.使用Page绘制组合图
    # plot_pages()
    # 3.绘制时间线轮播多图
    plot_timeline()
