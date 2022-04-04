import json

dct = {
    1: {
        'enemies': [
            {'name': 'SmallSquare', 'position': (50, 50)},
            {'name': 'SmallSquare', 'position': (100, 150)},
            {'name': 'SmallSquare', 'position': (375, 300)},
        ]
    },
    2: {
        'enemies': [
            {'name': 'SmallSquare', 'position': (70, 80)},
            {'name': 'BigSquare', 'position': (200, 250)},
            {'name': 'BigSquare', 'position': (380, 170)},
            {'name': 'SmallSquare', 'position': (275, 100)},
        ]
    },
    3: {
        'enemies': [
            {'name': 'BigSquare', 'position': (400, 90)},
            {'name': 'BigSquare', 'position': (200, 170)},
            {'name': 'BigSquare', 'position': (100, 305)},
        ]
    }
}

with open('levels.json', 'w') as file:
    json.dump(dct, file, indent=2)
