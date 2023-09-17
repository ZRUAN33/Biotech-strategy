from dash import Dash, dcc, html, Input, Output
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import plotly.io as pio

df = pd.read_csv('.\SGEN candlestickV3.csv')
fig = make_subplots(rows=3, cols=1, subplot_titles=("Chart 1day", "Volume proportion", "Chart 1min"),
                    vertical_spacing=0.1, shared_xaxes=True,
                    specs=[[{"secondary_y": True}],
                           [{"secondary_y": False}],
                           [{"secondary_y": True}]])  # 控制三张图是否用同一个横轴shared_xaxes=True
# 调整上下两个subplot的高度比
# row_heights = [0.7, 0.3]
# 画1day蜡烛图
candlestick_trace_1day = go.Candlestick(x=df['date'],
                                        open=df['open_1day'],
                                        high=df['high_1day'],
                                        low=df['low_1day'],
                                        close=df['close_1day'],
                                        name="Candlestick 1day")
fig.add_trace(candlestick_trace_1day, row=1, col=1, secondary_y=False)

# 画1day折线图
bar_1day = go.Bar(x=df["date"], y=df["turnover_1day"], name="turnover 1day")
fig.add_trace(bar_1day, row=1, col=1, secondary_y=True)
# 如果要把柱状图换成折线图，则换成代码line_trace_1day = go.Scatter(x=df["date"], y=df["turnover_1day"], name="turnover 1day")

# 画1min蜡烛图
candlestick_trace_1min = go.Candlestick(x=df['date'],
                                        open=df['open_1min'],
                                        high=df['high_1min'],
                                        low=df['low_1min'],
                                        close=df['close_1min'],
                                        name="Candlestick 1min")
fig.add_trace(candlestick_trace_1min, row=3, col=1, secondary_y=False)

# 添加折线图到第二个子图
bar_1min = go.Bar(x=df["date"], y=df["turnover_1min"], name="turnover 1min")
fig.add_trace(bar_1min, row=3, col=1, secondary_y=True)

# 画中间的一个柱状图，显示每日最后一分钟的交易量占一天的占比
bar_proportion = go.Bar(x=df["date"], y=df["volume_proportion"], name="volume_proportion")
fig.add_trace(bar_proportion, row=2, col=1, secondary_y=False)

# # 调整图的布局和大小
# fig.update_layout(
#     height=800,
#     width=1200,
# )

fig.update_xaxes(rangeslider=dict(visible=False), row=1, col=1)
fig.update_xaxes(rangeslider=dict(visible=False), row=2, col=1)
fig.update_xaxes(rangeslider=dict(visible=False), row=3, col=1)
pio.write_html(fig, file='Candlestick Chart with Lines.html', auto_open=False)
