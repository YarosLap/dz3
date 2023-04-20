# В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.

fruits = "Абрикос, " "авокадо, " "ананас, " "апельсин, " "айва, " "банан, " "бергамот, " "гранат, " "грейпфрут, " "груша, " "гуава, " "джекфрут, " "питахайя, " "карамбола, " "киви, " "клементины, " "кумкват, " "лайм, " "лимон, " "лонган, " "манго, " "мангостин, " "мандарин, " "маракуйя, " "мушмула, " "нектарин, " "папайя, " "персик, " "помело, " "померанец, " "рамбутан, " "салак, " "саподилла, " "свити, " "слива, " "хеномелес, " "хурма, " "цитрон, " "черимойя, " "чомпу, " "яблоко."
 
print("Фрукты в наличии:")
print(fruits, '\n')
 
new_lst = []
letter = input('Введите первую букву фрукта: ').lower()
print()
 
for word in fruits.split():
    if word.lower().startswith(letter):
      if not word[-1].isalpha():
        word = word[:-1]
      new_lst.append(word)
print(f'Фрукты на букву "{letter}" это: ')
print(', '.join(new_lst))
