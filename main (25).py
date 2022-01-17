# This program keeps track the number of pounds  # of food eaten by three monkeys  eat each day 
# during a typical week using a two dimensional list.
# rows is used as a constant to hold the numbers 
# of monkeys.
rows = 3
# columns is used as a constant to hold the number of days.
cols = 7
rows, cols = (3, 7)
data_list= [] 
def main():
  # Initialize an accumulator for food.
  total = 0.0
  # Get each monkey data from the user.
  for r in range(rows):
    print('Monkey #', r + 1, 'Data:')
    monkey_list = []
    
    for c in range(cols):
      print('The amount of food eaten in day', c+ 1, ': ', sep='', end='')
      food_amnt = float(input())
      # Make sure the food amount is not negative.
      while food_amnt < 0:
        print('ERROR: The food amount cannot be negative')
        food_amnt = float(input('Enter the correct food amount: '))
      total += food_amnt
      monkey_list.append(food_amnt)
    data_list.append(monkey_list)
  # Display the monkeys data. 
  print('The data of the whole family of monkeys:')
  print(data_list)  
  # Display the average amount of food eaten each
  # day by the whole family of monkeys.
  print('The average is', total/7)
  # Display the least amount of food eaten during the week by any one monkey.
  print('The least amount is', min(data_list))
  # Display the greatest amount of food eaten during the week by any one monkey.
  print('The greatest amount is', max(data_list))

main()


  


