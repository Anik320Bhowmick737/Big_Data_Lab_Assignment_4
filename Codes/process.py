import pandas as pd
import yaml
import os


def process(path):
    os.mkdir("/Users/anikbhowmick/Python/Big_Data_Assignment/A03/Input_path")
    input_path = "/Users/anikbhowmick/Python/Big_Data_Assignment/A03/Input_path/"
    cols_to_keep = ['DATE','DailyMinimumDryBulbTemperature','DailyDepartureFromNormalAverageTemperature','DailyAverageDryBulbTemperature','DailyMaximumDryBulbTemperature']

    csv_files = os.listdir(path)

    for file in csv_files:
        complete_path = os.path.join(path,file)
        Data = pd.read_csv(complete_path)
        Data = Data.assign(DATE=Data['DATE'].str[5:7])[cols_to_keep].dropna()
        Data = Data.groupby('DATE').mean(numeric_only=True)
        if(len(Data)>10):
            Data.to_csv(os.path.join(input_path,f'{file[:-4]}_inp.csv'))
    
if __name__ == "__main__":
    params = yaml.safe_load(open("params.yaml"))["process"]
    path = params["path"]
    process(path)


