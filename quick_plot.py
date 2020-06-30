# -*- coding: utf-8 -*-
"""
Proj: pyecharts
Created on:   2020/6/29 18:15
@Author: RAMSEY

"""

import pandas as pd
from pyecharts.charts.basic_charts.bar import Bar
from pyecharts.charts.basic_charts.line import Line
from pyecharts.charts.basic_charts.boxplot import Boxplot
from pyecharts.charts.basic_charts.geo import Geo
from pyecharts.charts.basic_charts.map import Map
from pyecharts.charts.basic_charts.pie import Pie
from pyecharts.charts.basic_charts.wordcloud import WordCloud
from pyecharts.charts.basic_charts.scatter import Scatter
from pyecharts import options as opts

"""
快速了解pyecharts中的一些基本图形
1.柱状图:Bar
2.折线图:Line
3.绘制散点图:scatter
4.绘制箱线图:boxplot
5.绘制词云:wordcloud
6.绘制地理地图
    6.城市:Geo
    7.国家:Map
    pyecharts中Geo表达和城市关联的数据,Map表达和国家和省份关联的数据。
8.绘制饼图
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

    # 图形配置项
    scatter.set_global_opts(
        # 标题
        title_opts=opts.TitleOpts(title='不同性别身高体重分布'),
        # x轴
        xaxis_opts=opts.AxisOpts(
            name='体重', name_location='end', min_=40, max_=90, max_interval=10, name_gap=25
        ),
        # y轴
        yaxis_opts=opts.AxisOpts(
            name='身高', name_location='end', min_=150, max_=180, max_interval=5, name_gap=25
        ),
        # 视觉映射配置项
        visualmap_opts=opts.VisualMapOpts(
            # 颜色映射
            # type_="color",
            # 大小映射
            type_='size',
            max_=145,
            min_=185,
            dimension=1  ## 组件映射维度
        )
    )
    # 绘制散点图
    scatter.render('散点图示范.html')


def plot_boxplot():
    """
    绘制箱线图
    :return: html
    """
    # 加载数据
    x = ['1班', '2班', '3班', '4班']
    y1 = [78, 98, 56, 78, 90.0, 45, 78, 20, 87, 86, 74, 89, 94]
    y2 = [89, 82, 45, 67, 68, 78.0, 79, 98, 71, 56, 78, 81, 80]
    y3 = [90, 80, 60, 89, 76, 73.0, 72, 92, 89, 87, 65, 66, 76]
    y4 = [82, 72, 55, 100, 90.0, 78, 69, 67, 87, 66, 78, 71, 82]

    # 初始化箱线图
    box = Boxplot(init_opts=opts.InitOpts(width='600px', height='420px'))

    # 添加数据
    #
    y_data = box.prepare_data([y1, y2, y3, y4])
    box.add_xaxis(xaxis_data=x)
    box.add_yaxis(series_name='各班成绩分布', y_axis=y_data)

    # 绘制箱线图
    box.render('箱线图示范.html')


def plot_wordcloud():
    """
    绘制词云
    :return:
    """
    # 加载原始数据
    words = ['python', 'jupyter', 'numpy', 'pandas', 'matplotlib', 'sklearn',
             'xgboost', 'lightGBM', 'simpy', 'keras', 'tensorflow',
             'hive', 'hadoop', 'spark']

    counts = [100, 90, 65, 95, 50, 60, 70, 70, 20, 70, 80, 80, 60, 60]
    data_sequence = [(word, count) for word, count in zip(words, counts)]

    # 初始化词云
    wordclouds = WordCloud(init_opts=opts.InitOpts(width='600px', height='420px'))

    # 添加数据源
    wordclouds.add(series_name='数据算法常用工具', data_pair=data_sequence, word_size_range=[4, 20], shape='star')

    # 配置设置
    wordclouds.set_global_opts(
        title_opts=opts.TitleOpts(title='数据算法常用工具'),

    )

    # 绘制词云
    wordclouds.render('词云示范图.html')


def plot_geo_city():
    """
    绘制地理地图:
        pyecharts中Geo表达和城市关联的数据,Map表达和国家和省份关联的数据。
    :return: html
    """
    # 加载数据
    data = [
        ("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15),
        ("惠州", 37), ("江阴", 37), ("蓬莱", 37), ("韶关", 38), ("嘉峪关", 38), ("广州", 38),
        ("张家港", 52), ("三门峡", 53), ("锦州", 54), ("南昌", 54), ("柳州", 54), ("三亚", 54),
        ("呼和浩特", 58), ("成都", 58), ("大同", 58), ("镇江", 59), ("桂林", 59), ("张家界", 59),
        ("北京", 79), ("徐州", 79), ("衡水", 80), ("包头", 80), ("绵阳", 80), ("乌鲁木齐", 84),
        ("菏泽", 194), ("合肥", 229), ("武汉", 273), ("大庆", 279)]

    # 初始化地图
    geo = Geo(init_opts=opts.InitOpts())

    # 初始化地图类型
    geo.add_schema(maptype='china')

    # 加载数据
    geo.add(series_name='全国省会城市', data_pair=data)
    #
    # 配置
    geo.set_global_opts(
        title_opts=opts.TitleOpts(title='全国主要城市'),
        # 视觉配置
        visualmap_opts=opts.VisualMapOpts(
            type_='color',
            min_=0,
            max_=300,
        ),
    )

    # 保存地图成html
    geo.render('地图示范图.html')


def plot_geo_country():
    """
    绘制地理地图:
        pyecharts中Geo表达和城市关联的数据,Map表达和国家和省份关联的数据。
    :return: html
    """
    # 加载数据
    countries = ["China", "Canada", "India", "Russia", "United States", "Japan"]
    capita_gdp = [13334, 43294, 5903, 23038, 53354, 36162]
    gdp_sequence = [(country, gdp) for country, gdp in zip(countries, capita_gdp)]

    # 初始化地图
    map = Map(init_opts=opts.InitOpts())

    # 加载数据:其中maptype可以初始化地图类型,而geo中需要单独设置
    map.add(series_name='人均gdp', data_pair=gdp_sequence, maptype='world', label_opts=opts.LabelOpts(is_show=False))

    # 配置
    map.set_global_opts(
        title_opts=opts.TitleOpts(title='全球主要国家gdp'),
        # 视觉配置
        visualmap_opts=opts.VisualMapOpts(
            type_='color',
            min_=50000,
            max_=5000,
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True)
    )

    # 保存地图成html
    map.render('世界地图示范图.html')


def plot_pie():
    """
    绘制饼图
    :return:
    """
    # 加载数据
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    values = [11, 12, 13, 10, 10, 10]
    data_sequence = [(name,value) for name,value in zip(attr,values)]

    # 初始化饼图
    pie = Pie(init_opts=opts.InitOpts(width='400px',height='400px'))

    # 添加数据
    pie.add(series_name='销售比例',data_pair=data_sequence,label_opts=opts.LabelOpts(is_show=True))



    pie.render('饼图示范图.html')

if __name__ == '__main__':
    pass
    # 1.绘制柱状图
    # plot_bar()
    # 2.绘制折线图
    # plot_line()
    # 3.绘制散点图
    # plot_scatter()
    # 4.绘制箱线图
    # plot_boxplot()
    # 5.绘制词云
    # plot_wordcloud()
    # 6.绘制城市地图
    # plot_geo_city()
    # 7.绘制世界地图
    # plot_geo_country()
    # 8.绘制饼图
    plot_pie()
