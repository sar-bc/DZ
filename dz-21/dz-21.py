# DZ-21
physics = {'Максим', 'Матвей', 'Александр'}
mathematics = {'Матвей', 'Евгения', 'Михаил', 'Максим', 'Наталья'}
print("Все призеры: ", physics | mathematics)
print("Призеры обеих олимпиад: ", physics & mathematics)
print("Обновленный список призеров по математике: ", mathematics & physics)
