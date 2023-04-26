import requests
from API_KEY import key

def get_news_title(topic):

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={key}"
    data = requests.get(url).json()

    for index, row in enumerate(data["articles"]):
        print(index+1, row["title"])

def get_news_details(index, topic):

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={key}"
    data = requests.get(url).json()

    print(data["articles"][index]["content"])




if __name__ == "__main__":
    topic_input = input("Please write your topic of interest and the app will provide the list of all available news: ")
    get_news_title(topic_input)

    while True:
        news_selection = input("Please enter the number of news you would like to read, to quit the app please enter 0: ")

        if news_selection == '0':
            break
        else:
            print(news_selection)
            index = int(news_selection)-1
            get_news_details(index, topic_input)
