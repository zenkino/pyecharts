from echarts.base import Base

class Radar(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def config(self, indicator, shape="", rader_text_color="#000", **kwargs):
        _indicator = []
        for indi in indicator:
            _name, _max = indi
            _indicator.append({"name": _name, "max": _max})
        self._option.update(
            radar={"indicator": _indicator,
                   "shape": shape,
                   "name": {"textStyle": {"color": rader_text_color}},
                   "splitLine": self.Option.split_line(**kwargs),
                   "splitArea": self.Option.split_area(**kwargs),
                   "axisLine": self.Option.axis_line(**kwargs)}
        )

    def add(self, *args, **kwargs):
        self._add(*args, **kwargs)

    def _add(self, name, value, **kwargs):
        self._option.get('legend').get('data').append(name)
        self._option.get('series').append({
            "type": "radar",
            "name": name,
            "data": value,
            "symbol": self.Option.symbol(**kwargs),
            "lineStyle": self.Option.line_style(**kwargs),
            "areaStyle": {"normal": self.Option.area_style(flag=True, **kwargs)}
        })
        self._option.get('legend').update(self.Option.legend(**kwargs))
        self._option.update(color=self.Option.color(self._colorlst, **kwargs))


r = [("销售", 6500),
     ("管理", 16000),
     ("信息技术", 30000),
     ("客服", 38000),
     ("研发", 52000),
     ("市场", 25000)]

v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]

if __name__ == "__main__":

    radar = Radar()
    radar.config(r)
    radar.add("预算分配", v1, label_color=["#000"])
    # radar.add("实际开销", v2, label_color=["#4e79a7"])
    radar.render()
    radar.show_config()