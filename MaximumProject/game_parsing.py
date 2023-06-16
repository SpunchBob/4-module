import requests
from bs4 import BeautifulSoup
response_gener = requests.get('https://store.steampowered.com/?l=russian')
response_best_games = requests.get('https://kanobu.ru/games/pc/popular/')
soup_gener = BeautifulSoup(response_gener.text, "html.parser" )
soup_best_games = BeautifulSoup(response_best_games.text, "html.parser")

def best_games():
    best_game_names = soup_best_games.find_all("div", {"class": "BaseElementCard_body__fcrUh"})
    num_game = 0
    best_games_list = []
    for gm_list in best_game_names:
        num_game += 1
        best_games_list.append(f"{num_game}.{gm_list.a.text}")
    return best_games_list
def action_games():
    games_names = soup_gener.find("div", {"class": "popup_genre_expand_content responsive_hidden", "data-genre-group": "action"})
    games_list = []
    for games_names_list in games_names:
        data = games_names_list.text
        games_list.append(data.strip())
        
    return games_list

def action_games_url():
    games_url = soup_gener.find("div", {"class": "popup_genre_expand_content responsive_hidden", "data-genre-group": "action"}).find_all("a")
    url_list = []
    num_url = 0   
    for games_urls_list in games_url: 
        num_url += 1
        url_list.append(f"{num_url}: {games_urls_list['href']}")
    
    return url_list


def adventure_games():
    games_names = soup_gener.find("div", {"class": "popup_genre_expand_content responsive_hidden", "data-genre-group": "adventure"})
    games_list = []
    for games_names_list in games_names:
        data = games_names_list.text
        games_list.append(data.strip())
        
    return games_list

def adventure_games_url():
    games_url = soup_gener.find("div", {"class": "popup_genre_expand_content responsive_hidden", "data-genre-group": "adventure"}).find_all("a")
    url_list = []
    num_url = 0
    for games_urls_list in games_url: 
        num_url += 1
        url_list.append(f"{num_url}: {games_urls_list['href']}")
    
    return url_list

def rpg_games():
    games_names = soup_gener.find("div", {'class': "popup_genre_expand_content responsive_hidden", "data-genre-group": "rpg"})
    games_list = []
    for games_names_list in games_names:
        data = games_names_list.text
        games_list.append(data.strip())

    return games_list

def rpg_games_url():
    games_url = soup_gener.find("div", {"class": "popup_genre_expand_content responsive_hidden", "data-genre-group": "rpg"}).find_all("a")
    url_list = []
    num_url = 0
    for games_urls_list in games_url: 
        num_url += 1
        url_list.append(f"{num_url}: {games_urls_list['href']}")
    
    return url_list

def simulation_games():
    games_names = soup_gener.find("div", {"class": "popup_genre_expand_content responsive_hidden", "data-genre-group": "simulation"})
    games_list = []
    for games_names_list in games_names:
        data = games_names_list.text
        games_list.append(data.strip())

    return games_list

def simulation_games_url():
    games_url = soup_gener.find("div", {"class": "popup_genre_expand_content responsive_hidden", "data-genre-group": "simulation"}).find_all("a")
    url_list = []
    num_url = 0
    for games_urls_list in games_url: 
        num_url += 1
        url_list.append(f"{num_url}: {games_urls_list['href']}")
    
    return url_list

def strategy_games():
    games_names = soup_gener.find("div", {"class": "popup_genre_expand_content responsive_hidden", "data-genre-group": "strategy"})
    games_list = []
    for games_names_list in games_names:
        data = games_names_list.text
        games_list.append(data.strip())

    return games_list

def strategy_games_url():
    games_url = soup_gener.find("div", {"class": "popup_genre_expand_content responsive_hidden", "data-genre-group": "strategy"}).find_all("a")
    url_list = []
    num_url = 0
    for games_urls_list in games_url: 
        num_url += 1
        url_list.append(f"{num_url}: {games_urls_list['href']}")
    
    return url_list

def sports_and_racing_games():
    games_names = soup_gener.find("div", {"class": "popup_genre_expand_content responsive_hidden", "data-genre-group": "sports_and_racing"})
    games_list = []
    for games_names_list in games_names:
        data = games_names_list.text
        games_list.append(data.strip())

    return games_list

def sports_and_racing_games_url():
    games_url = soup_gener.find("div", {"class": "popup_genre_expand_content responsive_hidden", "data-genre-group": "sports_and_racing"}).find_all("a")
    url_list = []
    num_url = 0
    for games_urls_list in games_url: 
        num_url += 1
        url_list.append(f"{num_url}: {games_urls_list['href']}")
    
    return url_list

best_games()