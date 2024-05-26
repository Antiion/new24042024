import random

boot_skates = 5#int(input('Количество роликов: '))
skate_list = []
people_list = []
for _ in range(boot_skates):
    skate_list.append(random.randint(39, 45))
print(skate_list)
amount_people = 3#int(input('Количество людей: '))
for ap in range(amount_people):
    people_list.append((random.randint(39, 45)))
print(people_list)

rent_count = 0
for pl in people_list:
    if pl in skate_list:
        rent_count += 1
        skate_list.remove(pl)

print('Наибольшее количество людей, которые смогут взять ролики:', rent_count)