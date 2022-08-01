from tkinter import messagebox
import smtplib
import requests
from twilio.rest import Client
from tkinter import *
import socket
socket.getaddrinfo('localhost', 8080)

MY_EMAIL = "dummyemailidentity@gmail.com"
MY_PASSWORD = "hello@123"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=MY_EMAIL, password=MY_PASSWORD)
FONT = ("Ariel", 20, "bold")
phone_no = "00"
percentage = 0
email_of_user = "abc@gmail.com"
phone_of_user = "000"
no_of_article = 0

BG = "#91E0FF"
ACCOUNT_SID = "AC6d1635de79e1e0b5d0296d94930bd1cb"
AUTH_TOKEN = "ec44193b0eed916c8acae5c115fa33ef"
STOCK_API_KEY = "2EO4OPP32HH5CY1X"
NEWS_API_KEY = "7084fa8841f0434ea05e35770e008ac8"
STOCK_NAME1 = "TSLA"
STOCK_NAME2 = "NOK"
STOCK_NAME3 = "GOOG"
STOCK_NAME4 = "MSFT"
STOCK_NAME5 = "AAPL"
COMPANY_NAME1 = "Tesla Inc"
COMPANY_NAME2 = "Google"
COMPANY_NAME3 = "Microsoft"
COMPANY_NAME4 = "Apple"
COMPANY_NAME5 = "Nokia"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def tesla():
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME1,
        "apikey": STOCK_API_KEY
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
    data1 = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data1.items()]
    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]
    day_before_yesterday_data = data_list[1]
    data_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
    difference = float(yesterday_closing_price) - float(data_before_yesterday_closing_price)
    up_down = None
    if difference > 0:
        up_down = "⬆️"
    else:
        up_down = "⬇️"
    diff_percent = round((difference / float(yesterday_closing_price)) * 100)
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME1
    }
    if abs(diff_percent) > percentage:
        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news_response.json()["articles"]
        n_articles = articles[:no_of_article]
        formatted_articles = [f"{STOCK_NAME1}: {up_down}{diff_percent}%\nHeadline : {article['title']}. \nBrief : "
                              f"{article['description']}" for article in n_articles]
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        for article in formatted_articles:
            message = client.messages.create(
                body=article,
                from_="+18647322745",
                to=phone_of_user
            )
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email_of_user, msg="Subject:Stock Alert\n\n"+article)
            connection.close()


def nokia():
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME2,
        "apikey": STOCK_API_KEY
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
    data2 = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data2.items()]
    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]
    day_before_yesterday_data = data_list[1]
    data_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
    difference = float(yesterday_closing_price) - float(data_before_yesterday_closing_price)
    up_down = None
    if difference > 0:
        up_down = "⬆️"
    else:
        up_down = "⬇️"
    diff_percent = round((difference / float(yesterday_closing_price)) * 100)
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME5
    }
    if abs(diff_percent) > percentage:
        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news_response.json()["articles"]
        n_articles = articles[:no_of_article]
        formatted_articles = [f"{STOCK_NAME2}: {up_down}{diff_percent}%\nHeadline : {article['title']}. \nBrief : "
                              f"{article['description']}" for article in n_articles]
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        for article in formatted_articles:
            message = client.messages.create(
                body=article,
                from_="+18647322745",
                to=phone_of_user
            )
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email_of_user, msg="Subject:Stock Alert\n\n" + article)
            connection.close()


def google():
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME3,
        "apikey": STOCK_API_KEY
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
    data3 = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data3.items()]
    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]
    day_before_yesterday_data = data_list[1]
    data_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
    difference = float(yesterday_closing_price) - float(data_before_yesterday_closing_price)
    up_down = None
    if difference > 0:
        up_down = "⬆️"
    else:
        up_down = "⬇️"
    diff_percent = round((difference / float(yesterday_closing_price)) * 100)
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME2
    }
    if abs(diff_percent) > percentage:
        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news_response.json()["articles"]
        n_articles = articles[:no_of_article]
        formatted_articles = [f"{STOCK_NAME3}: {up_down}{diff_percent}%\nHeadline : {article['title']}. \nBrief : "
                              f"{article['description']}" for article in n_articles]
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        for article in formatted_articles:
            message = client.messages.create(
                body=article,
                from_="+18647322745",
                to=phone_of_user
            )
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email_of_user, msg="Subject:Stock Alert\n\n" + article)
            connection.close()


