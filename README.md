Aplikacja tworząca fiszki do nauki angielskiego dla programu Anki (ankisrs.net) na podstawie plików tekstowych (np. napisów do filmów).
# Części aplikacji
## Baza wiedzy o użytkowniku
Zbiór krotek (słowo, nie znał/znał, kiedy znał/nie znał)  
W momencie dodania nowego słowa do bazy słowo to może być znane użytkownikowi lub nie.

## Lista frekwencyjna
Zbiór krotek (słowo, częstość występowania)

## Ankieta
Prosta aplikacja okienkowa, która zadaje pytania typu „Czy znasz słowo X?” i dodaje informacje do bazy wiedzy o użytkowniku.

## 1. Parser
### 1.1. Wyszukiwanie słów w pliku
Wejście: plik tekstowy  
Wyjście: zbiór „słów” z tego pliku (najdłuższe spójne ciągi liter)  
„Słowa” tutaj to niekoniecznie poprawne słowa w języku angielskim, np. poniżej „s”.

Przykład:  
Wejście:  
1  
00:00:03,036 --> 00:00:08,201  
She often speaks about Mary's fiancé.  
Wyjście:  
{She, often, speaks, about, Mary, s, fiancé}

### 1.2. Normalizacja słowa
#### 1.2.1. Zamiana dużych liter na małe
Przykład:  
{she, often, speaks, about, mary, s, fiancé}

#### 1.2.2. Wyłuskanie możliwych tematów/rdzeni ze słów
Tutaj coś trzeba wiedzieć o języku.  
Możliwe przykłady:
- income -> [income, come]
- moved -> [moved, mov, move]
- leaves -> [leaves, leav, leave]
- bought -> [bought]

Przykład:  
{[she], [often], [speaks, speak], [about], [mary], [s], [fiancé]}

#### 1.2.3. Zgadnięcie tematu/rdzenia
Najczęstsze słowo uznaję za temat.  
Przykład:  
{she, often, speak, about, fiancé}
## 2. Wybieranie ważnych słów
Użytkownik ma dwa cele:
- poszerzyć swoje ogólne słownictwo
- poszerzyć słownictwo potrzebne tylko do zrozumienia konkretnego materiału
	
Zysk poznania słowa to częstość f występowania tego słowa w języku/materiale.  
Strata to wysiłek potrzebny na nauczeniu słowa (współczynnik L<0) i na odpowiedzenie na pytanie w ankiecie („Czy znasz słowo X?”) (współczynnik A<0).  
Można estymować prawdopodobieństwo p znania słowa na podstawie bazy wiedzy o użytkowniku. Jeśli słowo znajduje się na 4533. miejscu na liście frekwencyjnej oraz użytkownik znał 20 na 40 słów między 4000 a 5000 miejscem na liście frekwencyjnej, to przyjmuję, że prawdopodobieństwo znania słowa wynosi 1/2. Nie wiem, jak w praktyce sprawdzi się takie rozumowanie.  

Średni zysk pytania o to słowo wynosi: (A + f + L) (1 - p) + A p

Można wybierać kilkadziesiąt słów o największym średnim zysku albo wszystkie o dodatnim średnim zysku.
Są one jeszcze przesiewane przez odpytanie użytkownika w ankiecie, czy zna dane słowa.

## 3. Tworzenie obiektu reprezentującego fiszkę
### 3.1. Angielskie słowo
Jest.
### 3.2. Audio angielskiego słowa
Jeszcze nie wiem, skąd je wziąć.
### 3.3. Przykładowe zdania
Jeszcze nie wiem, jak je wybierać, ale trzeba to robić mądrze, bo zdań jest aż pół miliona w Tatoeba.
### 3.4. Audio przykładowych zdań
Z Tatoeba.
### 3.5. Tłumaczenie słowa
Jeszcze nie wiem, skąd je wziąć.
### 3.6. Tłumaczenie zdań
Z Tatoeba.

## 4. Konwersja obiektów na pliki .apkg (pliki programu Anki)

# Linki
- https://tatoeba.org/
- http://ankisrs.net/
- http://decks.wikia.com/wiki/Anki_APKG_format_documentation
- http://www.meetenglish.pl/blog/ile-znam-slowek-po-angielsku/
- http://testyourvocab.com/
