from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from fchart.api.models import DataModel
from fchart.api.chart import Chart

app = FastAPI()

chart = Chart("http://127.0.0.1:8081")

@app.post("/pic")
async def pie(data:DataModel):
    return {"url",chart.pie(data)}

@app.post("/line")
async def line(data:DataModel):
    return {"url",chart.line(data)}

@app.post("/bar")
async def bar(data:DataModel):
    return {"url",chart.bar(data)}

app.add_middleware(CORSMiddleware, allow_origins="*", allow_methods="*",allow_headers=["*"])
playground_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
app.mount("/", StaticFiles(directory=playground_folder_path, html=True), name="chart")

    