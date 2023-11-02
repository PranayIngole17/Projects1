from project_app.utils import cust_segmentation
import config
from flask import Flask,jsonify,request,render_template


app =Flask(__name__)

@app.route('/',methods = ['GET'])
def cust_seg():
    print("welcome to cust_seg_model")
    return render_template('index.html')


@app.route('/prediction',methods = ['GET','POST'])
def get_prediction():
    if request.method == 'POST':
            purchases = request.form["purchases"]
            balance = request.form["balance"]
            credit_limit = request.form["credit_limit"]
            payment = request.form["payment"]
            tenure = request.form["tenure"]
            oneoff_purchases = request.form["oneoff_purchases"]
            installments_purchases = request.form["installments_purchases"]
            cash_advance = request.form["cash_advance"]
            prc_full_payment = request.form["prc_full_payment"]
            cash_advance_frequency = request.form["cash_advance_frequency"]
            cash_advance_trx = request.form["cash_advance_trx"]
            purchases_trx = request.form["purchases_trx"]
            minimum_payment = request.form["minimum_payment"]
            balance_frequency = request.form["balance_frequency"]
            oneoff_purchases_frequency = request.form["oneoff_purchases_frequency"]
            purchases_installments_frequency = request.form["purchases_installments_frequency"]
            print(purchases,balance,credit_limit,payment,tenure,oneoff_purchases,installments_purchases,cash_advance,prc_full_payment,cash_advance_frequency,cash_advance_trx,purchases_trx,minimum_payment,balance_frequency,oneoff_purchases_frequency,purchases_installments_frequency)
            cust_seg = cust_segmentation(purchases,balance,credit_limit,payment,tenure,oneoff_purchases,installments_purchases,cash_advance,prc_full_payment,cash_advance_frequency,cash_advance_trx,purchases_trx,minimum_payment,balance_frequency,oneoff_purchases_frequency,purchases_installments_frequency)
            result = cust_seg.get_predicted()
            print(f"the result {result}")
            if result[0]  == 0:
                 
                 if result[1] ==0:

                        return jsonify({"Result":"The customer belong to Cluster 0 ,1)the customer has high purchases ,balance , creditlimit ,onoff purchases and cashadvance , 2) They should be recommended for the increasing their creditlimit and more offers as they are predicted non defaulted"})

                 else :

                    return jsonify({"Result":"The customer belong to Cluster 0  1)the customer has high purchases ,balance , creditlimit ,onoff purchases and cashadvance  , 2) They should not be recommended for the increasing their creditlimit as they are predicted  defaulted"})
            else :
                if result[1] ==1:
                    return jsonify({"Result":"The customer belong to Cluster 1 , 1)the customer has Low purchases ,balance , creditlimit ,onoff purchases and cashadvance  , 2) They should not be recommended for the increasing their creditlimit as they are predicted defaulted"})

                else:

                   return jsonify({"Result":"The customer belong to Cluster 1 , 1)the customer has Low purchases ,balance , creditlimit ,onoff purchases and cashadvance  , 2) They should be recommended for the increasing their creditlimit and more offers as they are predicted non defaulted"})
    
    else:
            purchases1 = float(request.form["purchases"])
            balance1 = float(request.form["balance"])
            credit_limit1 = float(request.form["credit_limit"])
            payment1 = float(request.form["payment"])
            tenure1 = float(request.form["tenure"])
            oneoff_purchases1 = float(request.form["oneoff_purchases"])
            installments_purchases1 = float(request.form["installments_purchases"])
            cash_advance1 = float(request.form["cash_advance"])
            prc_full_payment1 = float(request.form["prc_full_payment"])
            cash_advance_frequency1 = float(request.form["cash_advance_frequency"])
            cash_advance_trx1 = float(request.form["cash_advance_trx"])
            purchases_trx1 = float(request.form["purchases_trx"])
            minimum_payment1 = float(request.form["minimum_payment"])
            balance_frequency1 = float(request.form["balance_frequency"])
            oneoff_purchases_frequency1 = float(request.form["oneoff_purchases_frequency"])
            purchases_installments_frequency1 = float(request.form["purchases_installments_frequency"])
            print(purchases1,balance1,credit_limit1,payment1,tenure1,oneoff_purchases1,installments_purchases1,cash_advance1,prc_full_payment1,cash_advance_frequency1,cash_advance_trx1,purchases_trx1,minimum_payment1,balance_frequency1,oneoff_purchases_frequency1,purchases_installments_frequency1)
            cust_seg1 = cust_segmentation(purchases1,balance1,credit_limit1,payment1,tenure1,oneoff_purchases1,installments_purchases1,cash_advance1,prc_full_payment1,cash_advance_frequency1,cash_advance_trx1,purchases_trx1,minimum_payment1,balance_frequency1,oneoff_purchases_frequency1,purchases_installments_frequency1)
            result1 = cust_seg1.get_predicted()
            print(f"the result {result1}")
            if result1[0]  == 0:
                 if result1[1] ==0:
                      return jsonify({"Result":"The customer belong to Cluster 0 \n 1)the customer has high purchases ,balance , creditlimit ,onoff purchases and cashadvance  \n 2) They should be recommended for the increasing their creditlimit and more offers as they are predicted non defaulted"})
                 else :

                    return jsonify({"Result":"The customer belong to Cluster 0 \n 1)the customer has high purchases ,balance , creditlimit ,onoff purchases and cashadvance  \n 2) They should not be recommended for the increasing their creditlimit as they are predicted  defaulted"})
            else :
                if result1[1] ==1:
                    return jsonify({"Result":"The customer belong to Cluster 1 \n 1)the customer has Low purchases ,balance , creditlimit ,onoff purchases and cashadvance  \n 2) They should not be recommended for the increasing their creditlimit as they are predicted defaulted"})

                else:

                   return jsonify({"Result":"The customer belong to Cluster 1 \n 1)the customer has Low purchases ,balance , creditlimit ,onoff purchases and cashadvance  \n 2) They should not be recommended for the increasing their creditlimit as they are predicted non defaulted"})
                 

                      


         








if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=config.PORT_NUM)
