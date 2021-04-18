#get user email address

email = input('what is your email address?: ').strip()

#slice out user name

user = email[:email.index('@')]

#slice domain name

domain = email[email.index('@')+1:]

#fromat message

output = 'your username is {} and your domain name is {}'.format(user,domain)

#display output message

print(output)
