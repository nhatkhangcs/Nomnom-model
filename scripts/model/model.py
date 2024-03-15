# from sentence_transformers import SentenceTransformer
# sentences = ["This is an example sentence", "Each sentence is converted"]

# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# embeddings = model.encode(sentences)
# print(embeddings)

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class EmbeddingModel:
    def __init__(self):
        self.data = []
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        self.embeddings = None

    def embedding(self, sentences):
        '''
            sentences: list of strings
            return: list of embeddings
        '''
        print('[+] Embedding sentences...')
        self.embeddings = self.model.encode(sentences)
        return self.embeddings
        
    def read_data(self, data):
        '''
            data: list of strings
        '''
        print('[+] Loading data into model...')
        self.data = data

    def similar_embeddings(self, input):
        '''
            input: string
            return: list of similar embeddings
        '''
        print('[+] Retrieving similar embeddings...')
        input_embedding = self.model.encode(input)
        # use cosine similarity to find similar embedding
        similarity_list = []
        # calculate similarity score for each pair of <input, embedding, index>
        for i, embedding in enumerate(self.embeddings):
            similarity = cosine_similarity([input_embedding], [embedding])[0][0]
            similarity_list.append((similarity, self.data[i]))

        # get top 10
        similarity_list = sorted(similarity_list, reverse=True)[:10]

        # return embeddings with highest similarity score
        return similarity_list


if __name__ == '__main__':
    model = EmbeddingModel()
    sentences = ["This is an example sentence", "Each sentence is converted"]
    print(model.embedding(sentences))