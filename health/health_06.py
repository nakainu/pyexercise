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


abe = {'height': 170, 'weight': 68}
abe_bmi = get_bmi(abe['height'], abe['weight'])
print('安倍')
print(f'BMI: {abe_bmi}')
print(f'肥満度: {fatness(abe_bmi)}')

print('------------------')

ike = {'height': 163, 'weight': 80}
ike_bmi = get_bmi(ike['height'], ike['weight'])
print('池')
print(f'BMI: {ike_bmi}')
print(f'肥満度: {fatness(ike_bmi)}')
