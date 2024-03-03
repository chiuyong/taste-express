import os
# -*- coding: utf-8 -*-

restaurants = [
    {'name': 'Restaurant A', 'category': 'Japanese', 'active': False}, 
    {'name': 'Restaurant B', 'category': 'Italian', 'active': True}
  ]

def render_program_name():
   ''' Exibe o nome estilizado do programa na tela '''
  print(''' 
  ████████╗░█████╗░░██████╗████████╗███████╗  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
  ╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
  ░░░██║░░░███████║╚█████╗░░░░██║░░░█████╗░░  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
  ░░░██║░░░██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
  ░░░██║░░░██║░░██║██████╔╝░░░██║░░░███████╗  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
  ░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░

  ''')

def render_menu():
  ''' Exibe as opções disponíveis no menu principal '''
  print('1. Register Restaurant')
  print('2. List Restaurants')
  print('3. Switch Active Restaurant')
  print('4. Exit\n')

def choose_option():
  ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
  '''
  try:
    selected_option = int(input('Select one option: '))
    if selected_option == 1:
      register_restaurant()
    elif selected_option == 2:
      list_restaurants()
    elif selected_option == 3:
      switch_active_restaurant()
    elif selected_option == 4:
      exit_program()
    else:
      invalid_option()
  except:
    invalid_option()

def exit_program():
  ''' Exibe mensagem de finalização do aplicativo '''
  render_option_subtitle('Program exited')

def return_to_menu():
  ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
  input('\nPress any key to return to menu ')
  main()

def render_option_subtitle(subtitle):
  ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
  '''
  os.system('clear')
  row = '*' * (len(subtitle))
  print(row)
  print(subtitle, end='\n\n')
  print(row)
  
def invalid_option():
  ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
  print('Invalid option')
  return_to_menu()

def register_restaurant():
  ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

  '''
  render_option_subtitle('Register new restaurant')
  restaurant_name = input('Write the name of a restaurant: ')
  restaurant_category = input(f'Write the category of the restaurant {restaurant_name} ')
  
  restaurants.append({'name': restaurant_name, 'category': restaurant_category, 'active': False})
  print(f'The restaurant {restaurant_name} was successfully registered!')
  return_to_menu()

def list_restaurants():
  ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
  '''

  render_option_subtitle('List restaurants')
  print(f"{'Restaurant name'.ljust(21)} | {'Restaurant category'.ljust(20)} | Status ")
  for restaurant in restaurants:
    print(f".{restaurant['name'].ljust(20)} | {restaurant['category'].ljust(20)} | {'Is active' if restaurant['active'] else 'Is deactivated'}")
  
  return_to_menu()
  
def switch_active_restaurant():
  ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
  '''
  render_option_subtitle('Switching active restaurant')
  restaurant_name = input('Write the name of the restaurant which you wish to switch the active state: ')
  restaurant_found = False
  for restaurant in restaurants:
    if restaurant_name == restaurant['name']:
      restaurant['active'] = not restaurant['active']
      restaurant_found = True
      message = f'The restaurant {restaurant_name} was successfully activated!' if restaurant['active'] else f'The restaurant {restaurant_name} was successfully deactivated!' #Ternary
      print(message)
  if not restaurant_found:
    print(f'The restaurant {restaurant_name} was not found!')
  return_to_menu()

def main():
  ''' Função principal que inicia o programa '''
  os.system('clear')
  render_program_name()
  render_menu()
  choose_option()

if __name__ == '__main__':
  main()