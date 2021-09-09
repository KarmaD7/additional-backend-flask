from flask_cors import CORS
from flask import Flask, redirect, url_for, make_response
from flask import request, jsonify
import requests, json
import numpy as np
import gensim
from gensim.models import KeyedVectors

DIM = 300
model = KeyedVectors.load_word2vec_format('entity/chinese.txt')
vocab = model.vocab
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/recommend', methods = ['POST'])
def recommend():
  entities = request.json
  entities = entities.get('entities')
  averaged_vector = np.zeros(DIM)
  cnt = 0

  for entity in entities:
    if entity not in app.vocab:
      continue
    cnt += 1
    averaged_vector += model[entity]
  
  if cnt == 0:
    averaged_vector = np.random(DIM)
  else:
    averaged_vector = averaged_vector / cnt

  similar = model.most_similar([averaged_vector])
  result = [entity for entity in similar.keys()]
  res = {'success': True, "result": result }

  return jsonify(res), 200

if __name__ == "__main__":
  app.run(host="127.0.0.1", port=8888, debug=True)