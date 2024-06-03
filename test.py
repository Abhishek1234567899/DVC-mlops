import pandas as pd

Data=[
    {"name": "abhi","age":22,"city":"bhopal"}
    {"name": "vashu","age":20,"city":"bhopal"}
    {"name": "dheeraj","age":26,"city":"bengaluru"}
    {"name": "pradeep","age":22,"city":"bombay "}
    
]
Data=pd.DataFrame(Data)

Data.to_csv("data/data.csv",index=False)