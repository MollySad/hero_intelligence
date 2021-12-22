import requests


def hero_intelligence(hero_list):
    hero = {}
    max = 0

    for name in hero_list:
        url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
        res = requests.get(url)

        hero[name] = int(res.json()['results'][0]['powerstats']['intelligence'])

    for name in hero:
        if hero[name] > max:
            max = hero[name]
            hero_name = name

    return hero_name


if __name__ == '__main__':
    
    print(f'Саиый умный супергерой - {hero_intelligence(["Hulk", "Captain America", "Thanos"])}')