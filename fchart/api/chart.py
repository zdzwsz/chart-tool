from fchart.api.models import DataModel
import matplotlib.pyplot as plt
import numpy as np
from uuid import uuid4

plt.rcParams['font.family'] = ['AR PL UKai CN']

layout = {
    1:[1,1],
    2:[1,2],
    3:[1,3],
    4:[2,3],
    5:[2,3],
    6:[2,3],
    7:[2,4],
    8:[2,4],
    9:[3,3],
    10:[3,4]
}



class Chart():
    def __init__(self,uri, folder = "fchart/static") -> None:
        self.uri = uri
        self.folder = folder

    def pie(self,data:DataModel):
        name = uuid4().hex + ".png"
        for key, value in data.x.items():
            xlabel = key
            xdata = value
        ydata = []
        ylabel = []
        if isinstance(data.y,list) : #list
            for d in data.y:
                for key, value in d.items():
                    ylabel.append(key)
                    ydata.append(value) 
        else: #dict
            for key, value in data.y.items():
                ylabel.append(key)
                ydata.append(value)
        l = layout.get(len(ydata))
        i = 1
        for y in ydata:
            plt.subplot(l[0],l[1],i)
            plt.pie(y, labels=xdata)
            plt.title(ylabel[i-1])
            i += 1
        plt.savefig(self.folder + "/" + name)
        plt.close()
        return self.uri + "/" + name
    
    def line(self,data:DataModel):
        name = uuid4().hex + ".png"
        for key, value in data.x.items():
            xlabel = key
            xdata = value
        ydata = []
        ylabel = []
        if isinstance(data.y,list) : #list
            for d in data.y:
                for key, value in d.items():
                    ylabel.append(key)
                    ydata.append(value) 
        else: #dict
            for key, value in data.y.items():
                ylabel.append(key)
                ydata.append(value)
        for i,y in enumerate(ydata):
            plt.plot(xdata, y, label= ylabel[i])

        plt.title(data.title)
        plt.legend()
        plt.savefig(self.folder + "/" + name)
        plt.close()
        return self.uri + "/" + name
    
    def bar(self,data:DataModel):
        bar_width=0.6/len(data.y)
        name = uuid4().hex + ".png"
        for key, value in data.x.items():
            xlabel = key
            xdata = value
        ydata = []
        ylabel = []
        if isinstance(data.y,list) : #list
            for d in data.y:
                for key, value in d.items():
                    ylabel.append(key)
                    ydata.append(value) 
        else: #dict
            for key, value in data.y.items():
                ylabel.append(key)
                ydata.append(value)
        index= np.arange(len(xdata))
        for i,y in enumerate(ydata):
            plt.bar( index + bar_width * i , y, bar_width, label= ylabel[i])
        #plt.bar(data.x, data.y)
        plt.xticks(index + bar_width / 2 * (len(data.y)-1), xdata)
        plt.title(data.title)
        plt.legend()
        plt.savefig(self.folder + "/" + name)
        plt.close()
        return self.uri + "/" + name