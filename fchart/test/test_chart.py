from fchart.api.chart import Chart
from fchart.api.models import DataModel


data = DataModel(
    title="公司营业表",
    y = {"营业额":[100,201,103,423,588,699],"纳税":[10,21,13,43,58,69],"利润":[13,22,17,53,68,79]},
    x = {"年度":["2021","2022","2023","2024","2025","2026"]}
)

data1 = DataModel(
    title="test a plt",
    y = {"output value":[100,201,103,423,588,699]},
    x = {"annual":["2021","2022","2023","2024","2025","2026"]}
)
jsondata = {'title': '南方软件园与清华科技园能耗对比', 'y': {'y0': ['162269', '231971', '292376', '341923'], 'y1': ['146054', '179767', '228827', '280567']}, 'x': {'x': ['2020', '2021', '2022', '2023']}}
data3 = DataModel(**jsondata)
char = Chart("http://127.0.0.1:8081")
#print(char.pie(data1))
#print(char.line(data1))
print(char.bar(data3))




