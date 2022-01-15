import csv
import plotly_express as px
import numpy as np
def getDataSource(data_path):
    size = []
    time = []
    with open(data_path)as f:
        df = csv.DictReader(f)
        for row in df:
            size.append (float(row["Size of TV"]))
            time.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return{"x":size,"y":time}

def corelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])

    print("Corelation is ",correlation[0,1])

def setup():
    data_path = "./SizeofTv.csv"
    dataSource = getDataSource(data_path)
    corelation(dataSource)

setup()    


    