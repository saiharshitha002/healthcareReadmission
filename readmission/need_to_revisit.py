import pandas as pd

def get_id(encounter_id):
    df = pd.read_csv("readmission/static/readmission/dataset/diabetic_data.csv")
    df = df[['encounter_id','readmitted']]
    print(df,"hello")
    res = df[df['encounter_id'] == encounter_id]
    print(res['readmitted'])
    return res['readmitted']