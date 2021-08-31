# .extend()와 .append()

a = ['star', 'love']
a.append(['spade'])
print(a) #=> ['star', 'love', ['spade']]

a.extend(['clover'])
print(a) #=> ['star', 'love', ['spade'], 'clover']

a.extend('joker')
print(a) #=> ['star', 'love', ['spade'], 'clover', 'j', 'o', 'k', 'e', 'r']