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
    }
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
    }
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

age = input('Please enter Your age as a number:'/n)

movie = input('Enter the name of the movie You want to see (please put your choice in ""):')

time = input('Please chose a screening time (please cose from morning, afternoon or evening, please put your choice in "")')

age_group = None
if (age < 16):
    age_group = 'child'
elif (age < 60):
    age_group = 'adult'
else:
    age_group = 'senior'

final_ticket_price = ticket_price_index[movie]['times'][time][age_group]['rating']
if (rating == 'R' and age_group == 'child'):
    print('Sorry You have to be at least 16 years of age to see this movie')
    break
else:
    print(f'The ticket will cost: {final_ticket_price} Euros')