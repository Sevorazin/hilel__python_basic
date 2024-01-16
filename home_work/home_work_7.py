"""
Даний словник, створити новий словник, змінивши місцями ключ та значення.
 У новий словник вставляти лише ті пари ключ-значення, які мають значення у початковому словнику понад 2000
chess_players = {
"Carlsen, Magnus": 1865,
"Firouzja, Alireza": 2804,
"Ding, Liren": 2799,
"Caruana, Fabiano": 1792,
"Nepomniachtchi, Ian": 2773
}
*Додаткове не обов'язкове завдання:
значення нового словника повинні складатися не з прізвища та імені розділених комою,
 а з прізвища, тільки першої літери імені та точки.
Результат має бути наступним:
new_chess_players = {
2804: 'Firouzja A.',
2799: 'Ding L.',
2773: 'Nepomniachtchi I.'
}
"""

chess_players = {"Carlsen, Magnus": 1865,
                 "Firouzja, Alireza": 2804,
                 "Ding, Liren": 2799,
                 "Caruana, Fabiano": 1792,
                 "Nepomniachtchi, Ian": 2773
                 }

new_chess_players = {}


def players():
    for player in chess_players:
        key, item = player, chess_players[player]
        if item < 2000:
            continue
        else:
            a, b = key.split()
            b_1 = b[0:1]+"."
            key = a + b_1
            key, item = item, key
            new_couple = {key: item}
            new_chess_players.update(new_couple)


players()
print("new_chess_players : ", new_chess_players)
