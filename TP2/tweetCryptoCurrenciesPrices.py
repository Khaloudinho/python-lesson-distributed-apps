#!/usr/bin/env python
# -*-coding:utf-8-*-

from currencies import *
from conf.twitterCredentials import *
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

    # pas securitaire aucune verification
    targetCurrency = input('\nRenseignez la devise cible uniquement EUR, USD, GBP : \n')

    # Boucle de maniere indefinie
    while True:

        # En 1 requete on obtient le prix de toutes les crypto monnaies de l'API a la date courante
        prices = get_currencies_price(targetCurrency)

        # On veut s'assurer que les cryptos monnaies demandees sont presentes dans l'API et dans la liste des elements desirees
        # On recupere celle qui sont disponibles
        existingAndAskedCurrencies = getExistingCurrenciesCode(prices, askedCurrencies)

        printCurrencies(prices, existingAndAskedCurrencies, targetCurrency)

        currentMessage = listCurrencies(prices, existingAndAskedCurrencies, targetCurrency)+ " #crypto"

        if(changeCourses(previousMessage, currentMessage)):
            # Met a jour notre compte twitter
            api.update_status(currentMessage)
            sendEmail(currentMessage)

        time.sleep(10)

        previousMessage = currentMessage

