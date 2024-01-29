import random

rooms = {
    'start': {
        'description': 'You are in a dark room. Try to escape. There is a door to your north.',
        'north': 'room1'
    },
    'room1': {
        'description': 'You are in room 1. There is a door to your east and south.',
        'east': 'room2',
        'south': 'start'
    },
    'room2': {
        'description': 'You are in room 2. You encounter a friendly character in the room. Choose what to do.',
        'west': 'room1',
        'south': 'room3',
        'east': 'room4',
        'events': {
            'Interact': 'friendly_character',
            'Ignore': 'no_interaction'
        }
    },
    'room3': {
        'description': 'You entered a trap room! Game over.',
        'end': True
    },
    'room4': {
        'description': 'You are in room 4. There is a door to your west and a hidden passage to the north.',
        'west': 'room2',
        'north': 'room5'
    },
    'room5': {
        'description': 'You are in room 5. You see a staircase going up to your west.',
        'west': 'room6'
    },
    'room6': {
        'description': 'Congratulations! You reached the top of the staircase. You won!',
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
        elif 'events' in room and action in room['events']:
            return room['events'][action]
        else:
            print('Invalid action. Try again.')

def handle_event(event):
    if event == 'friendly_character':
        print('You encounter a friendly character in the room.')
        choice = input('Do you want to (1) Chat with the character or (2) Ignore the character? ').strip()
        if choice == '1':
            print('You have a pleasant conversation with the character. They give you a small gift.')
        elif choice == '2':
            print('You decide to ignore the character. They shrug and continue on their way.')
    elif event == 'no_interaction':
        print('You choose not to interact with anything in the room and continue on your journey.')

current_room = rooms['start']

while 'end' not in current_room:
    show_room(current_room)

    if 'events' in current_room:
        choice = input('Choose an option: ' + ', '.join(current_room['events'].keys()) + '\n').strip()
        handle_event(current_room['events'][choice])

    next_room = get_action(current_room)
    current_room = rooms[next_room]

print(current_room['description'])
