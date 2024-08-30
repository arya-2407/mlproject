import os
import sys
import dill
import pandas as pd 
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)

def evaluate_model(X_train,y_train,X_test,y_test,models,param):
    try:
        report={}
        for i in range(len(list(models))):
            model=list(models.values())[i] #fetch model from models dict
            param_grid=param[list(models.keys())[i]]   

            gs=GridSearchCV(model,param_grid=param_grid,cv=3,n_jobs=-1)#initialize grid search
            gs.fit(X_train,y_train)

            #model.fit(X_train,y_train) #train model

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            y_train_pred=model.predict(X_train) #predict on train data
            y_test_pred=model.predict(X_test) #predict on test data

            train_model_score=r2_score(y_train,y_train_pred) #train performance
            test_model_score=r2_score(y_test,y_test_pred) #test performance

            report[list(models.keys())[i]] = test_model_score #recording test performance 
        return report
    except Exception as e:
        raise CustomException(e,sys)




