def get_bmi(height, weight):
    return weight / ((height / 100) ** 2)


def get_standard_weight(height, weight):
    return ((height / 100) ** 2) * 22


abe = {'height': 170, 'weight': 68}
abe_bmi = get_bmi(abe['height'], abe['weight'])
abe_standard_weight = get_standard_weight(abe['height'], abe['weight'])
print('安倍')
print(f'BMI: {abe_bmi}')
print(f'適性体重: {abe_standard_weight}')

print('------------------')

ike = {'height': 163, 'weight': 80}
ike_bmi = get_bmi(ike['height'], ike['weight'])
ike_standard_weight = get_standard_weight(ike['height'], ike['weight'])
print('池')
print(f'BMI: {ike_bmi}')
print(f'適性体重: {ike_standard_weight}')
