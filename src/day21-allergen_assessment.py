from santas_little_helpers import *
from collections import defaultdict

today = day(2020, 21)


def present(a_foods, i_foods):
  return all(a_food in i_foods for a_food in a_foods)


def find_inert_ingredients(foods):
  ingredient_map = defaultdict(set)
  allergen_map = defaultdict(set)
  for idx, (ingredients, allergens) in enumerate(foods):
    for ingredient in ingredients:
      ingredient_map[ingredient].add(idx)
    for allergen in allergens:
      allergen_map[allergen].add(idx)

  non_allergen_used = 0
  inert_ingredients = set()
  for ingredient, i_foods in ingredient_map.items():
    if any(present(a_foods, i_foods) for a_foods in allergen_map.values()):
      continue
    inert_ingredients.add(ingredient)
    non_allergen_used += len(i_foods)
  return non_allergen_used, inert_ingredients


def dangerous_list(foods, inert_ingredients):
  alls = dict()
  for ingredients, allergens in foods:
    for allergen in allergens:
      if allergen not in alls:
        alls[allergen] = ingredients - inert_ingredients
      else:
        alls[allergen] &= ingredients - inert_ingredients

  dangerous = dict()
  while any(len(allergens) > 1 for allergens in alls.values()):
    for allergen, ingredients in alls.items():
      if len(ingredients) == 1:
        for other in alls.keys():
          if other == allergen:
            continue
          alls[other] -= ingredients
        dangerous[allergen] = next(iter(ingredients))
  return ','.join(ingredient for _, ingredient in sorted(dangerous.items()))


def parse(line):
  ingredients, allergens = line.split(' (contains ')
  ingredients = ingredients.split(' ')
  allergens = allergens[:-1].split(', ')
  return set(ingredients), set(allergens)


def main():
  foods = list(get_data(today, [('func', parse)]))
  non_allergen_used, inert_ingredients = find_inert_ingredients(foods)
  print(f'{today} star 1 = {non_allergen_used}')
  print(f'{today} star 2 = {dangerous_list(foods, inert_ingredients)}')


if __name__ == '__main__':
  timed(main)
