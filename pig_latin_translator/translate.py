def pig_latin(content = ""):
  if not(content):
    print('Please enter in a sentence')
    content = input()

  translated_content = content.split()

  for index, word in enumerate(translated_content):
    first_letter = word[0]

    if first_letter in 'aeiou':
      translated_content[index] = f'{word}ay'
    else:
      translated_content[index] = f'{word[1:]}{first_letter}ay'

    if index != 0 and index % 15 == 0:
      translated_content[index] +='\n'
    else:
      translated_content[index] +=' '

  translated_content[0] = translated_content[0].capitalize()

  formatted_output = ''.join(translated_content)

  output = open("pig_latin_translation.txt","w+")
  output.truncate(0)
  output.write(formatted_output)
  output.close()

  print()
  print()
  print('The pig latin translation is:')
  print('================================')
  print()
  print(formatted_output)
  print()
  print('================================')

print()
print('Welcome to the pig latin translator!')
print()
print('If you would like to translate a file, please make sure its contents are in the "content.txt" file provided')
print()
input('Would you like to translate a file? [y:N]')

pig_latin()