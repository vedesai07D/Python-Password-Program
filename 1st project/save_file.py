import pandas as pd

def save(name, password):

    pas = pd.DataFrame({
        "Name": [name],
        "Password": [password]
    })

    pas.to_csv("details.csv", index = False, header = False, mode = 'a')
    # r=read only, w=overwrite, a=continue write

def opn(name, password):

    pas = pd.read_csv("details.csv")

    if ((pas["Name"] == name) & (pas["Password"] == password)).any():
        print("Details....")
    else:
        print("Invalid login")