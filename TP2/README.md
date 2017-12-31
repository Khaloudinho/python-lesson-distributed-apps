# 1 - prérequis 

## 1.1 - avoir Python 3 et pip3

Remarque : pip3 est normallement installé d'office avec Python3 

```bash
    https://www.python.org/downloads/
    https://pip.pypa.io/en/stable/installing/
```

## 1.2 - installer le module Tweepy

```bash
    pip3 install tweepy
```

# 2 - twitterbot - fonctionnement

(voir la vidéo fournie twitter-bot.mp4)

Etapes

1. Créer un compte twitter
2. Créer une application 
3. Renseigner les bons identifiants dans `credentials.py`
4. Executer la commande suivante

```bash
    python3 tweetCryptoCurrenciesPrices.py 
```

Dans le programme le tweet (si un des cours a changé) a lieu toutes les 10 secondes.

Utilisation 

- l'utlisateur a renseigné ses identifiants twitter dans credentials.py`
- l'utilisateur renseigne les crypto monnaies qu'il désire étudier
- les données utilisées proviennent de l'API de coinmarketcap.com.  
