##a = 1
##b = 101
##c = ''
##d= ''
##
##while a < b :
##    if a%2 ==0:
##        c = a
##    else:
##        d = a
##    print(c, d, sep=' \t')
##    a +=1
##'''
##5+1 = 6
##5++ = 6
##1+5 = 6
##++5 = 6
##
##5-- = 5 -1 ==4
##
##a += 1
##a++
##a = a+1
##'''

country = input ('which country is giant  is giant of Africa: ').capitalize()

while country != 'Nigeria':
    print ('Not correct ')
    country = input ('Which country is the giant of Africa: ').capitalize()

print('Correct !')
