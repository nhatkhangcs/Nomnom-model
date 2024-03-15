import pandas as pd

class DataReader:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = None

    def load_data_for_embeddings(self, key):
        '''
            return: pandas dataframe
        '''
        print('[+] Loading data into DataReader...')
        data = pd.read_csv(self.data_path)
        return data[key]
    
    def dataframe_creator(self):
        '''
            return: list of items <food_id, name, picture_url, rating, calories, sugar, podium, protein, saturated_fat> 
        '''
        data = pd.read_csv(self.data_path)
        return data
    
if __name__ == '__main__':
    list_items = []
    # each item is a dictionary, each dictionary has the following keys: food_id, name, picture_url, rating, calories, sugar, podium, protein, saturated_fat
    data_reader = DataReader('data/RAW_recipes.csv')
    #data = data_reader.load_data_for_embeddings('name')
    #print(data)
    # print row names
    #print(data_reader.dataframe_creator().columns)
    #print(data_reader.dataframe_creator().iloc[[0]])

    for i in range(1):
        dict_item = {}
        dict_item['food_id'] = data_reader.dataframe_creator().iloc[i]['id']
        dict_item['name'] = data_reader.dataframe_creator().iloc[i]['name']
        # dict_item['picture_url'] = data_reader.dataframe_creator().iloc[i]['picture_url']
        # dict_item['rating'] = data_reader.dataframe_creator().iloc[i]['average_rating']
        dict_item['description'] = data_reader.dataframe_creator().iloc[i]['description']
        dict_item['nutrition'] = data_reader.dataframe_creator().iloc[i]['nutrition']
        dict_item['tags'] = data_reader.dataframe_creator().iloc[i]['tags']
        # dict_item['votes'] = data_reader.dataframe_creator().iloc[i]['votes']
        list_items.append(dict_item)

    print(list_items)