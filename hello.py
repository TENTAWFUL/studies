# This program greets you and asks a few questions.

print('Hello!')

input()

print('What is your name?')

name=input()

print('Nice to meet you, ' + name + '!')
print('The length of your name is:')
print(len(name))
print('What is your age?')

age=input()

print(name + ', You will be ' + str(int(age) + 1) + ' in a year. Feel old yet?')
print('Thank you for taking the time to try out my first program.')
print('(Type anything to exit)')

input()
