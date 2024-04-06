<!-- # Project tree
. NomNom-model
 * [data](./data)
 * [scripts](./scripts)
   * [apis](./scripts/apis)
   * [data](./scripts/data)
   * [model](./scripts/model)
   * [constant.py](./scripts/constant.py)
   * [data_reader.ipynb](./scripts/data_reader.ipynb)
   * [food-recommendation-systems.ipynb](./scripts/food-recommendation-systems.ipynb)
   * [main.py](./scripts/main.py)
   * [offical_preprocess.ipynb](./scripts/offical_preprocess.ipynb)
   * [subtag.txt](./scripts/subtag.txt)
 * [.gitignore](./.gitignore)
 * [README.md](./README.md)
 * [requirements.txt](./requirements.txt) -->

# Installation
~1.5GB from transformer
```
pip install requirements.txt
```
install data in [food recommend data](https://www.kaggle.com/code/ngohoantamhuy/food-recommendation-systems/input?select=RAW_recipes.csv&fbclid=IwAR0WfEgG5ycCFpElFpi5BQpm0CujFczIxra42EvMgAWKUfU2Bit4gCKVMRc) in the root of project like the project tree

# Search model usage
Model size: ~1.37GB (binary)
Make sure to download it to `Nomnom-model/scripts/model/model0604.pkl`. 

- Download from Google Drive:
  [Model link (in drive folder `[232] Nomnom WebApp`)](https://drive.google.com/file/d/10miJrjCwN-WyyPpyBDw0b6Cg1HGgPepr/view?usp=drive_link)
- Download by gdown:
    ```bash
    gdown 10miJrjCwN-WyyPpyBDw0b6Cg1HGgPepr -O Nomnom-model/scripts/model/model0604.pkl
    ```
## Run
See `scripts/similar_foods.py` and `model/model.py`
```bash
cd scripts
python scripts/similar_foods.py
```

### More info
```python
# Use this method
model.search(
    name: str, 
    ingredients: str,
    tags: str,
    nutrition: list[float],
    k: int = 1000, # No need to care, k high => Better results but SLOWER. inbox Tri Duc for more hot hot hot info!
) -> list[tuple[food_info, score]] # Higher score -> More similar
```
```python
# Example
similar_foods = model.search(
    name='salmon',
    ingredients='salmon, wasabi',
    tags='japanese, 15-minutes-or-less',
    nutrition=[600, 80, 10, 50, 150, 30, 50], # NUTRITIONS = ['calories', 'fat', 'sugar', 'sodium', 'protein', 'saturated_fat', 'carbohydrates']
)[:10] # Take 10 most similar (can take up to k)
```
### Get ID of the foods
```python
ids = [similar_food[0]['id'] for similar_food in similar_foods]
```