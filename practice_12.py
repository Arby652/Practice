per_cent={'ТКБ':5.6, 'СКБ':5.9, 'ВТБ':4.28, 'СБЕР': 4.0}
d1 = 5.6
d2 = 5.9
d3 = 4.28
d4 = 4.0
k = 100
m = int(input("Введите сумму:"))
deposit = [round(m/k*d1),round(m/k*d2),round(m/k*d3),round(m/k*d4)]
d = max(deposit)

print("deposit =", deposit)
print("Максимальная сумма, которую вы можете заработать - ", d)


