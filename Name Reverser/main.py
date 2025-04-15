while True:
  name = input("Please enter your name: ")

  first_char = name[0]
  rest = name[1:]

  reversed = ""
  i = 0

  while i < len(rest) - 1:
    reversed += rest[i+1] + rest[i]
    i += 2

    if len(name) % 2 == 0 and i < len(rest):
      reversed += rest[i]

  print("Name reversed: ", first_char + reversed)
  print("Last and first character reversed: ", reversed[-1] + reversed[:i] + first_char)