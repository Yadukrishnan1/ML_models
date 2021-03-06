import pandas as pd
from sklearn import model_selection

if name == "__main__":
    df = pd.read_csv("input/train.csv")
    df["kfold"] = -1
    
    df = df.sample(frac=1).reset_index(drop=True)
    
    kf = model_selection.StartifiedKFold(n_splits=5, shuffle=False, random_state=42)
    
    for fold, (train_idx, val_idx) in enumerate(kf.split(X=df, y=df.target.values)):
        print((len(train_idx), len(val_idx)))
        df.loc[val_idx, 'kfold'] = fold
        
        
    df.to_csv("input/train_fold.csv", index=False)
