# for i in range(1, 11,): #start, stop, step
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i * j}')
# dict_ = {"a": 1, "b": 2, "c": 3}
# for i in dict_:
#     print(i, dict_[i])
cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for car in cars:
    print(f'Я езжу на автомобиле марки {car}')
    cars_count += 10
print(f'Общее кол-во автомобилей: {cars_count}')


