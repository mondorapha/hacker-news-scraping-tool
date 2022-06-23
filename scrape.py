import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get('https://news.ycombinator.com/')
parsed_soup = BeautifulSoup(res.text, 'html.parser')
titlelink = parsed_soup.select('.titlelink')
subtext = parsed_soup.select('.subtext')


def sort_by_votes(dictionary):
    return sorted(dictionary, key=lambda k: k['points'], reverse=True)


def create_custom_hackernews(links, votes):
    new_hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        hyperlinks = links[index].get('href', None)
        vote = votes[index].select('.score')
        if len(vote):
            points = int((vote[0].getText().replace(' points', '')))
            if points > 99:
                new_hn.append(
                    {'title': title, 'link': hyperlinks, 'points': points})
    return sort_by_votes(new_hn)


pprint.pprint(create_custom_hackernews(titlelink, subtext))
