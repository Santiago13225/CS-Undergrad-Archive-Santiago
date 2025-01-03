def display(data):
	print("[Server]: " + data)
	
display("Attempting to initialize the server...")

from time import sleep
from flask import Flask, request, send_file
import logging
from document_scanner import scan

HOST = '192.168.1.199'
PORT = 5000

try:
	app = Flask(__name__)
except Exception as e:
	display("Failed to launch server, terminating process...")
	print(e)
	exit()
display("Successfully launched server")

#Creates a new entry
@app.route("/create/entry", methods = ['POST'])
def handle_entry():
	f = request.files['file']
	#to complete later...
	return None

#Creates many entries
@app.route("/create/entries", methods = ['POST'])
def handle_entries():
	f = request.files['file']
	#to complete later...
	return None

#Query for count of queries
@app.route("/read/count/<filter>", methods = ['GET'])
def handle_count_query(filter):
	return None

#Query for a single entry
@app.route("/read/entry/<filter>", methods = ['GET'])
def handle_get_entry(filter):
	return None

#Query for all entries given a single search
@app.route("/read/search/<filter>", methods = ['GET'])
def handle_search_entries(filter):
	return None

#Query for entry with no or least annotations
@app.route("/read/annotation/min", methods = ['GET'])
def handle_get_entry_min_annotation():
	return None
	
#Query for entry with most annotations
@app.route("/read/annotation/max", methods = ['GET'])
def handle_get_entry_max_annotations():
	return None
	
#Fully replace annotations given image unique identifier
@app.route("/update/annotation-replace/<filter>", methods=['PUT'])
def annotation_replacement(filter):
	return None

#Mix annotations given when given unique image identifer
@app.route("/update/annotate-given-image/<filter>", methods=['PUT'])
def annotate_given_image(filter):
	return None

#Edit metadata of image given unique image identifer
@app.route("/update/edit-metadata-given-image/<filter>", methods=['PUT'])
def edit_metadata_given_image(filter):
	return None

#Edit metadata tag

@app.route("/update/edit-metadata-tag/<filter>", methods=['PUT'])
def edit_metadata_tag(filter):
	return None

#Remove metadata
@app.route("/delete/remove-metadata/<filter>", methods=['DELETE'])
def remove_meta_data(filter):
	return None

#Remove metadata tag
@app.route("/delete/remove-tag/<filter>", methods=['DELETE'])
def remove_meta_data_tag(filter):
	return None

#Remove annotations
@app.route("/delete/remove-annotations/<filter>", methods=['DELETE'])
def remove_annotations(filter):
	return None

#Remove image and all info on it
@app.route("/delete/remove-image/<filter>", methods=['DELETE'])
def remove_image(filter):
	return None

if __name__ == "__main__":
	app.run(threaded=True, host=HOST, port=PORT)