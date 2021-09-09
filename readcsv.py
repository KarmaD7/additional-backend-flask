import pandas as pd
import numpy as np


def get_entity_name(course: str):
  data = pd.read_csv('dataset/' + course +'.csv')
  data = list(np.array(data))
  entity_names = [triples[2] for triples in data if triples[1] == 'http://www.w3.org/2000/01/rdf-schema#label']
  entity_names = list(set(entity_names))
  return entity_names

course_name = 'biology'
out_filename = "name/" + course_name + ".txt"
course_entities = get_entity_name(course_name)
# print(course_entities)
file = open(out_filename, 'w')
file.close()
with open(out_filename, 'w') as f:
  for entity in course_entities:
    try:
      f.write(entity + '\n')
    except:
      continue
