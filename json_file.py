import numpy as np
import pandas as pd
import operator
import json
from pprint import pprint

with open('recipes.json') as f:
    recipes = json.load(f)
# pprint(recipes)


for recipe in recipes:  # начинаем перебор всех рецептов
    if recipe['id'] == 13121:  # если id текущего рецепта равен искомому
        print(recipe['cuisine'])  # выводим на экран кухню, к которой относится блюдо
        break  # и прерываем цикл, т.к. нужное блюдо уже найдено

last_pos = len(recipes) - 1
recipe = recipes[last_pos]
res = recipe['cuisine']
print(res)
res = len(recipe['ingredients'])
print(res)

for recipe in recipes:
    if recipe['id'] == 17636:
        break
rec_list = recipe['ingredients']
check_list = [
    'tomato sauce',
    'spinach',
    'italian seasoning',
    'broccoli',
    'chopped onion',
    'skinless chicken thighs',
    'chopped green bell pepper'
]
rec_set = set(rec_list)
check_set = set(check_list)
intersection = rec_set.intersection(check_set)
print(intersection)
res_list = list(intersection)
pprint(res_list)

for recipe in recipes:
    if recipe['id'] == 42013:
        break
res = len(recipe['ingredients'])
print(res)

for recipe in recipes:
    if recipe['id'] == 23629:
        break
rec_list = recipe['ingredients']
check_list = [
    'eggs',
    'black beans',
    'black olives',
    'dry vermouth',
    'chicken livers',
    'olive oil'
]
rec_set = set(rec_list)
check_set = set(check_list)
diff = check_set - rec_set
res_list = list(diff)
pprint(res_list)

item_set = set()
for recipe in recipes:
    if recipe['cuisine'] == 'italian':
        rec_list = recipe['ingredients']
        for item in rec_list:
            item_set.add(item)
item_list = list(item_set)
res = len(item_list)
pprint(res)

item_set = set()
for recipe in recipes:
    if recipe['cuisine'] == 'russian':
        rec_list = recipe['ingredients']
        for item in rec_list:
            item_set.add(item)
check_list = [
    'bacon',
    'bread slices',
    'buttermilk',
    'red beets',
    'mozzarella cheese',
    'carrots'
]
check_set = set(check_list)
res_set = check_set - item_set
res_list = list(res_set)
pprint(res_list)

item_set = set()
for recipe in recipes:
    rec_list = recipe['ingredients']
    for item in rec_list:
        item_set.add(item)
ingredients = list(item_set)
pprint(ingredients)

food = {}  # создаём пустой словарь для хранения информации об ингредиентах
for item in ingredients:  # перебираем список ингредиентов
    food[item] = 0  # добавляем в словарь ключ, соответствующий очередному ингредиенту
for recipe in recipes:  # перебираем список рецептов
    for item in recipe['ingredients']:  # и список ингредиентов в каждом рецепте
        food[item] += 1  # увеличиваем значение нужного ключа в словаре на 1
pprint(food)

ingr100 = list()
for curr_k, curr_v in food.items():
    if curr_v > 100:
        ingr100.append(curr_k)
pprint(ingr100)

max_v = 0
max_k = ''
for curr_k, curr_v in food.items():
    if curr_v > max_v:
        max_v = curr_v
        max_k = curr_k
pprint(max_k)

ingr1 = list()
for curr_k, curr_v in food.items():
    if curr_v == 1:
        ingr1.append(curr_k)
pprint(ingr1)
pprint(len(ingr1))

with open('recipes.json') as f:
    recipes = json.load(f)


def find_item(cell):
    if item in cell:
        return 1
    return 0


df = pd.DataFrame(recipes)
item_set = set()
for recipe in recipes:
    rec_list = recipe['ingredients']
    item_set |= set(rec_list)

for item in item_set:
    df[item] = df['ingredients'].apply(find_item)
df['ingredients'] = df['ingredients'].apply(len)
print(df)

df.to_csv('recipes.csv', index=False)

df = pd.read_csv('recipes.csv')
ids = df['id'].to_list()
print(ids)

df = pd.read_csv('recipes.csv')
col_names = df.columns.to_list()
ingredients = col_names[3:]
print(ingredients)


df = pd.read_csv('recipes.csv')
ids = df['id'].to_list()
col_names = df.columns.to_list()
ingredients = col_names[3:]


def make_list(curr_df_row):
    curr_ingrs = curr_df_row.iloc[0].to_list()
    ing_len = len(ingredients)
    result = []
    for i in range(3, ing_len):
        if curr_ingrs[i] == 1:
            result.append(ingredients[i-3])
    return result


new_recipes = []
for current_id in ids:
    curr_df_row = df[df['id'] == current_id]
    cuisine = curr_df_row['cuisine'].iloc[0]
    current_ingredients = make_list(curr_df_row)
    current_recipe = {'cuisine': cuisine, 'id': int(current_id), 'ingredients': current_ingredients}
    new_recipes.append(current_recipe)
print(new_recipes)


with open("new_recipes.json", "w") as write_file:
    json.dump(new_recipes, write_file)
