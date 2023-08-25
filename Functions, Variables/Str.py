name = input('What is your name: ').title()

#Removes whitespace
name = name.strip()

#Split firs name and last name
first, last = name.split(' ')
print(f'hello {first}')