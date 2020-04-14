def get_bmi(height, weight):
    return weight / ((height / 100) ** 2)


def fatness(bmi):
    if 18.5 > bmi:
        return '痩せ型'
    elif 18.5 <= bmi < 25.0:
        return '標準'
    elif 25.0 <= bmi < 30:
        return '肥満'
    else:
        return '過度の肥満'


person = []
person.append({'name': 'abe', 'height': 170, 'weight': 68})
person.append({'name': 'ike', 'height': 163, 'weight': 80})
person.append({'name': 'uno', 'height': 152, 'weight': 45})


for p in person:
    bmi = get_bmi(p['height'], p['weight'])
    print(p['name'])
    print(f'BMI: {bmi}')
    print(f'肥満度: {fatness(bmi)}')
    print('------------------')
