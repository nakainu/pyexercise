abe = {'height': 170, 'weight': 68}
ike = {'height': 163, 'weight': 80}

abe_bmi = abe['weight'] / ((abe['height'] / 100) ** 2)
abe_standard_weight = ((abe['height'] / 100) ** 2) * 22
ike_bmi = ike['weight'] / ((ike['height'] / 100) ** 2)
ike_standard_weight = ((abe['height'] / 100) ** 2) * 22

print(abe_bmi)
print(ike_bmi)
