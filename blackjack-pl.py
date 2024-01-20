import random

#Ogólna talia do gry
def talia():
    wartosci = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    rodzaje = ['♠', '♥', '♣', '♦']
    nowa_talia = [{'Wartość karty': x, 'Rodzaj': y} for x in wartosci for y in rodzaje]
    random.shuffle(nowa_talia)
    return nowa_talia

#Wartości danych kart
def wartosc_karty(x):
    wartosci = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}
    return wartosci[x]

#Sumowanie wartości kart + zachowanie się w momencie wylosowania Asa
def sumuj(uczestnik):
    return sum(wartosc_karty(karta['Wartość karty']) for karta in uczestnik) + 10 if 'A' in [karta['Wartość karty'] for karta in uczestnik] and sum(wartosc_karty(karta['Wartość karty']) for karta in uczestnik) <= 11 else sum(wartosc_karty(karta['Wartość karty']) for karta in uczestnik)

#Dobieranie kart przez gracza
def dobierz(gtalia, gracz):
    karta = gtalia.pop()
    gracz.append(karta)
    print('\nDobieram kartę...\n')

#Dobieranie kart przez krupiera 
def dobierz_krupiera(gtalia, krupier):
    while sumuj(krupier) < 17:
        karta = gtalia.pop()
        krupier.append(karta)

#Wynik remisowy gry
def remis(gracz, krupier):
    return sumuj(gracz) == sumuj(krupier)
     
#"Interfejs graficzny" gry w postaci wydruków
def interfejs(gracz, krupier, pokaz_karty=False):
    print('\nTwoja talia:', gracz, '\nSuma punktów:', sumuj(gracz))
    if pokaz_karty:
        print('\nTalia krupiera:', krupier, '\nSuma punktów:', sumuj(krupier))
    else:
        print('\nTalia krupiera:', [krupier[0], 'X'])

#Możliwość zagrania ponownie
def kontynuacja():
    return input('Zagrać ponownie? (Y/N)\n').strip().lower() == 'y'

#"Głowica" - główna część gry
def root():
    #Tworzenie talii graczy
    while True:
        #Pierwsze rozdanie
        gtalia = talia()
        gracz = [gtalia.pop(), gtalia.pop()]
        krupier = [gtalia.pop(), gtalia.pop()]
        #Głowica gry
        while True:
            if sumuj(gracz) == 21:
                interfejs(gracz, krupier, pokaz_karty=True)
                print('\nBlackjack! Osiągasz 21 punktów. Wygrywasz.')
                break
            interfejs(gracz, krupier)
            #Dostępne akcje/wybory dla gracza
            wybor = input('\nDobrać kartę? (Y/N)\n').upper()
            #Dobieranie
            if wybor == 'Y':
                dobierz(gtalia, gracz)
                if sumuj(gracz) > 21:
                    interfejs(gracz, krupier, pokaz_karty=True)
                    print('\nSuma twoich punktów przekroczyła 21. Krupier wygrywa.')
                    break
            #Pasowanie
            elif wybor == 'N':
                dobierz_krupiera(gtalia, krupier)
                interfejs(gracz, krupier, pokaz_karty=True)
                if remis(gracz, krupier):
                    print('\nRemis. Twoja suma punktów jest równa sumie punktów krupiera.')
                else:
                    zwyciezca = '\nGracz' if sumuj(gracz) > sumuj(krupier) or sumuj(krupier) > 21 else '\nKrupier'
                    print(zwyciezca, 'wygrywa.')
                break
            else:
                #"Grzeczne" uwzględnienie literówki
                print('\nNiepoprawna wartość. Spróbuj ponownie.\n')
        #Zakończenie pętli (gry) jeżeli gracz nie wyrazi woli
        if not kontynuacja():
            break

if __name__ == '__main__':
    root()