def display(data):
	print("[Server]: " + data)
	
display("Attempting to initialize the server...")

from time import sleep
from flask import Flask, request, send_file
from tensorflow.keras.models import Sequential
import logging
import numpy as np
from six import BytesIO
from PIL import Image, ImageDraw, ImageFont
from IPytho.display import display, Javascript
from Ipython.display import Image as IPyImage

import glob

from object_detection.utils import visualization_utils as viz_utils
from object_detection.utils import colab_utils

import matplotlib
import matplotlib.pyplot as plt
import tensorflow as tf

#%matplotlib inline
#from document_scanner import scan

HOST = 'localhost'
PORT = 5000

try:
	app = Flask(__name__)
except Exception as e:
	display("Failed to launch server, terminating process...")
	print(e)
	exit()
display("Successfully launched server")

dev_key = "secretkey"

#Create/Post
@app.route("/create/<entry_name>", methods = ['POST'])
def handle_create(model_name):
	message = 'invalid key: 403'
	key_create = request.form['key']
	if key_create == dev_key:
		#importing model
		model = Sequential()
		for layer in model_name.layers:
			model.add(layer)
	message = 'model created: 200'
	return {'msg': message}


def get_model():
	# Create a simple model.
	inputs = keras.Input(shape=(32,))
	outputs = keras.layers.Dense(1)(inputs)
	model = keras.Model(inputs, outputs)
	model.compile(optimizer="adam", loss="mean_squared_error")
	return model



class CustomLayer(keras.layers.Layer):
	def __init__(self, a):
		self.var = tf.Variable(a, name="var_a")


layer = CustomLayer(5)
layer_ckpt = tf.train.Checkpoint(layer=layer).save("custom_layer")

ckpt_reader = tf.train.load_checkpoint(layer_ckpt)

ckpt_reader.get_variable_to_dtype_map()



#Read/Get
@app.route("/read/inf/<entry_name>", methods = ['POST'])
def handle_read_inference(model_name = get_model()):
	model = Sequential()
	for layer in model_name.layers:
  		model.add(layer)
	model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])
	model.fit(train_images, train_labels, epochs=10)
	test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
	print('\nTest accuracy:', test_acc)
	predictions = probability_model.predict(test_images)
	predictions[0]
	print('\nTest accuracy:', test_acc)
	i = 0
	plt.figure(figsize=(6,3))
	plt.subplot(1,2,1)
	plot_image(i, predictions[i], test_labels, test_images)
	plt.subplot(1,2,2)
	plot_value_array(i, predictions[i], test_labels)
	plt.show()

def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

@app.route("/read/batch_inf/<entry_name>", methods = ['POST'])
def handle_batch_inference(model_name, lImages):
	for i in range(lImages):
		plt.subplot(lImages, 1, 2*i+1)
		plot_image(i, predictions[i], test_labels, test_images)
		plt.subplot(lImages, 1, 2*i+2)
		plot_value_array(i, predictions[i], test_labels)
		#add probabilities
		#add bounding box
		#add add item classification
		#add trash classification
	plt.tight_layout()
	plt.show()

	return {'Probabilities': 'model created', 'error_message': None, }, 200
	

@app.route("/read/list/<entry_name>", methods = ['GET'])
def handle_usable_models(code: list, models: list, X_train: np.array, X_test: np.array, X: pd.DataFrame):
	for model in models:  # or for i in range(0, len(models)):
		y_score = model.fit(X_train, y_train).decision_function(X_test)
        # or y_score = models[i].fit(X_train, y_train).decision_function(X_test)
		fpr, tpr, _ = roc_curve(y_test, y_score)
		roc_auc = auc(fpr, tpr)
        
        # Traditional Scores
		y_pred = pd.DataFrame(model[i].predict(X_train)).reset_index(drop=True)
		Recall_Train,Precision_Train, Accuracy_Train  = recall_score(y_train, y_pred), precision_score(y_train, y_pred), accuracy_score(y_train, y_pred)
		y_pred = pd.DataFrame(model[i].predict(X_test)).reset_index(drop=True)
		Recall_Test = recall_score(y_test, y_pred)
		Precision_Test = precision_score(y_test, y_pred)
		Accuracy_Test = accuracy_score(y_test, y_pred)

		for i in range(len(tuples)):
			results['Model_'+code[i]] = [roc_auc, Accuracy_Train, Precision_Train, Recall_Train, Accuracy_Test, 
                            Precision_Test, Recall_Test]
	return results
	#return {'msg': 'model list'}, 200
	

