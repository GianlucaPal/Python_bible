from random import choice

questions = ['why is the sky blue', 'why is there a face on the moon', 'Where are all the dinosaurs']

question = choice(questions)
answer = input(questions).strip().upper()

while answer != 'JUST BECAUSE':
    answer = input('why').strip().upper()

print('oh.....okay')
