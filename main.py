def sub(*args,**kwargs):
    import pickle
    import sklearn
    loaded_model = pickle.load(open('heart_model.sav', 'rb'))
    result2 = loaded_model.predict([[0,0,0,0,0,0,0,0,0,0,0,0,0]])
    print(result2)
sub()
