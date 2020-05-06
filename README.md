#Automat sprzedający napoje

##Opis zadania
  * Automat przechowuje informacje o monetach znajdujących się w nim (1, 2, 5,
    10, 20, 50gr, 1, 2, 5zł)
  * Automat przechowuje informacje o towarach znajdujących się w nim (przedmioty o
    numerach od 30 do 50), każdy o określonej cenie w określonej liczbie (domyślnie
    po 5 sztuk każdego towaru)
  * Okno z przyciskami pozwalającymi na wrzucanie monet, polem wyświetlającym
    kwotę wrzuconych monet, przyciskiem przerywającym transakcję (wyrzuca
    wrzucone monety), przyciskami 0-9 pozwalającymi wpisać numer wybranego
    towaru oraz polem wyświetlającym wpisany numer towaru.
  * Po wybraniu poprawnego numeru towaru:
    + Jeśli wrzucono za mało monet, wyskakuje okno z informacją o cenie towaru
      oraz (jeśli towar się skończył) o jego braku w automacie.
    + Jeśli wrzucono monety, których wartość jest większa lub równa cenie wybranego
      towaru, automat sprawdza czy towar jest dostępny i czy może wydać resztę
        - Brak towaru: wyskakuje okienko z informacją o braku w automacie.
        - Brak reszty/może wydać: wyskakuje okienko z informacją o
          zakupach, wydaje resztę (dolicza wrzucone monety, odlicza wydane
          jako reszta, odlicza wydany towar), odejmuje towar.
        - Nie może wydać: wyskakuje okienko z napisem "Tylko odliczona kwota".
   
##Testy
1. Sprawdzenie ceny jednego towaru - oczekiwana informacja o cenie.
2. Wrzucenie odliczonej kwoty, zakup towaru - oczekiwany brak reszty.
3. Wrzucenie większej kwoty, zakup towaru - oczekiwana reszta.
4. Wykupienie całego asortymentu, próba zakupu po wyczerpaniu towaru -
   oczekiwana informacja o braku.
5. Sprawdzenie ceny towaru o nieprawidłowym numerze (<30 lub >50) -
   oczekiwana informacja o błędzie.
6. Wrzucenie kilku monet, przerwanie transakcji - oczekiwany zwrot monet.
7. Wrzucenie za małej kwoty, wybranie poprawnego numeru towaru, wrzucenie
   reszty monet do odliczonej kwoty, ponowne wybranie poprawnego numeru towaru
   - oczekiwany brak reszty.
8. Zakup towaru płacąc po 1 gr - suma stu monet ma być równa 1zł (dla floatów
   suma sto razy 0.01+0.01+...+0.01 nie będzie równa 1.0). Płatności można dokonać
   za pomocą pętli for w interpreterze.

[Project Repository](../blob/master)