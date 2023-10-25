import requests
import tkinter as tk

def getNews():
    api = '1f95d5f4580d4c6e87f54eb60380492d'
    url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey='+api
    news = requests.get(url).json()

    articles = news["articles"]
    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(min(68, len(my_articles))):
        my_news = my_news + my_articles[i] + "\n"

    label.config(text = my_news)

canvas = tk.Tk()
canvas.geometry("2000x2000")
canvas.title("News App")
canvas.colormapwindows()

button = tk.Button(canvas, font = 50, text = "Top business headlines in the US right now", command = getNews)
button.pack(pady = 20)


label = tk.Label(canvas,font = 18, justify = "left")
label.pack(pady = 20)

getNews()
canvas.mainloop()