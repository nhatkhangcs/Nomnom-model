from model.model import EmbeddingModel
from data.dataReader import DataReader
import pickle
import os
# load DATA_PATH and MODEL_PATH
DATA_PATH = 'data/RAW_recipes.csv'
MODEL_PATH = 'scripts/model/embeddings.pkl'

# data reader
data_reader = DataReader(DATA_PATH)
data = data_reader.load_data_for_embeddings('name') #only embedding the name of food

# create model

embeddings = None

model = EmbeddingModel()

# load data to model
model.read_data(data)

if not os.path.exists(MODEL_PATH):
    # embedding
    embeddings = model.embedding(data)

    # pkl
    with open('../embeddings.pkl', 'wb') as f:
        pickle.dump(embeddings, f)

else:
    with open(MODEL_PATH, 'rb') as f:
        embeddings = pickle.load(f)
        model.embeddings = embeddings

# print(embeddings)
# Give a input sentence, retrieve which embeddings are most similar to the input sentence
input_sentence = 'fried chicken'

# retrieve similar embeddings
similar_embeddings = model.similar_embeddings(input_sentence)

itemList = data_reader.dataframe_creator()

print(similar_embeddings)

print(similar_embeddings[0][1])

# retrieve information for similar_embeddings[0] (top 1)
# each embedding is a tuple (similarity_score, food_name), need to retrieve with same food name
for i in range(len(itemList)):
    if similar_embeddings[0][1] == itemList.iloc[i][0]:
        print(itemList.iloc[i])
        break