from data import load_data
from menu import display_menu, get_choice, allow_continue
from lib import display_cargo_list, display_catalog_list, display_catalog_info, search_cargo, add_cargo, del_cargo, move_emp


if __name__ == '__main__':
  cargo = load_data()
  
  while (True):
    display_menu()
    choice = get_choice()
    if choice == 1:
      display_cargo_list(cargo)
    elif choice == 2:
      car_name = input('Введіть назву категорії ')
      display_catalog_list(cargo, car_name)
    elif choice == 3:
      cat_name = input('Введіть назву категорії ')
      car_name = input('Введіть назву товару ')
      display_catalog_info(cargo, car_name, cat_name)
    elif choice == 4:
      car_name = input('Введіть назву товару ')
      search_cargo(cargo, car_name)
    elif choice == 5:
      cat_name = input('Введіть назву категорії ')
      car_name = input('Введіть назву товару ')
      size = input('Введіть розмір товару ')
      color = input('Введіть колір товару ')
      price = input('Введіть ціну товару ')
      add_cargo(cargo, cat_name, car_name, size, color, price)
    elif choice == 6:
      cat_name = input('Введіть назву категорії ')
      car_name = input('Введіть назву товару ')
      del_cargo(cargo, cat_name, car_name)
    elif choice == 7:
      cat_name = input('Введіть назву категорії ')
      car_name = input('Введіть назву товару що хочете перемстити ')
      cat_name1 = input('Введіть назву категорії куди хочете перемістити ')
      car_name1 = input('Введіть назву товару ')
      move_emp(cargo, cat_name, car_name, cat_name1, car_name1)
    elif choice == 9:
      break
    else:
      pass
    if not allow_continue():
      break
  print('Програма завершена')