import json


def load_data() -> dict:
  with open('hrdep.json', 'r', encoding='utf-8') as file:
    cargo = json.load(file)
  print('Данні успішно загруженні')
  return cargo


def save_data(cargo) -> dict:
  with open('hrdep1.json', 'w', encoding='utf-8') as file:
    json.dump(cargo, file)
  print('Дінні успішно збережені')
  