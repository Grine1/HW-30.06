from data import save_data
import copy


def display_cargo_list(cargo) -> None:
  i = 0
  for cat in cargo:
    i += 1
    print(f'{i} - {cat}') 


def display_catalog_list(cargo, cat_name) -> None:
  if cat_name not in cargo:
    print('Такої категорії не існує ')
  else:
    cat = cargo[cat_name]
    j = 0
    for car in cat:
      j += 1
      print(f'{j}. {car}')


def check_cargo(cargo, cat_name, car_name) -> bool:
  if cat_name not in cargo:
    print('Такої категорії не існує ')
    return False
  else:
    cat = cargo[cat_name]
    if car_name not in cat:
      print('Такого товару не існує ')
      return False
    else:
      return True 


def display_catalog_info(cargo, cat_name, car_name) -> None:
  if check_cargo(cargo, cat_name, car_name):
    cat = cargo[cat_name]
    if car_name in cat:
      car = cat[car_name]
      sze = car['size']
      col = car['color']
      prc = car['price']
      print(f'{sze} - {col} / {prc}')


def search_cargo(cargo, car_name) -> None:
  success = False
  for cat_name in cargo.keys():
    cat = cargo[cat_name]
    if car_name in cat:
      car = cat[car_name]
      print('Товар найдений')
      print(f'{cat_name} -> {car_name} - {car}')
      success = True
      break
  if not success:
    print(f'Товар {car_name} не найдено')


def add_cargo(cargo, cat_name, car_name, size, color, price) -> None:
  if cat_name not in cargo:
    print(f'{cat_name} не найдено')
    return
  else:
    cat = cargo[cat_name]
    if car_name in cat:
      print(f'{car_name} є такий товар. ')
      return
    else:
      cat[car_name] = {
        'size': size,
        'color': color,
        'price': price,
      }
      save_data(cargo)
      print(f'Товар {car_name} успішно добавленний')


def del_cargo(cargo, cat_name, car_name) -> None:
  if check_cargo(cargo, cat_name, car_name):
    del cargo[cat_name][car_name]
    save_data(cargo)
    print('Товар успішно видалений') 


def move_emp(cargo, cat_name, car_name, cat_name1, car_name1) -> None:
    if cat_name not in cargo:
      print(f'{cat_name} не найдено')
    else:
      cat = cargo[cat_name]
      if car_name not in cat:
        print(f'не найдено')
      else:
        cargo[cat_name1][car_name1] = cargo[cat_name][car_name].copy()
      del cargo[cat_name][car_name]
      save_data(cargo)
      print(f'Характеристики товару успішно добавленні')