def microsoft():
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME4,
        "apikey": STOCK_API_KEY
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
    data4 = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data4.items()]
    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]
    day_before_yesterday_data = data_list[1]
    data_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
    difference = float(yesterday_closing_price) - float(data_before_yesterday_closing_price)
    up_down = None
    if difference > 0:
        up_down = "⬆️"
    else:
        up_down = "⬇️"
    diff_percent = round((difference / float(yesterday_closing_price)) * 100)
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME3
    }
    if abs(diff_percent) > percentage:
        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news_response.json()["articles"]
        n_articles = articles[:no_of_article]
        formatted_articles = [f"{STOCK_NAME4}: {up_down}{diff_percent}%\nHeadline : {article['title']}. \nBrief : "
                              f"{article['description']}" for article in n_articles]
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        for article in formatted_articles:
            message = client.messages.create(
                body=article,
                from_="+18647322745",
                to=phone_of_user
            )
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email_of_user, msg="Subject:Stock Alert\n\n" + article)
            connection.close()


def apple():
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME5,
        "apikey": STOCK_API_KEY
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
    data5 = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data5.items()]
    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]
    day_before_yesterday_data = data_list[1]
    data_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
    difference = float(yesterday_closing_price) - float(data_before_yesterday_closing_price)
    up_down = None
    if difference > 0:
        up_down = "⬆️"
    else:
        up_down = "⬇️"
    diff_percent = round((difference / float(yesterday_closing_price)) * 100)
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME4
    }
    if abs(diff_percent) > percentage:
        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news_response.json()["articles"]
        n_articles = articles[:no_of_article]
        formatted_articles = [f"{STOCK_NAME5}: {up_down}{diff_percent}%\nHeadline : {article['title']}. \nBrief : "
                              f"{article['description']}" for article in n_articles]
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        for article in formatted_articles:
            message = client.messages.create(
                body=article,
                from_="+18647322745",
                to=phone_of_user
            )
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email_of_user, msg="Subject:Stock Alert\n\n" + article)
            connection.close()


