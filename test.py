import urllib.request




def download_data():
    try:
        res = urllib.request.urlretrieve("https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=7F6BE616-8CE6-449E-8620-5F627C22AA0D", "dataset.csv")
        return res
    except Exception as e:
        print(e)
        return False


import pandas as pd

def get_data():
    data = pd.read_csv('dataset.csv')
    return data
    
df = get_data()
dataset = df.values.tolist()
print(dataset[0])