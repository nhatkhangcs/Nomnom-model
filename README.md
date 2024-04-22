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
# Instant deploy
Run all in `which_to_nomnom.ipynb`

# Installation
~1.5GB from transformer
```
pip install requirements.txt
```
install data in [food recommend data](https://www.kaggle.com/code/ngohoantamhuy/food-recommendation-systems/input?select=RAW_recipes.csv&fbclid=IwAR0WfEgG5ycCFpElFpi5BQpm0CujFczIxra42EvMgAWKUfU2Bit4gCKVMRc) in the root of project like the project tree

# Search model usage
Model size: ~2.2GB (binary)
- Download by gdown:
    ```bash
    cd scripts
    gdown 1i3eT_VF6yA_G4GvlAsehwSeIQmzXzn40 -O data/RAW_recipes.csv
    gdown 1-7p4bHR2IAWAaZHbaRS-IUYWb1TMsvWS -O data/embedded_names.pkl
    gdown 1-6Rvib4upv9VHEl1nwB2-D1SczbTieD2 -O data/embedded_ingredients.pkl
    gdown 1yZQi3gWc90xGwXDvwvuTTMGbzzzkl1Gc -O data/embedded_tags.pkl
    gdown 1nL4rOEbZiEEVqM1EdDL7WpifMcparEax -O data/scaler.pkl
    gdown 1-9ee6DlGTn5RhmONWQdqGzCdtiGP4POr -O data/nutrition_scaled.pkl
    ```
## Run (`./scripts`)
```bash
python app.py
```

### More info
```python
# Use this method
model.search(
    name: str, 
    ingredients: str,
    tags: list[str],
    nutrition: list[float],
    k: int = 1000, # No need to care, k high => Better results but SLOWER. inbox Tri Duc for more hot hot hot info!
) -> list[tuple[food_info, score]] # Higher score -> More similar
```
```python
# Example
similar_foods = model.search(
    name='salmon',
    ingredients='salmon, wasabi',
    tags=['japanese', '15-minutes-or-less'],
    nutrition=[600, 80, 10, 50, 150, 30, 50], # NUTRITIONS = ['calories', 'fat', 'sugar', 'sodium', 'protein', 'saturated_fat', 'carbohydrates']
)[:10] # Take 10 most similar (can take up to k)
```
### Get ID of the foods
```python
ids = [similar_food[0]['id'] for similar_food in similar_foods]
```