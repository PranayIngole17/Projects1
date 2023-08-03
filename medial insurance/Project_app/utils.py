import pickle
import json
import numpy as np
from Project_app import config


class medicalInsurance():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region ='region_'+ region

    def load_model(self):
         
         
         with open(config.MODEL_FILE_PATH,'rb') as f:
              
              self.model = pickle.load(f)
        
         with open(config.JSON_FILE_PATH,'rb') as f:
              
              self.project_data = json.load(f)

    def get_predicted_charges(self):
          self.load_model()
          
          test_array = np.zeros(len(self.project_data['columns']))
          
          test_array[0] = self.age
          test_array[1] = self.project_data["sex"][self.sex]
          test_array[2] = self.bmi
          test_array[3]= self.children
          test_array[4] = self.project_data["smoker"][self.smoker]
            
          test_index = self.project_data["columns"].index(self.region)
          test_array[test_index]=1
          print(f"Test Array :  {test_array}")
          predicted_charges = self.model.predict([test_array])
          print(f"Charges for Medical Insurance are : RS. {round(predicted_charges[0], 2)}")
          return predicted_charges




if __name__ == "__main__":
     
     
     age=19.0
     sex= "female"
     bmi=27.9
     children= 0.0
     smoker="yes"
     region = "southwest"

     med_ins =medicalInsurance(age,sex,bmi,children,smoker,region)
     med_ins.get_predicted_charges()



        