@app.route("/read/download/<entry_name>", methods = ['GET'])
def handle_download_models(model_name):
	#TODO: Implement output

	field = None
	try:
		field = model_name._meta.get_field(field)
	except FieldDoesNotExist:
		return 'Error: Model does not exist'
		pass

	if field:
		y_score = model_name.fit(model_name.X_train, model_name.y_train).decision_function(model_name.X_test)
        # or y_score = models[i].fit(X_train, y_train).decision_function(X_test)
		fpr, tpr, _ = roc_curve(model_name.y_test, y_score)
		roc_auc = auc(fpr, tpr)
        
        # Traditional Scores
		y_pred = pd.DataFrame(model_name[i].predict(model_name.X_train)).reset_index(drop=True)
		Recall_Train,Precision_Train, Accuracy_Train  = recall_score(model_name.y_train, y_pred), precision_score(y_train, y_pred), accuracy_score(y_train, y_pred)
		y_pred = pd.DataFrame(model_name[i].predict(model_name.X_test)).reset_index(drop=True)
		Recall_Test = recall_score(model_name.y_test, y_pred)
		Precision_Test = precision_score(model_name.y_test, y_pred)
		Accuracy_Test = accuracy_score(model_name.y_test, y_pred)

	results['Model_'+ code[i]] = [roc_auc, Accuracy_Train, Precision_Train, Recall_Train, Accuracy_Test, 
                            Precision_Test, Recall_Test]
	return results

#Update/Put
@app.route("/update/<model_name>", methods = ['PUT'])
def update_model(model_name, new_model):
	key = request.form['key']
	if key == dev_key:
		for i in len(model_name.layers):
			model_name.pop()
		
		for layer in new_model.layers:
  			model_name.add(layer)
		return {"message": "model successfully updated"}
	else:
		return {"error" : "invalid key"}, 403

@app.route("/update/metadata/<model_name>", methods = ['PUT'])
def update_metadata(model_name, replaceable, replacee):
	key = request.form['key']
	if key == dev_key:
		data = pd.DataFrame(model_name)
		model_name.replace(to_replace = replaceable,
           value=replacee)
		return {"message": "model metadata successfully updated"}, 200
	return {"error" : "invalid key"}, 403

@app.route("/update/metadata-tag/<model_name>", methods = ['PUT'])
def update_metadata_tag(model_name):
	key = request.form['key']
	if key == dev_key:
		# TODO: update model metadata tag...
		return {"message": "model metadata tag successfully updated"}, 200
	return {"error" : "invalid key"}, 403


#Delete/Delete
@app.route("/delete/<model_name>", methods = ['DELETE'])
def delete_model(model_name):
	key = request.form['key']
	if key == dev_key:
		# delete model...
		for i in len(model_name.layers):
			model_name.pop()
		return {"message": "model successfully deleted"}, 200
	return {"error" : "invalid key"}, 403


@app.route("/delete/metadata-tag/<model_name>", methods = ['DELETE'])
def delete_metadata_tag(model_name):
	key = request.form['key']
	if key == dev_key:
		# delete model metadata tag...

		return {"message": "model metadata tag successfully deleted"}, 200
	return {"error" : "invalid key"}, 403


if __name__ == "__main__":
	app.run(debug=True, threaded=True, host=HOST, port=PORT) 