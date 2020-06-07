# Automat sprzedający napoje - raport

### Założenia projektowe
Jako środowisko wybrałem PyCharm od JetBrains, ponieważ jest to bardzo podobne środowisko do IntellIJ, 
z którym jestem zaznajomiony.
Do rysowania okienek użyłem polecanej biblioteki tkinter. Uznałem, że jest ona właściwa dla typu aplikacji, 
jaką zamierzam stworzyć. Zastanawiałem się nad dość popularnym PyGame, ale jako że nie miałem jeszcze okazji 
pracować z żadną z wspomnianych bibliotek, wybór padł na mniej zaawansowaną, czyli tkinter.

### Ogólny opis kodu
Kod podzieliłem na dwie głowne klasy odpowiadające za logikę i interfejs, umieszczone w dwóch 
różnych modułach. Dodatkowo mniejszy moduł "exeptions" w którym zdefiniowałem przydatne klasy wyjątków, 
oraz moduł "utils", w którym umieściłem klasy Coin i Wallet odpowiadające za prawidłowe działanie, 
przechowywanie i reprezentacje pieniędzy potrzebnych do działania automatu.

### Co udało się zrobić i z czym były problemy
Wszystkie założenia projektu zostały zrealizowane, największym problemem okazał się standard języka 
Python, który nie zakłada tworzenia osobnego pliku na prawie każdą klasę, tak jak w językach, 
do których jestem przyzwyczajony i z których najczęściej korzystam.
Oprócz tego lekko problematyczne okazało się połączenie interfejsu z logiką, tak aby zachować 
wyraźny podział która część kodu jest odpowiedzialna za co.
   
### Zauważone problemy z testami
Podczas pisania testów nie zauważyłem żadnego niepożądanego zachowania programu, ale nie do 
końca wiedziałem jak dokładnie testy mają wyglądać. Myślę że wszystkie testy zostały napisane 
prawidłowo i dobrze obrazują działanie mojej aplikacji. W niektórych miejscach musiałem umieścić 
część kodu z interfejsu, takiego jak obsługa wyjątków, ponieważ całe testy były przeprowadzana na 
samej logice, bez użycia funkcji z interfejsu. Na interfejsie przeprowadziłem je ręcznie, i też 
nie wykazały żadnych błędów

[Lambda 1](https://github.com/macpor9/projektJS/blob/1e46b5ce38ec61adf17ea977a79929d1c32bf36e/interface.py#L66)\
[Lambda 2](https://github.com/macpor9/projektJS/blob/1e46b5ce38ec61adf17ea977a79929d1c32bf36e/interface.py#L67)\
[Lambda 3](https://github.com/macpor9/projektJS/blob/1e46b5ce38ec61adf17ea977a79929d1c32bf36e/interface.py#L68)\
[Lambda 4](https://github.com/macpor9/projektJS/blob/1e46b5ce38ec61adf17ea977a79929d1c32bf36e/interface.py#L69)


[List comprehensions](https://github.com/macpor9/projektJS/blob/1e46b5ce38ec61adf17ea977a79929d1c32bf36e/interface.py#L66)\
[List comprehensions](https://github.com/macpor9/projektJS/blob/1e46b5ce38ec61adf17ea977a79929d1c32bf36e/interface.py#L67)\
[List comprehensions](https://github.com/macpor9/projektJS/blob/1e46b5ce38ec61adf17ea977a79929d1c32bf36e/logic.py#L104)

[Main logic class](https://github.com/macpor9/projektJS/blob/1e46b5ce38ec61adf17ea977a79929d1c32bf36e/logic.py#L70)\
[Main interface class](https://github.com/macpor9/projektJS/blob/1e46b5ce38ec61adf17ea977a79929d1c32bf36e/interface.py#L5)

[Exceptions module](https://github.com/macpor9/projektJS/blob/master/exceptions.py)

[Interface module](https://github.com/macpor9/projektJS/blob/master/interface.py)\
[Logic module](https://github.com/macpor9/projektJS/blob/master/logic.py)


[Project Repository](https://github.com/macpor9/projektJS)