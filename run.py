import math
import json
import os
import numpy as np
import pandas as pd
from model import VideoModel
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/predict', methods=['POST'])
def predict_youtube_video():
	if not request.json:
		abort(400)

	data = request.json
	data = data['data']
	model = VideoModel()
	train_df = model.get_data('video_train.csv')
	model.train_model(train_df)

	predicted = model.predict(data)
	return predicted.to_json(orient ='records') 
		
def create_save_dir():
	save_dir = 'save_model'
	if not os.path.exists(save_dir):
		os.makedirs(save_dir)

if __name__ == '__main__':
	create_save_dir()
	app.run(debug = True) 

