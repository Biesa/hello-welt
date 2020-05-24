#Mpodstawowe menu gry
while True:
        print("Witaj w Blackjacku!\nAby zagrać w grę - wybierz 1.\nAby poznać zasady gry - wybierz 2.\nAby zakończyć program - wybierz 3.")
        wybór= str(input())
        if wybór== "1":
            print("Zaczynamy! Będę Twoim Kurpierem :).\nCzy znasz zasady?")
            znajomość_zasaad=str(input())
            if znajomość_zasaad=="tak":
                print("Wspaniale. Przejdźmy do gry.")
                print("Rozdaję karty.") #tutaj 1 funkcja wylosowania 2 kart dla kurpiera (jedna jest niewiadoma dla gracza) i 2 odkryte karty dla gracza.
            elif znajomość_zasaad=="nie":
                print("\nPUNKTACJA KART:\nKarty od dwójki do dziesiątki mają wartość równą numerowi karty.\nWalet, Dama i Król mają wartość równą 10 punktów.\nAs ma wartość równą 1 lub 11, w zależności co jest lepsze dla gracza.")
                print("\nMOŻLIWOŚCI RUCHU:\nDobrać kartę (hit)\nNie dobierać kart (stand)\nPodwoić stawkę (double down)\nRozdwoić karty (split)")
            break
        elif wybór== "2":
            print("Celem gry jest pokonać krupiera poprzez uzyskanie sumy jak najbliższej 21 punktów w kartach jednak nie przekraczając 21. Gracz stawia zakład na specjalnym stole używając żetonów. Następnie gracz i krupier dostają po dwie karty. Obydwie karty gracza są odkryte, natomiast tylko jedna karta krupiera jest pokazana graczowi")
            break
        elif wybór=="3":
            print("Może następnym razem. Do zobaczenia!")
            break
        else:
            print("Aby zagrać w grę - wybierz 1.\nAby poznać zasady gry - wybierz 2.\nAby zakończyć program - wybierz 3.")
            wybór=str(input())

#talia z 52 kart
# Numery i kolory kart są zakodowane (mapowane) w dwóch listach.


#tasowanie talii

#tworzenie "ręki"

#dobieranie nKarty HIT

#nie dobieranie karty STNAD

#Podwojenie stawki DOUBLE DOWN

#rozdwojenie karty SPLIT
