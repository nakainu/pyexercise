bank = {}
statement = {}
with open('accounts.csv', encoding='utf-8') as f:
    f.readline()
    for row in f:
        col = row.split(',')
        bank[col[0]] = f'{col[1]}-{col[2]}'


with open('statements.csv', encoding='utf-8') as f:
    f.readline()
    for row in f:
        col = [r.strip() for r in row.split(',')]
        id = col[3]
        if id not in statement:
            statement[id] = 0
        statement[id] += int(col[2])


for key, val in statement.items():
    print(f'{bank[key]}: {val}')