def choice():
    def isChecked():
        if v1.get() == 1:
            tesla()
        if v2.get() == 1:
            nokia()
        if v3.get() == 1:
            google()
        if v4.get() == 1:
            microsoft()
        if v5.get() == 1:
            apple()

    canvas.destroy()
    submit_button.destroy()
    name_of_user = name.get()
    label.config(text=f"Dear {name.get()}, please fill in your details to get regular alerts about stock market", bg=BG)
    name.destroy()
    label.place(x=150, y=50)
    email_label = Label(text="EMAIL ID  :", font=FONT, bg=BG)
    email = Entry(font=FONT, width=30)
    email.place(x=300, y=200)
    email_label.place(x=100, y=200)
    phone = Entry(font=FONT)
    phone.place(x=300, y=250)
    phone_no_label = Label(text="PHONE NO. :", font=FONT, bg=BG)
    phone_no_label.place(x=100, y=250)
    country_label = Label(text="Your country :", font=FONT, bg=BG)
    country_label.place(x=100, y=300)
    options = ["Afghanistan", "Australia", "Bangladesh", "Bhutan", "Brazil", "Canada",
               "China", "France", "Germany", "India", "Israel", "Italy", "Japan", "Norway", "Pakistan"]
    clicked = StringVar()
    clicked.set("India", )
    country_code_menu = OptionMenu(window, clicked, *options, )
    country_code_menu.config(font=FONT)
    country_code_menu.place(x=300, y=300)
    global phone_no, phone_of_user
    phone_no = Entry(font=FONT)
    phone_of_user = phone_no.get()
    no_of_articles = Entry(font=FONT)
    no_of_articles.place(x=700, y=350)
    per_alert = Entry(font=FONT)
    per_alert.place(x=700, y=400)
    article_label = Label(text="Number of articles you want to receive *:", font=FONT, bg=BG)
    article_label.place(x=100, y=350)
    per_alert_label = Label(text="% change in the stock prices above which\nyou want to receive alerts and related "
                                 "news *:", font=FONT, bg=BG)
    per_alert_label.place(x=100, y=400)
    canvas1 = Canvas(width=400, height=270)
    image1 = PhotoImage(file="aa.png")
    canvas1.create_image(200, 135, image=image1)
    canvas1.photoimage = image1
    canvas1.place(x=1000, y=450)

    def submit_details():
        global no_of_article, percentage, email_of_user
        if len(email.get()) == 0 and len(phone_no.get()) == 0:
            messagebox.showerror(title="Empty fields", message="You have to fill atleast one out of email and "
                                                               "phone number !")
            if len(email.get()) == 0:
                email.focus()
            else:
                phone_no.focus()
        if len(no_of_articles.get()) == 0 or len(per_alert.get()) == 0:
            messagebox.showerror(title="OOPS !", message="Please do not leave any important field empty")
        if len(no_of_articles.get()) == 0:
            no_of_articles.focus()
        else:
            per_alert.focus()
        if v1 == 0 and v2 == 0 and v3 == 0 and v4 == 0 and v5 == 0:
            messagebox.showerror(title="OOPS !", message="Please select atleast one stock that interests you !")
        no_of_article = int(no_of_articles.get())
        percentage = int(per_alert.get())
        email_of_user = email.get()
        messagebox.showinfo(title="Your details:", message=f"Dear {name_of_user}, these are the details you entered :"
                                                           f"\nEmail :{email_of_user}"
                                                           f"\nPhone number :{phone_of_user}\n"
                                                           f"% change in prices for alert :{percentage}"
                                                           f"\nNumber of news articles you want to receive "
                                                           f":{no_of_article}\n Press OK to continue...")

        isChecked()

    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()
    v5 = IntVar()
    c1 = Checkbutton(window, text="Tesla", variable=v1, onvalue=1, offvalue=0, font=FONT)
    c1.place(x=500, y=600)
    c2 = Checkbutton(window, text="Nokia", variable=v2, onvalue=1, offvalue=0, font=FONT)
    c2.place(x=500, y=550)
    c3 = Checkbutton(window, text="Google", variable=v3, onvalue=1, offvalue=0, font=FONT)
    c3.place(x=500, y=500)
    c4 = Checkbutton(window, text="Microsoft", variable=v4, onvalue=1, offvalue=0, font=FONT)
    c4.place(x=500, y=700)
    c5 = Checkbutton(window, text="Apple", variable=v5, onvalue=1, offvalue=0, font=FONT)
    c5.place(x=500, y=650)
    label2 = Label(text="Please select the stocks\nthat interest you :", font=FONT, bg=BG)
    label2.place(x=100, y=600)
    submit_button1 = Button(text="SUBMIT DETAILS", font=FONT, command=submit_details)
    submit_button1.place(x=1050, y=250)


window = Tk()
window.title("Stock Alert !")
window.config(bg=BG, height=1200, width=1200)
canvas = Canvas(width=1000, height=600, bg=BG, highlightthickness=0)
image = PhotoImage(file="stock_b_660_300321041755.png")
canvas.create_image(300, 300, image=image)
canvas.place(x=150, y=100)
label = Label(text="Please enter your name,\ndear STOCK TRADER :", font=("Calibri", 30, "bold"))
label.place(x=1020, y=100)
name = Entry(font=("Ariel", 30, "bold"))
name.place(x=1000, y=300)
submit_button = Button(text="SUBMIT", command=choice, font=("Ariel", 40, "bold"))
submit_button.place(x=1100, y=500)

window.mainloop()
