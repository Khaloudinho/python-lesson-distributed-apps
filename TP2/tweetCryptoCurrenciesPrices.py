#!/usr/bin/env python
# -*-coding:utf-8-*-

from currencies import *
from twitterCredentials import *
import tweepy
import time

# Nous nous authentifions
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Affiche notre idendite
print(api.me().name)


if __name__ == '__main__':
    """
        Methode principale
    """
    askedCurrencies = askCurrencies()

    previousMessage = ""

    # Boucle de maniere indefinie
    while True:

        # En 1 requete on obtient le prix de toutes les crypto monnaies de l'API a la date courante
        prices = get_currencies_price()

        # On veut s'assurer que les cryptos monnaies demandees sont presentes dans l'API et dans la liste des elements desirees
        # On recupere celle qui sont disponibles
        existingAndAskedCurrencies = getExistingCurrenciesCode(prices, askedCurrencies)

        printCurrencies(prices, existingAndAskedCurrencies)

        currentMessage = listCurrencies(prices, existingAndAskedCurrencies)+ " #crypto"

        if(changeCourses(previousMessage, currentMessage)):
            # Met a jour notre compte twitter
            api.update_status(currentMessage)


        time.sleep(10)

        previousMessage = currentMessage

