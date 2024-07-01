list_input = []
for i in range(6):
  user_input = input("Enter a value")
  try:
      list_input.append(int(user_input))
      
  except:
    list_input.append((user_input))


  print(list_input))
