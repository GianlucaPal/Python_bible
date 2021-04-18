#get sentence from user

original = input('Enter a sentence: ').strip().lower()

#split sentense into words

words = original.split()

#loop through words and convert

newWords = []

for word in words:
    if word[0] in 'aeiou':
        newWord = word + 'ay'
        newWords.append(newWord)
    else:
        vowelPos = 0
        for letter in word:
            if letter not in 'aeiou':
                vowelPos = vowelPos + 1
            else:
                break
        cons = word[:vowelPos]
        theRest = word[vowelPos:]
        newWord = theRest + cons+'ay'
        newWords.append(newWord)
        
#stick words back together
output=' '.join(newWords)

#output final string

print(output)
