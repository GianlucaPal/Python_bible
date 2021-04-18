vowels = 0
consonants = 0

for letter in 'supercalafragilisticexpialidocios':
    if letter.lower() in 'aeiou':
        vowels = vowels+1
    elif letter == '':
        pass
    else:
        consonants = consonants+1

print('there are {} vowels'.format(vowels))
print('there are {} consonants'.format(consonants))

students = {
    'male':['Tom','Charlie','Harry','Frank'],
    'female':['Sarah','Huda','Samantha','Emily','Elizabeth']
    }

for key in student.keys():
    for name in students[key]:
        if 'a' in name:
            print(name)
