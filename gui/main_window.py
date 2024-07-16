import configparser
import time
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
from gui.ui_project import Ui_MainWindow
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from nltk.stem.porter import PorterStemmer
import re
from nltk.corpus import stopwords
import pickle
from twikit import Client
from datetime import datetime

def preprocess_text(text):
    text = remove_emoji(text)
    port_stem = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    # Removing URLS
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)

    # Removing html tags
    text = re.sub(r"<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});", " ", text)

    # Removing the Punctuation
    text = re.sub(r"[^\w\s']", " ", text)

    # Removing words that have numbers
    text = re.sub(r"\w*\d\w*", " ", text)

    # Removing Digits
    text = re.sub(r"[0-9]+", " ", text)

    # Cleaning white spaces
    text = re.sub(r"\s+", " ", text).strip()

    text = text.lower()
    # Check stop words
    tokens = []
    for token in text.split():
        if token not in stop_words and len(token) > 2:
            tokens.append(port_stem.stem(token))
    return " ".join(tokens)

def predict_text(text, model, vectorizer):
    text = preprocess_text(text)
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    return prediction

from langdetect import detect

def is_english(text):
    try:
        language = detect(text)
        return language == 'en'
    except:
        return False

import re
import emoji

def remove_emoji(text):
    return emoji.replace_emoji(text, replace='')

class MainGUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Analiza sentimentelor de pe Twitter")
        self.statisticaButton.clicked.connect(self.swich_to_statisticaPage)
        self.pozitiveButton.clicked.connect(self.swich_to_pozitivePage)
        self.negativeButton.clicked.connect(self.swich_to_negativePage)
        self.setariButton.clicked.connect(self.swich_to_setariPage)
        self.searchButton.clicked.connect(self.search)
        self.salveazaButon.clicked.connect(self.on_save_button_clicked)
        self.model = pickle.load(open("model\\artifacts\\model.sav", 'rb'))
        self.vectorizer = pickle.load(open("model\\artifacts\\vectorizer.pkl", 'rb'))

    def on_save_button_clicked(self):
        username = self.usernameBar.text()
        email = self.emailBar.text()
        password = self.parolaBar.text()
        self.update_config_file(username, email, password)

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def search(self):
        text = self.searchBar.text()
        if len(text) > 0:
            self.get_tweets(text)

    def get_tweets(self, text):
        config = configparser.ConfigParser()
        config.read('gui\\config\\config.ini')

        USERNAME = config['credentials']['username']
        EMAIL = config['credentials']['email']
        PASSWORD = config['credentials']['password']

        client = Client('en-US')
        try:
            client.login(auth_info_1=USERNAME, auth_info_2=EMAIL, password=PASSWORD)
        except:
            self.show_error_message("EROARE LOGARE", "Contul introdus este invalid!")
            return

        while True:
            try:
                tweets = client.search_tweet(text, 'Media', count=200)
                break
            except Exception as e:
                print(str(e))

        numar_de_0 = 0
        numar_de_1 = 0
        lista_pozitive = []
        lista_negative = []

        for tweet in tweets:
            tweetText = remove_emoji(tweet.text)
            tweetText = tweetText.lower()
            tweetText = re.sub(r"https?://\S+|www\.\S+", " ", tweetText)
            tweetText = re.sub(r"<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});", " ", tweetText)
            tweetText = re.sub(r"[^\w\s']", " ", tweetText)
            if is_english(tweetText):
                nr = predict_text(tweetText, self.model, self.vectorizer)[0]
                if nr == 0:
                    numar_de_0 += 1
                    lista_negative.append(tweet)
                else:
                    numar_de_1 += 1
                    lista_pozitive.append(tweet)
        self.setupChart(self.statisticaPage, text, numar_de_1, numar_de_0)
        self.setupList(self.pozitivePage, lista_pozitive)
        self.setupList(self.negativePage, lista_negative)

    def update_config_file(self, username, email, password, filename='gui\\config\\config.ini'):
        config = configparser.ConfigParser()
        config['credentials'] = {
            'username': username,
            'email': email,
            'password': password
        }
        with open(filename, 'w') as configfile:
            config.write(configfile)

    def setupList(self, parentWidget, tweets_list):
        layout = parentWidget.layout()
        if layout is not None:
            self.clearLayout(layout)
        else:
            layout = QtWidgets.QVBoxLayout(parentWidget)
        # Crearea unui QScrollArea
        scroll_area = QtWidgets.QScrollArea(parentWidget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("border: none;")

        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        container = QtWidgets.QWidget()
        vbox = QtWidgets.QVBoxLayout(container)

        label_style = """
            QLabel {
                background-color: rgb(31, 29, 51);
                color: white;
                border-radius: 10px;
                padding: 8px;
                margin: 5px;
                word-wrap: true;
                 font-size: 14pt;
            }
        """

        for tweet in tweets_list:
            formatted_date = datetime.strptime(tweet.created_at, '%a %b %d %H:%M:%S %z %Y').strftime('%d.%m.%Y %H:%M:%S')
            label = QtWidgets.QLabel("@" + tweet.user.name + "   " + formatted_date + "\n\n" + tweet.text)
            label.setStyleSheet(label_style)
            label.setWordWrap(True)
            label.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
            vbox.addWidget(label)
        scroll_area.setWidget(container)
        layout.addWidget(scroll_area)

    def setupChart(self, parentWidget, termen_cautat, t_pozitive, t_negative):
        main_layout = parentWidget.layout()
        if main_layout is not None:
            self.clearLayout(main_layout)
        else:
            main_layout = QtWidgets.QHBoxLayout(parentWidget)

        fig = Figure(facecolor='none', frameon=False)
        ax = fig.add_subplot(111)
        data = [t_negative, t_pozitive]
        labels = ['Negativ', 'Pozitiv']
        colors = ['red', 'green']
        textprops = {"color": "white"}
        ax.pie(data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, textprops=textprops)
        ax.axis('equal')

        canvas = FigureCanvas(fig)
        canvas.setStyleSheet("background-color:transparent;")
        main_layout.addWidget(canvas)

        text_widget = QtWidgets.QWidget()
        text_layout = QtWidgets.QVBoxLayout(text_widget)
        text_widget.setStyleSheet("""
            QWidget {
                background-color: rgb(31, 29, 51);
                border-radius: 15px;
                padding: 15px;
                margin: 10px;
            }
        """)

        label_style = "color: white; font-size: 14pt;"

        term_label = QtWidgets.QLabel(f"Termen căutat: \n{termen_cautat}")
        term_label.setStyleSheet(label_style)
        term_label.setAlignment(QtCore.Qt.AlignCenter)
        text_layout.addWidget(term_label)

        poz_label = QtWidgets.QLabel(f"Tweeturi pozitive: \n{t_pozitive}")
        poz_label.setStyleSheet(label_style)
        poz_label.setAlignment(QtCore.Qt.AlignCenter)
        text_layout.addWidget(poz_label)

        neg_label = QtWidgets.QLabel(f"Tweeturi negative: \n{t_negative}")
        neg_label.setStyleSheet(label_style)
        neg_label.setAlignment(QtCore.Qt.AlignCenter)
        text_layout.addWidget(neg_label)

        main_layout.addWidget(text_widget)
        parentWidget.setLayout(main_layout)

    def swich_to_statisticaPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def swich_to_pozitivePage(self):
        self.stackedWidget.setCurrentIndex(1)

    def swich_to_negativePage(self):
        self.stackedWidget.setCurrentIndex(2)

    def swich_to_setariPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def show_error_message(self, titlu, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle(titlu)
        error_dialog.setInformativeText(message)
        error_dialog.exec_()