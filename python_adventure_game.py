rooms = {
    'start': {
        'description': 'You are in a dark room. There is a door to your north.',
        'north': 'room1'
    },
    'room1': {
        'description': 'You are in room 1. There is a door to your east and south.',
        'east': 'room2',
        'south': 'start'
    },
    'room2': {
        'description': 'You are in room 2. There is a door to your west and south.',
        'west': 'room1',
        'south': 'room3'
    },
    'room3': {
        'description': 'You are in room 3. You can see the treasure behind a door to your south ! Congratulations!',
        'south': 'room4'
        
    },
    'room4':{
        'descritpion': 'You are in the last room. You collected the treasure!',
        'end': True
    }
}
def show_room(room):
    print(room['description'])

    if 'north' in room:
        print('There is a door to your north.')
    if 'east' in room:
        print('There is a door to your east.')
    if 'south' in room:
        print('There is a door to your south.')
    if 'west' in room:
        print('There is a door to your west.')
def get_action(room):
    while True:
        action = input('What do you want to do? ').lower().strip()

        if action == 'north' and 'north' in room:
            return room['north']
        elif action == 'east' and 'east' in room:
            return room['east']
        elif action == 'south' and 'south' in room:
            return room['south']
        elif action == 'west' and 'west' in room:
            return room['west']
        else:
            print('Invalid action. Try again.')
current_room = rooms['start']

while 'end' not in current_room:
    show_room(current_room)
    next_room = get_action(current_room)
    current_room = rooms[next_room]

print(current_room['description'])
