from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html', pmprediction=0, ebprediction=0, pmhigher=0, ebhigher=0)

@app.route('/reSale', methods=['POST'])
def get_price():
    if request.method=='POST':
        result=request.form
        brand = result['brand']
        category = result['category']
        condition = result['condition']

        pmpkl_file = open('catpm', 'rb')
        pmindex_dict = pickle.load(pmpkl_file)
        pmcat_vector = np.zeros(len(pmindex_dict))

        ebpkl_file = open('cateb', 'rb')
        ebindex_dict = pickle.load(ebpkl_file)
        ebcat_vector = np.zeros(len(ebindex_dict))

        try:
            pmcat_vector[pmindex_dict['brand_'+str(brand)]] = 1
        except:
            pass
        try:
            pmcat_vector[pmindex_dict['condition_'+str(condition)]] = 1
        except:
            pass
        try:
            pmcat_vector[pmindex_dict['category_'+str(category)]] = 1
        except:
            pass
        try:
            pmcat_vector[pmindex_dict['site_'+str(site)]] = 1
        except:
            pass

        try:
            ebcat_vector[ebindex_dict['brand_'+str(brand)]] = 1
        except:
            pass
        try:
            ebcat_vector[ebindex_dict['condition_'+str(condition)]] = 1
        except:
            pass
        try:
            ebcat_vector[ebindex_dict['category_'+str(category)]] = 1
        except:
            pass

        pmpkl_file = open('pmmodel.pkl', 'rb')
        pmmodel = pickle.load(pmpkl_file)
        pmprediction = pmmodel.predict(pmcat_vector.reshape(1, -1))
	
        for sale in pmprediction:
            if sale < 15:
                pmprediction = sale - 2.95
            if sale > 15:
                pmprediction = sale*0.8
        
        ebpkl_file = open('ebmodel.pkl', 'rb')
        ebmodel = pickle.load(ebpkl_file)
        ebprediction = ebmodel.predict(ebcat_vector.reshape(1, -1))

        for sale in ebprediction:
            if sale < 50:
                ebprediction = sale*0.9125
            if sale > 50:
                ebprediction = sale*0.9125 - sale*0.04
        
        pmhigher = ((pmprediction/ebprediction)*100) - 100
        ebhigher = ((ebprediction/pmprediction)*100) - 100

        return render_template('landing.html', pmprediction=int(pmprediction), ebprediction=int(ebprediction), pmhigher=int(pmhigher), ebhigher=int(ebhigher))


if __name__ == '__main__':
	app.debug = True
	app.run()
