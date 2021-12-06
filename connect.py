import os
import ccxt
import pandas as pd

# longXscanner has ID -1001595033443
# shortXscanner has ID -1001495341425
# Somstradamus : VIP Scalping has ID -1001559747350

# Quelques ref utiles :
# https://github.com/ccxt/ccxt/blob/master/examples/py/binance-futures-margin.py

# Après avoir effectué la manip pour recupérer les credentials d'API
# les mettre en dessous ">>ICI...<<" (remplacez tout le texe entre guillemets hein)

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY", ">>ICI_API_KEY<<")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET", ">>ICI_API_SECRET<<")

UT_VERY_LONG = "1M"
UT_LONG = "1w"
UT_MEDIUM = "1d"
UT_SHORT = "1m"

PERIOD = 104

binance = ccxt.binance(
    {
        "apiKey": BINANCE_API_KEY,
        "secret": BINANCE_API_SECRET,
        "options": {"defaultType": "future"},
    }
)

markets = binance.load_markets()


def get_resistances(pair: str, limit: int = PERIOD, nb: int = 5):
    ohlcv_very_long = binance.fetch_ohlcv(pair, UT_VERY_LONG, limit=limit + 1)
    df_very_long = pd.DataFrame(ohlcv_very_long)

    ohlcv_long = binance.fetch_ohlcv(pair, UT_LONG, limit=limit + 1)
    df_long = pd.DataFrame(ohlcv_long)

    ohlcv_medium = binance.fetch_ohlcv(pair, UT_MEDIUM, limit=limit + 1)
    df_medium = pd.DataFrame(ohlcv_medium)

    # TIP: ne pas faire 2 calls, le close de la derniere ligne est le ticker
    # et on utilise le call le + recent
    ticker = df_medium[-1:][4]

    # On prends les *clotures*, sans la derniere ligne qui est le prix actuel
    s_very_long = df_very_long[4][:limit]
    s_long = df_long[4][:limit]
    s_medium = df_medium[4][:limit]

    # On concatene les series et on les trie
    s_all = s_medium.append(s_long).append(s_very_long)

    result = s_all.where(s_all > float(ticker)).sort_values()[:nb]
    return float(ticker), result


def set_leverage_mode(pair: str, leverage: int = 5):
    try:
        binance.set_margin_mode("ISOLATED", pair)
    except Exception:
        print("ERR: modification du mode de levier (déjà ISOLATED ?)")
    try:
        binance.set_leverage(leverage, pair)
    except Exception:
        print(f"ERR: modification du facteur de levier (déjà x{leverage} ?)")


######################################################


def scalp_helper(pair: str):
    # Je suis gentil je permet d'aller plus vite manuellement
    if not pair.endswith("USDT"):
        pair = pair.upper() + "USDT"

    print(f"🤖 SCALP ORDER - PAIR: {pair}")
    print(f"https://www.binance.com/en/futures/{pair}")
    print("Modification mode de levier et facteur ...")
    set_leverage_mode(pair)

    ticker, resistances = get_resistances(pair)
    r1 = float(resistances.array[0])

    if pd.isnull(r1):
        print(f"ERR: Pas de résistance trouvée, PRICE: {ticker}")
        return

    print(f"Ticker : {ticker}")

    # Affiche les 5 premieres résistances :
    print("Résistances: ")
    for r in resistances.array:
        print(f"R : {r}")
