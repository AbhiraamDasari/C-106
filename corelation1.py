import csv
import plotly_express as px
import numpy as np
def getDataSource(data_path):
    size = []
    time = []
    with open(data_path)as f:
        df = csv.DictReader(f)
        for row in df:
            size.append (float(row["Marks In Percentage"]))
            time.append(float(row["Days Present"]))
    return{"x":size,"y":time}

def corelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Corelation is ",correlation[0,1])

def setup():
    data_path = "./Student Marks vs Days Present.csv"
    dataSource = getDataSource(data_path)
    corelation(dataSource)

setup()    