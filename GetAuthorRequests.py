import requests


def urlfetch(author):
    url = 'https://jsonmock.hackerrank.com/api/articles'
    page = 0
    results = 1
    titles = []
    while results > 0:
        titledata = requests.get(url+'?author='+str(author)+'&page='+str(page)).json()
        # print(timedata)
        # print(timedata)
        if len(titledata["data"]) == 0:
            break
        else:
            page += 1
            results = len(titledata["data"])
            # data.append(timedata["data"])
            for i in titledata["data"]:
                # print(i)
                if i["title"] is not None:
                    titles.append(i["title"])
                elif i["title"] is None and i["story_title"] is not None:
                    titles.append(i["story_title"])
                elif i["title"] is None and i["story_title"] is None:
                    continue

    return titles

print(urlfetch('epaga'))