from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/reSale',methods=['POST','GET'])
def get_price():
    if request.method=='POST':
        result=request.form
        brand = result['Brand']
        category = result['Category']
        condition = result['Condition']
        site = result['Site']

        pkl_file = open('cat', 'rb')
        index_dict = pickle.load(pkl_file)
        cat_vector = np.zeros(len(index_dict))

        try:
            cat_vector[index_dict['Brand_'+str(brand)]] = 1
        except:
            pass
        try:
            cat_vector[index_dict['Condition_'+str(condition)]] = 1
        except:
            pass
        try:
            cat_vector[index_dict['Category_'+str(category)]] = 1
        except:
            pass
        try:
            cat_vector[index_dict['Site_'+str(site)]] = 1
        except:
            pass

        pkl_file = open('model.pkl', 'rb')
        logmodel = pickle.load(pkl_file)
        prediction = logmodel.predict(cat_vector.reshape(1, -1))
        
        return render_template('result.html',prediction=prediction)


if __name__ == '__main__':
	app.debug = True
	app.run()
