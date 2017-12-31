# TP2 : monitoring de crypto-monnaies

But 

* avoir un programme qui twitte en temps réel les cours de plusieurs crypto-monnaies

Note : 

* si vous décidez de suivre le process nous n'allons pas faire *d'objet* mais plutôt du *scripting*
* l'idée est de se rendre compte des limites de cette manière de procéder


## 0 - prérequis

Avoir installé `tweepy` et disposé de Python 3

Etre au sein d'un projet python vide

## 1 - paramétrer twitter

Nous vous suggérons de vous reporter à la vidéo dans **aide/parametrage-twitter.mp4**

1. créer un compte twitter
2. ajouter une api
3. ajouter un fichier `twitterCredentials.py` par exemple
    
```bash
    #!/usr/bin/env python
    # -*-coding:utf-8-*-

    consumer_key = 'y8v3XvOvTfAWDpWXKuQjJZNXk'
    consumer_secret = 'tZYDSQspqZqxFiSt2rube0s4ZiKzMBqwfHiU8KBnm1nj0oo8uS'
    access_token = '904064854314684416-dMvQlnWgqwPd3tNfvA0NBJrFzcLALYD'
    access_token_secret = 'TPiKJyCxzOitVCBsr6JJp6EpTknRVpOEmccHy2p90JsVP'
```
      
## 2 - réaliser notre projet

créons 2 fichiers 

1. `tweetCryptoCurrenciesPrices.py` 
    * notre fichier lanceur (comme un main en java)
2. `currencies.py`
    * notre fichier contenant nos méthodes métiers

### 2.1 - imports

### 2.1.1 `tweetCryptoCurrenciesPrices.py`

Nous avons besoin pour travailler

* de tweepy pour intéragir avec notre compte twitter
* de time pour faire des pauses dans notre algorithme
* d'utiliser les méthodes définies dans `currencies.py`

```python
    #!/usr/bin/env python
    # -*-coding:utf-8-*-

    from currencies import *
    from twitterCredentials import *
    import tweepy
    import time
```

### 2.1.2 `currencies.py`

Nous avons besoin pour travailler

* de requêter d'où urllib
* de manipuler du json d'où json

```python
    #!/usr/bin/env python
    # -*-coding:utf-8-*-

    from __future__ import absolute_import, print_function

    import urllib.request
    from json import loads
```

### 2.2 - API

Dans `currencies.py` :


Nous utiliserons l'API de coinmarketcap

rajouter au fichier : 

```python
    API_PATH='https://api.coinmarketcap.com/v1/ticker/?limit=2000&convert=EUR'
```

### 2.2 - méthodes utiles

Nous allons définir les différentes méthodes utiles dans `currencies.py`.

`currencies.py` regroupe toutes les méthodes métiers (qui sont relativement peu nombreuses), ce choix peut être discuté et on peut tout à fait faire un autre découpage du projet (E/S user, notifications, extraction data)

nous avons les besoins métiers suivants 

1. l'utilisateur doit pourvoir s'informer sur plusieurs devises (E/S clavier)
2. nous devons aller chercher les données en temps réel (API)
3. nous devons twitter les résultats et les afficher dans la console de la machine qui execute le script
4. nous devons gérer les problématiques de devises inexistantes

1/ 

Dans `tweetCryptoCurrenciesPrices.py` on ajoute :

```python
    if __name__ == '__main__':
    """
        Methode principale
    """
    # Methode qui demande a l'utilisatur les devises
    askedCurrencies = askCurrencies()
```

Dans `currencies.py` on ajoute :

```python
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
```

2/ comme nous savons que nous avons un nombre limité d'interactions avec l'API de coinmarketcap (**no more than 10 per minute.**)

Nous essayerons donc dans la mesure du possible de limiter notre utilisation et d'effectuer une pause de 60 secondes dans nos scripts ou d'utiliser une connexion avec une ip tierce (4G, VPN (voir VPNgate.com) etc..)

Remarque :

* Nous operons 1 seule requête, au lieu de N requêtes pour N devises car l'API nous le permet..

Dans `tweetCryptoCurrenciesPrics.py` on ajoute dans le `if __name__ == '__main__':` :

```python
    # Boucle de maniere indefinie
    while True:
        # En 1 requete on obtient le prix de toutes les crypto monnaies de l'API a la date courante
        prices = get_currencies_price()
        
        time.sleep(10)

```

Dans `currencies.py` on ajoute :

```python
    # API
    # Interagir avec l'API coinmarketcap
    def get_currencies_price():
        """
            Call api and convert json to object
    
            :return json (object) : object representation of obtained json about currencies
        """
        req = urllib.request.urlopen(API_PATH)
        return loads(req.read())
```

Nous allons ensuite gérer le cas soulevé dans 4 `get_currencies_price()`

Dans `tweetCryptoCurrenciesPrics.py` on ajoute à la suite dans le `while True:`  :

