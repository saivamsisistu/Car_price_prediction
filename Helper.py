import pickle
with open('LinearRegressionModel.pkl','rb') as f:
    model=pickle.load(f)
    print(model)