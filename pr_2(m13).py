num_t = int(input("Введите количество билетов:"))
cost = 0
for i in range(num_t):
    age = int(input("Введите возраст:"))
    if age < 18:
        cost += 0
    elif 18 <= age < 25:
        cost += 990
    else:
        cost += 1390

if num_t > 3:
    cost = cost - ((cost/100)*10)

print("Итого к оплате:", round(cost))