```python
    # On veut s'assurer que les cryptos monnaies demandees sont presentes dans l'API et dans la liste des elements desirees
    # On recupere celle qui sont disponibles
    existingAndAskedCurrencies = getExistingCurrenciesCode(prices, askedCurrencies)

```

Dans `currencies.py` on ajoute :

```python
    # Permet d'eviter les erreurs lies a des suppresion de crypto monnaies dans l'API coinmarketcap
    def getExistingCurrenciesCode(json, askedCurrencies):
        """
            Determine if askedCurrencies are supported by the used API
    
            :param json (object) : representation of obtained currencies
            :param askedCurrencies (list) : list of asked currencies by code (EUR, USD, ..)
    
            :return existingAndAskedCurrencies (list) : list of currencies which are
        """
        # Construction d'une liste de currencies existantes
        currencies = []
        for currency in json:
            currencies.append(currency['symbol'])
        
        # devises exploitables par notre programme
        existingAndAskedCurrencies = set(currencies).intersection(set(askedCurrencies))
        
        # difference entre 2 set
        unExistingCurrencies = set(existingAndAskedCurrencies) ^ set(askedCurrencies)
        print("Inexistantes au sein de l'API :" + str(unExistingCurrencies))
        return existingAndAskedCurrencies
    
```

Actuellement nous avons réussi à 

* a gérer les demandes utilisateurs
* nous connecter à l'API
* à récupérer les cours des devises

Remarque :

* on aurait très bien pu utiliser  `Argparse` comme moyen de gestion des demandes utilisateur.


Nous devons donc (lorsqu'on boucle) :

1. afficher dans la ligne de commande les valeurs des devises
2. poster le message sur twitter

0/ 

nous utiliserons une méthode commune pour lister les valeurs des devises :

Dans `currencies.py` on ajoute :
```python
    # Obtenir la valeur d'une crypto monnaie selon son code identificateur BTC ==> bitcoin
    def getCurrencyById(json, currencyCode):
        """
            Get the value of a specific currency
    
            :param json (object) : json object representation of obtained json
            :param currencyCode (str) : currency code (EUR, USD, ..)
    
            :return currency_price (str)
        """
        # Filtrer par le code devise
        for x in json:
            if x['symbol'] == currencyCode:
                currency_price = str(round(float(x['price_eur']), 2))
                return currency_price
```

et

```python
    # Generation du message
    def listCurrencies(json, selectedCurrencies):
        """
            Constructs the message content
    
            :param json (object) : object representation of json
            :param selectedCurrencies (list) : retained currencies
    
            :return currenciesMessage (str) : change currencies ?
        """
        currenciesMessage = "[EUR]\n"
        for currencyCode in selectedCurrencies:
            currenciesMessage += currencyCode + ": "+getCurrencyById(json, currencyCode)+'\n'
        return currenciesMessage
```


1/ 

Pour afficher en ligne de commande nous faisons un simple print 

Soit dans `tweetCryptoCurrenciesPrics.py` (toujours dans la boucle) :

```python
   printCurrencies(prices, existingAndAskedCurrencies)
```


Soit dans `currencies.py` :

```python
    # Affichage en ligne de commande
    def printCurrencies(prices, avaiableCurrencies):
        """
            Debug method which displays currencies courses
    
            :param prices (list) : list of currencies's price
            :param avaiableCurrencies (list) : retained currencies
        """
        print("***prices***\n" + listCurrencies(prices, avaiableCurrencies) +"***prices***\n")
```

2/ Pour envoyer le message sur twitter 

Nous devons nous authentifier initialement :

Dans `tweetCryptoCurrenciesPrics.py` (juste après les imports et avant la boucle) on ajoute :

```python
    # Nous nous authentifions
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    # Affiche notre idendite
    print(api.me().name)
```

Nous devons vérifier si un des cours à changé (pour éviter les status dupliqués): 

Dans `currencies.py` on ajoute :
```python
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
```

Nous devons poster sur twitter :

Dans `tweetCryptoCurrenciesPrics.py` on ajoute :

avant la boucle :
```python
    previousMessage = ""
```

dans la boucle on modifie tel que :
```python
    if(changeCourses(previousMessage, currentMessage)):
        # Met a jour notre compte twitter
        api.update_status(currentMessage)
    
    time.sleep(10)
    
    previousMessage = currentMessage
```

## 3 - conclusion

On voit qu'il est relativement simple 

* d'intéragir avec twitter (via `tweepy`)
* que la gestion des E/S a la main est un peu lourde
* que la manipulation des données provenant de l'api est un peu plus délicate
    * on aurait pu utiliser des dataframes etc..

qu'est ce qu'on pourrait améliorer ?

* passer sur de l'objet
* éviter l'implémentation de contraintes en dur (144 caractères d'un tweet)
* permettre la généricite (mail, fb, google etc..)
* utilisations de générateur etc
* refractorer certaines méthodes et repenser le process
* etc. 