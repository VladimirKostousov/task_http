import requests


url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
request = requests.get(url).json()
heroes_list = ['Hulk', 'Captain America', 'Thanos']
int_hero_dict = {}
for hero in heroes_list:
    for heroes in request:
        if heroes['name'] == hero:
            int_hero_dict.update({hero: heroes['powerstats']['intelligence']})
print(f'Самый интеллектуальный герой: {[k for k,v in int_hero_dict.items() if v == max(int_hero_dict.values())]}')


