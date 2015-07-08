import argh
import requests
from bs4 import BeautifulSoup

BASE_URL = r"https://github.com/{user}"

def get_soup_for_user(username):
    resp = requests.get(BASE_URL.format(user=username))
    resp.raise_for_status()

    soup = BeautifulSoup(resp.content, "html.parser")
    return soup

@argh.named("contribs")
def get_contribs_for_user(username):
    soup = get_soup_for_user(username)
    
    el = soup.find_all("span", {"class": "contrib-number"})[0] 

    contribs = el.text

    print "{u}'s contributions: {c}".format(
        u=username,
        c=contribs,
    )

@argh.named("streak")
def get_streak_for_user(username):
    soup = get_soup_for_user(username)
    
    el = soup.find_all("span", {"class": "contrib-number"})[1]

    streak =  el.text

    print "{u}'s current streak: {s}".format(
        u=username,
        s=streak,
    )


if __name__ == "__main__":
    parser = argh.ArghParser()
    parser.add_commands([get_streak_for_user, get_contribs_for_user])

    parser.dispatch()


