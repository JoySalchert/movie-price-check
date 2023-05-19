# index holding the movie names, age ratings, screening time, viewer age options and corresponding ticket prices
ticket_price_index = {
    'When Harry met Sally': {
        'name' : 'When Harry met Sally',
        'rating' : 'G',

        'times' : {
            'morning' : {
                'child' : 10,
                'adult' : 16,
                'senior' : 12
            },
            'afternoon' : {
                'child' : 10,
                'adult' : 18,
                'senior' : 12
            },
            'evening' : {
                'child' : 12,
                'adult' : 20,
                'senior' : 14
            }
        }
    },
    'Snow White and the 7 Dwars': {
        'name' : 'When Harry met Sally',
        'rating' : 'G',

        'times' : {
            'morning' : {
                'child' : 10,
                'adult' : 16,
                'senior' : 12
            },
            'afternoon' : {
                'child' : 10,
                'adult' : 18,
                'senior' : 12
            },
            'evening' : {
                'child' : 12,
                'adult' : 20,
                'senior' : 14
            }
        }
    },
    'Texas Chainsaw Massacre': {
        'name' : 'When Harry met Sally',
        'rating' : 'R',

        'times' : {
            'morning' : {
                'child' : 10,
                'adult' : 16,
                'senior' : 12
            },
            'afternoon' : {
                'child' : 10,
                'adult' : 18,
                'senior' : 12
            },
            'evening' : {
                'child' : 12,
                'adult' : 20,
                'senior' : 14
            }
        }
    }
}

while True:
    age = input('Please enter Your age as a number:\n')
    if age.isdigit():
        age = int(age)
        break
    else:
        print('Sorry Your entry is invalid')

while True:
    movie = input('Enter the name of the movie You want to see:\n')
    if movie in ticket_price_index:
        break
    else:
        print('Sorry Your entry is invalid')

while True:
    time = input('Please chose a screening time (please cose from morning, afternoon or evening:\n')
    if time in ticket_price_index[movie]['times']:
        break
    else:
        print('Sorry Your entry is invalid')

age_group = None
if (age < 16):
    age_group = 'child'
elif (age < 60):
    age_group = 'adult'
else:
    age_group = 'senior'

rating = ticket_price_index[movie]['rating']
if (rating == 'R' and age_group == 'child'):
    print('Sorry You have to be at least 16 years of age to see this movie')
else:
    final_ticket_price = ticket_price_index[movie]['times'][time][age_group]
    print(f'The ticket will cost: {final_ticket_price} Euros')
