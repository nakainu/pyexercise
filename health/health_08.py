from statistics import mean


# BMIを返す
def get_bmi(height, weight):
    return weight / ((height / 100) ** 2)


# 標準体重を返す
def get_standard_weight(height, weight):
    return ((height / 100) ** 2) * 22


# 肥満度の判定
def fatness(bmi):
    if 18.5 > bmi:
        return '痩せ型'
    elif 18.5 <= bmi < 25.0:
        return '標準'
    elif 25.0 <= bmi < 30:
        return '肥満'
    else:
        return '過度の肥満'


# 人物
person = []
person.append({'name': 'abe', 'height': 170, 'weight': 68})
person.append({'name': 'ike', 'height': 163, 'weight': 80})
person.append({'name': 'uno', 'height': 152, 'weight': 45})

for p in person:
    bmi = get_bmi(p['height'], p['weight'])
    standard_weight = get_standard_weight(p['height'], p['weight'])
    print(f'名前: {p["name"]}')
    print(f'BMI値: {bmi} ({fatness(bmi)})')
    print(f'適正体重: {standard_weight}')
    print('------------------')

# 身長・体重の平均値
avg_height = mean(p['height'] for p in person)
avg_weight = mean(p['weight'] for p in person)
print(f'平均身長: {avg_height}')
print(f'平均体重: {avg_weight}')
