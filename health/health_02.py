abe_height = 170
abe_weight = 68
ike_height = 163
ike_weight = 80

abe_bmi = abe_weight / ((abe_height / 100) ** 2)
abe_standard_weight = ((abe_height / 100) ** 2) * 22
ike_bmi = ike_weight / ((ike_height / 100) ** 2)
ike_standard_weight = ((ike_height / 100) ** 2) * 22

print(f'安倍のBMI: {abe_bmi}')
print(f'安倍の適正体重: {abe_standard_weight}')
print(f'池のBMI: {ike_bmi}')
print(f'池の適正体重: {ike_standard_weight}')
