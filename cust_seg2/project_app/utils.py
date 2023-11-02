import pickle
import numpy as np
import json
import config


class cust_segmentation():

    def __init__(self,purchases,balance,credit_limit,payments,tenure,oneoff_purchases,installments_purchases,cash_advance,prc_full_payment,cash_advance_frequency,cash_advance_trx,purchases_trx,minimum_payments,balance_frequency,oneoff_purchases_frequency,purchases_installments_frequency):
        self.purchases = purchases
        self.balance = balance
        self.credit_limit = credit_limit
        self.payments = payments
        self.tenure = tenure
        self.oneoff_purchases = oneoff_purchases
        self.installments_purchases = installments_purchases
        self.cash_advance = cash_advance
        self.prc_full_payment = prc_full_payment
        self.cash_advance_frequency = cash_advance_frequency
        self.cash_advance_trx = cash_advance_trx
        self.purchases_trx = purchases_trx
        self.minimum_payments = minimum_payments
        self.balance_frequency = balance_frequency
        self.oneoff_purchases_frequency = oneoff_purchases_frequency
        self.purchases_installments_frequency = purchases_installments_frequency




    def load_model(self):
        with open('project_app\pipeline.pkl','rb') as f:
            self.model1 = pickle.load(f)

        with open('project_app\pipeline.pkl','rb') as f:
            self.model2 = pickle.load(f)    


    def get_predicted(self):
        self.load_model()

        test_array = np.zeros(16)
        test_array[0]= self.purchases
        test_array[1]= self.balance
        test_array[2]= self.credit_limit
        test_array[3]= self.payments
        test_array[4]= self.tenure
        test_array[5]= self.oneoff_purchases
        test_array[6]= self.installments_purchases
        test_array[7]= self.cash_advance
        test_array[8]= self.prc_full_payment
        test_array[9]= self.cash_advance_frequency
        test_array[10]= self.cash_advance_trx
        test_array[11]= self.purchases_trx
        test_array[12]= self.minimum_payments
        test_array[13]= self.balance_frequency
        test_array[14]= self.oneoff_purchases_frequency
        test_array[15]= self.purchases_installments_frequency

        print(test_array)
        prdicted_cluster = self.model1.predict([test_array])[0]
        predicted_cust_default = self.model2.predict([test_array])[0]
        if prdicted_cluster == 0:
            if predicted_cust_default ==0:
                print("The customer belong to Cluster 0 \n 1)the customer has high purchases ,balance , creditlimit ,onoff purchases and cashadvance  \n 2) They should be recommended for the increasing their creditlimit and more offers as they are predicted non defaulted")

            else :
                print("The customer belong to Cluster 0 \n 1)the customer has high purchases ,balance , creditlimit ,onoff purchases and cashadvance  \n 2) They should not be recommended for the increasing their creditlimit as they are predicted  defaulted")
        else :
            if predicted_cust_default ==1:
                print("The customer belong to Cluster 1 \n 1)the customer has Low purchases ,balance , creditlimit ,onoff purchases and cashadvance  \n 2) They should not be recommended for the increasing their creditlimit as they are predicted defaulted")

            else:
                print("The customer belong to Cluster 1 \n 1)the customer has Low purchases ,balance , creditlimit ,onoff purchases and cashadvance  \n 2) They should be recommended for the increasing their balance , creditlimit and more offers as they are predicted non defaulted")
        return prdicted_cluster,predicted_cust_default

        
        







if __name__=="__main__":
    purchases = 0
    balance = 3202.467416
    credit_limit=7000
    payments = 4103
    tenure = 12
    oneoff_purchases = 0
    installments_purchases=0
    cash_advance=6442.94
    prc_full_payment=0.2222
    cash_advance_frequency= 0.25000
    cash_advance_trx = 4
    purchases_trx = 0
    minimum_payments = 1072.340217
    balance_frequency = 0.900
    oneoff_purchases_frequency = 0.0
    purchases_installments_frequency= 0.0

    cust_seg = cust_segmentation(purchases,balance,credit_limit,payments,tenure,oneoff_purchases,installments_purchases,cash_advance,prc_full_payment,cash_advance_frequency,cash_advance_trx,purchases_trx,minimum_payments,balance_frequency,oneoff_purchases_frequency,purchases_installments_frequency)
    cust_seg.get_predicted()
 

    



        