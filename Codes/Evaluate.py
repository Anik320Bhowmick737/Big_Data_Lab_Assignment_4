from sklearn.metrics import r2_score
import pandas as pd
import yaml
import json
import os

def Evaluate(name_csv):
    input_path = "/Users/anikbhowmick/Python/Big_Data_Assignment/A03/Input_path/"+name_csv+"_inp.csv"
    target_path = "/Users/anikbhowmick/Python/Big_Data_Assignment/A03/Ground_truth/"+name_csv+"_GT.csv"
    Data_x = pd.read_csv(input_path)
    Data_y = pd.read_csv(target_path)

    cols_x = Data_x.columns[1:]
    cols_y = Data_y.columns[1:]
    #print(cols_x)
    #print(cols_y)

    if(len(Data_x)<len(Data_y)):
        missing_date = [i+1 for i in range(12) if i+1 not in list(Data_x['DATE'])]
        Data_y = Data_y[~Data_y['DATE'].isin(missing_date)]
    
    elif(len(Data_x)>len(Data_y)):
        missing_date = [i+1 for i in range(12) if i+1 not in list(Data_y['DATE'])]
        Data_x = Data_x[~Data_x['DATE'].isin(missing_date)]


    print(f"\n\n The R2_score of the csv id : {name_csv} is\n\n")
    r2_scores = {}
    for i in range(min(len(cols_x),len(cols_y))):
        x = Data_x[cols_x[i]].values
        y = Data_y[cols_y[i]].values
        
        r2_scores[cols_x[i]] =r2_score(y,x)
        print(f"For column {cols_x[i]}\n\n")
        print(f"{r2_score(y,x):.5f}")
        print("**********\n\n")
    
    X=Data_x.values
    Y=Data_y.values
    print("Weighted R2 score:\n\n")
    print(f"{r2_score(y,x,multioutput='variance_weighted'):.5f}\n\n")
    r2_scores['Weighted R2 score']=r2_score(y,x,multioutput='variance_weighted')
    out_dir = "/Users/anikbhowmick/Python/Big_Data_Assignment/A03/final_result_json"
    with open(os.path.join(out_dir,f"{name_csv}_r2_scores.json"), "w") as f:
        json.dump({name_csv: r2_scores}, f, indent=4)

if __name__ == "__main__":
    params = yaml.safe_load(open("params.yaml"))["Evaluate"]
    name_csv = params["name_csv"]
    Evaluate(name_csv)


 

