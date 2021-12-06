# 1 - CREER DES CLES D'API SUR BINANCE

Voir : https://www.binance.com/fr/support/faq/360002502072

Vous mettez _jamais_ withdrawal comme droit sur vos API, d'accord ?

Puis récupérer la clé et l'API secret (copiez-les quelque part en attendant de faire les autres manips)

# 2 - MODIFIER LE FICHIER `connect.py`

Plus particulièrement les lignes :

```
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY", ">>ICI_API_KEY<<")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET", ">>ICI_API_SECRET<<")
```

Ou vous collez les informations de l'API Binance

Ces informations permettent de se connecter à l'API binance, pour :

- configurer le mode de levier et le facteur,
- Obtenir les données brutes des cours pour faire un calcul sommaire des résistances,
- plein d'autres trucs ...

# 3 - MODIFIER LE FICHIER `telegram.py`

Plus compliqué, il vous créer une API sur télégram pour se connecter directement au channel:

- suivez les instructions sur : https://core.telegram.org/api/obtaining_api_id
- en gros, vous devez rentrer votre numéro de tel, puis vous recevrez un code pour passer au menu de config de telegram

- connectez vous à : https://my.telegram.org/ , puis choisissez "API development tools"
- une fois connecté, un lien devrait vous mener vers les données de l'API telegram
- créez votre API
- meme manip que sur Binance, vous mettez de coté les champs **App api_hash** et **App api_id** : il vont vous servir à vous connecter automatiquement à Telegram et récupérer les messages

- remplir les valeurs ici, dans `telegram.py` :

```

TELEGRAM_API_HASH = ">>ici le API hash récupéré<<"
TELEGRAM_API_ID = 000000 # ici_un_entier_sans_guillemets
TELEGRAM_SCALP_SHORT_ID = 00000000 # demande dans le chan ...

```

# 4 - PREPARER ET LANCER LE PROGRAMME

Il y a deux scripts d'install dans ce repertoire mais en gros:
d'install dans ce repertoire mais en gros:

- il faut que Python 3 soit installé
- il faut que les librairies necessaires soient installés

Pour Python 3 sous windows, je ne sais pas trop: mais je suppose
que commencer par : https://docs.python.org/3/using/windows.html peut-être une bonne idée...

Ouvrez un terminal, puis dans le répertoire 'helper-scalper' :

```
pip install -r requirements.txt
```

pour installer les libs listées dans le fichier `requirements.txt`.

puis

```
python telegram.py

```

pour lancer programme.

Enjoy !

Utilisez les issues (https://github.com/ikarius/helper-scalper/issues) plutot que de polluer le chan, merci !
