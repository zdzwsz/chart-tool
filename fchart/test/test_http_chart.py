import requests

xdata = "2020,2021,2022,2023"
ydata = "162269,231971,292376,341923;146054,179767,228827,280567"
title = "南方软件园与清华科技园能耗对比"
ydata_group = ydata.split(";")
y = {}
i=0
for yd in ydata_group :
    y["y" + str(i)]=yd.split(",")
    i += 1
x = {"x":xdata.split(",")}
if title is None:
    title = "Data Chart"
payload = {"title": title, "y": y,"x":x}
url = "http://127.0.0.1:8081/" + "bar"
print("payload:",payload)
response = requests.post(url, json=payload)
# 检查请求是否成功
if response.status_code == 200:
    # 获取响应内容（假设是JSON格式）
    print(response.json())
else:
    print({"error" : response.status_code })