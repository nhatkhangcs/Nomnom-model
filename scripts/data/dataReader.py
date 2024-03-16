# Import the pickle library
import pandas as pd
import pickle
import os

class DataReader:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = pd.read_csv(data_path)

    def load_data_embed_name(self):
        '''
            return: pandas dataframe
        '''
        
        return self.data['name']
    
    def dataframe_creator(self):
        '''
            return: list of items <food_id, name, picture_url, rating, calories, sugar, podium, protein, saturated_fat> 
        '''
        print('[+] Loading data into DataReader...')
        if os.path.exists('data/recipe_list.pkl'):
            with open('data/recipe_list.pkl', 'rb') as f:
                recipe_list = pickle.load(f)
                return recipe_list
        # Clean and split tags using list comprehensions
        df_process = self.data.copy()
        df_process['tags'] = df_process['tags'].apply(lambda tags: [tag.strip()[1:-1] for tag in tags.strip()[1:-1].split(',') if tag.strip()])

        # Define the template for applying to the 'nutrition' column
        df_process['nutrition'] = df_process['nutrition'].apply(lambda nutrition: [float(num) for num in nutrition.strip('[]').split(',')])
        recipe_list = []
        for index, row in df_process.iterrows():
            recipe_list.append((row['name'], row['id'], row['tags'], row['nutrition'], row['description']))

        # Open a file for writing in binary mode
        with open('data/recipe_list.pkl', 'wb') as f:
            # Pickle the recipe_list object
            pickle.dump(recipe_list, f)
        return recipe_list
    
if __name__ == '__main__':
    list_items = []
    # each item is a dictionary, each dictionary has the following keys: food_id, name, picture_url, rating, calories, sugar, podium, protein, saturated_fat
    data_reader = DataReader('data/RAW_recipes.csv')
    #data = data_reader.load_data_embed_name()
    #print(data)
    # print row names
    #print(data_reader.dataframe_creator().columns)
    #print(data_reader.dataframe_creator().iloc[[0]])

    