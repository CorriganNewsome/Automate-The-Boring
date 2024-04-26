'''

# Annoying while loop that will continue unless the user enters 'your name'

name = ''
while name != 'your name':
    print('Please type your name')
    name = input()
print('Thank you')
'''
'''
# continue statment
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello Joe. What is the password? (Hint: It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access Granted')


# For Loops
print('My name is')
for i in range(5):
    print('Corrigan Five Times (' + str(i) + ')')
    '''
# range with step
for i in range(0, 12, 2):
    print (i)