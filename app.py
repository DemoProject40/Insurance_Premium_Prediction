from flask import Flask, render_template, request
from src.pipeline.prediction_pipeline import Custom_Data, Predict_Pileline


app = Flask(__name__)


@app.route('/')
def home_page():
	return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def predict_datapoint():
	if request.method == 'GET':
		return render_template('form.html')

	else:
		data = Custom_Data(
			age = request.form.get('age'),
			sex = request.form.get('sex'),
			bmi = float(request.form.get('bmi')),
			children = request.form.get('children'),
			smoker = request.form.get('smoker'),
			region = request.form.get('region')
		)
		
		final_df = data.get_data_as_dataframe()
		predict_pipeline = Predict_Pileline()
		pred = predict_pipeline.predicts(final_df)

		results = round(pred[0],3)

		return render_template('result.html',final_result = results)

		

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
