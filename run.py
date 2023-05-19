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