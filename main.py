import os
import time

import requests
from bs4 import BeautifulSoup
from requests.structures import CaseInsensitiveDict

checked = 0


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def set_window_title(title):
    if os.name == "nt":
        os.system(f"title {title}")


while True:
    set_window_title(f"Bye Bye Bitcoin // Checked Wallets: {checked} // by clout")

    url = "https://www.bitcoinlist.io/random"
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/99.0.4844.82 Safari/537.36"
    )

    try:
        req = requests.get(url, headers=headers, timeout=20)
        req.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro de conexão: {e}")
        time.sleep(5)
        continue

    soup = BeautifulSoup(req.content, "html.parser")
    wallets = soup.find_all("tr")

    for wallet in wallets:
        getwallet = str(wallet.getText()).strip()

        if not getwallet or "Private Key" in getwallet:
            continue

        parts = getwallet.split()
        if len(parts) < 4:
            continue

        privkey, uncompaddy, compaddy, balance = parts[:4]

        try:
            balance_value = float(balance)
        except ValueError:
            continue

        checked += 1

        if balance_value > 0:
            with open("hits.txt", "a+", encoding="utf-8") as file:
                file.write(
                    f"{balance} BTC found in Adress: {compaddy} // "
                    f"Private Key: {privkey}\n"
                )

        clear_screen()
        set_window_title(f"Bye Bye Bitcoin // Checked Wallets: {checked} // by clout")

        print(f"""
            .-.____________________.-.
     ___ _.' .-----.    _____________|======+--------------------+
    /_._/   (      |   /_____________|      |   Bye Bye Bitcoin  |
      /      `  _ ____/                     |      by clout      |
      |_      .\\( \\                          |____________________|
    .'  `-._/__`_//
  .'       |'           Private Key: {privkey}
 /        /             Uncompressed Address: {uncompaddy}
/        |              Compressed Address: {compaddy}
|        '              Balance: {balance}
|        |
`-._____.-'""")

        time.sleep(0.5)
