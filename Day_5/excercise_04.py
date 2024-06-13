pizza_size = input('Welcome, Please place your order in sizes: ')

pizza_size = pizza_size.lower()
s_price = 180
m_price = 240
l_price = 290
extra_price = 25
bill = 0
# total = sum(s_price,m_price,l_price,extra_price)
while(pizza_size):
    if pizza_size == 'small':
        bill = s_price
        print('Total invoice: ',s_price)

    elif pizza_size == 'medium':
        bill = m_price
        print('Please pay: ',m_price)

    elif pizza_size == 'large':
        bill = l_price
        print('PLease pay: ',l_price)
    else:
        print('Sorry, Selected size is not Available')
        break

    toppings =input('Do you need Extra toppings: '
                    'Yes or No: ')
    toppings = toppings.lower()
    if toppings== 'yes':
        bill += extra_price
        print('Please pay the extra Amount: ',bill)
        break
    else:
        print('Thank you for order, your order wll be ready in 10 mins')
