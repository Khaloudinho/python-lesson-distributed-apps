#!/usr/bin/env python
# -*-coding:utf-8-*-

from __future__ import absolute_import, print_function

import urllib.request
from json import loads

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from conf.mailCredentials import *


API_PATH='https://api.coinmarketcap.com/v1/ticker/?limit=2000&convert='

# E/S utilisateurs
# Demander de rentrer des codes devises a l'utilisateur
def askCurrencies():
    """
        Ask currencies to user

        :return askedCurrencies (list) : list of currencies which are asked
    """
    userInputMessage = "(les codes devises faux seront ignores)\nEntrez les codes des differentes devises:\n"
    userInput = input(userInputMessage).split()

    while len(userInput)>12:
        print("\n/!\Vous ne DEVEZ PAS fournir plus de 12 codes devises/!\ (twitter limite un post a 144 caracteres)\n")
        userInput = input(userInputMessage).split()

    askedCurrencies = [str(x) for x in userInput]

    print("Choix: " + str(askedCurrencies))
    return askedCurrencies

# API
# Interagir avec l'API coinmarketcap
def get_currencies_price(targetCurrency):
    """
        Call api and convert json to object

        :return json (object) : object representation of obtained json about currencies
    """
    req = urllib.request.urlopen(API_PATH+targetCurrency)
    return loads(req.read())

# Permet d'eviter les erreurs lies a des suppresion de crypto monnaies dans l'API coinmarketcap
def getExistingCurrenciesCode(json, askedCurrencies):
    """
        Determine if askedCurrencies are supported by the used API

        :param json (object) : representation of obtained currencies
        :param askedCurrencies (list) : list of asked currencies by code (EUR, USD, ..)

        :return existingAndAskedCurrencies (list) : list of currencies which are
    """
    currencies = []
    for currency in json:
        currencies.append(currency['symbol'])
    existingAndAskedCurrencies = set(currencies).intersection(set(askedCurrencies))
    unExistingCurrencies = set(existingAndAskedCurrencies) ^ set(askedCurrencies)
    print("Inexistantes au sein de l'API :" + str(unExistingCurrencies))
    return existingAndAskedCurrencies


# Obtenir la valeur d'une crypto monnaie selon son code identificateur BTC ==> bitcoin
def getCurrencyById(json, currencyCode, targetCurrency):
    """
        Get the value of a specific currency

        :param json (object) : json object representation of obtained json
        :param currencyCode (str) : currency code (EUR, USD, ..)

        :return currency_price (str)
    """
    # Filtrer par le code devise
    for x in json:
        if x['symbol'] == currencyCode:
            currency_price = str(round(float(x['price_'+targetCurrency.lower()]), 2))
            return currency_price

# Generation du message
def listCurrencies(json, selectedCurrencies, targetCurrency):
    """
        Constructs the message content

        :param json (object) : object representation of json
        :param selectedCurrencies (list) : retained currencies

        :return currenciesMessage (str) : change currencies ?
    """
    currenciesMessage = "["+targetCurrency+"]\n"
    for currencyCode in selectedCurrencies:
        currenciesMessage += currencyCode + ": "+getCurrencyById(json, currencyCode, targetCurrency)+'\n'
    return currenciesMessage

# Affichage en ligne de commande
def printCurrencies(prices, avaiableCurrencies, targetCurrency):
    """
        Debug method which displays currencies courses

        :param prices (list) : list of currencies's price
        :param avaiableCurrencies (list) : retained currencies
    """
    print("***prices***\n" + listCurrencies(prices, avaiableCurrencies, targetCurrency) +"***prices***\n")

# Twitter
# Detecter si le message twitter est le meme que le precedent pou eviter tout bug avec l'API twitter a ce sujet
def changeCourses(previousMessage, currentMessage):
    """
        Determine if one of observed currency has changed..

        :param previousMessage (str) : previous message for twitter
        :param currentMessage (str) : current message for twitter

        :return change (bool) : change currencies ?
    """
    return bool(previousMessage!=currentMessage)

# Envoi de mail
def sendEmail(currentMessage):

    msg = MIMEMultipart()
    msg['From'] = EXPEDITEUR
    msg['To'] = DESTINATAIRE
    msg['Subject'] = "Crypto courses TP2"
    body = currentMessage
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(EXPEDITEUR, MY_PASSWORD)
    except:
        print(MAIL_AUTHENTIFICATION_ERROR)

    text = msg.as_string()

    try:
        server.sendmail(EXPEDITEUR, DESTINATAIRE, text)
    except:
        print(MAIL_SEND_ERROR)

    server.quit()
