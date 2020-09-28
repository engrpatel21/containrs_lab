print('\n')
#1
print('Out put for #1')
students = ['jack','jill','some dude', 'some other dude']
print(f'second: {students[1]}, last: {students[len(students)-1]}\n')

#2
print('Output for #2')
foods = ('salami', 'sandwich', 'pastrami', 'burger')
for food in foods:
    print(f'{food} is a good food')
print('\n')

#3  
print('Output for #3')  
for food in foods[2:4]:
    print(f'{food} is a good food')
print('\n')

#4
print('Output for #4')
home_town = {
  'city': 'the Darkness',
  'state': 'Shadow Realm',
  'population': 'me'
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}\n")


#5
print('Output for #5')
for key, value in home_town.items():
    print(f'{key} = {value}')
print('\n')

#6 
print('Output for #6')
cohort =[]
for i in range(len(students)):
    cohort.append({
        'student': students[i],
        'fav_food': foods[i]
    })

for students in cohort:
    print(f"{students}")
print('\n')

#7
print('Output for #7')
foods_with_a = [ food for food in foods if food.find('a') > 0]
print(foods_with_a)