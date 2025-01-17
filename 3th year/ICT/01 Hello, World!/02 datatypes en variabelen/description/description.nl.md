<!---
@TODO opsplitsing variabelen en datatypes
--->

## Soorten getallen en tekst
Een computer kan omgaan met heel wat verschillende soorten gegevens. Werken we met gegevens binnen Python, dan zal Python zelf bepalen welke soort gegevens het zijn, bijvoorbeeld een getal of een stukje tekst. Toch is het zeer nuttig om enkele **datatypes** beter te leren kennen.

### Gehele getallen
Het belangrijkste datatype zijn ongetwijfeld de gehele getallen, in het Engels noemt men dit **integers**. Met behulp van de *functie* `type()` kan je gemakkelijk achterhalen wat het type van een gegeven of *variabele* is. In het onderstaande codevoorbeeld wordt het getal 5 opgeslagen in de variabele `x`. In Minecraft zou je dit als volgt doen:

![variabele](media/minecraft_new_variable.png "variabele"){:data-caption="Een variabele definiëren in Minecraft Education Edition" width="139px"}

Maak nu een nieuwe Repl aan en probeer het volgende stukje code uit:

```python
x = 5
print( type( x ) )
```
Je merkt dat `x` van het type `int` is.

{: .callout.callout-danger}
> #### Opgelet
> De naam van een variabele mag geen spaties of eigenaardige karakters bevatten. De naam `geheel getal` is dus niet geldig voor een variabele, wel toegelaten is `geheel_getal`.

Gebruik bij het programmeren steeds **variabelen**. Stel dat je de oppervlakte van een kubus met zijde 3 moet berekenen. Doe dan als volgt:
```python
zijde = 3
oppervlakte_kubus = 6 * zijde * zijde
print( oppervlakte_kubus )
```
Door in de *berekeningen* de variabele `zijde` te gebruiken, kan het programma eenvoudig aangepast worden op de oppervlakte van een kubus met zijde 5 te bepalen. Het volstaat dan om de eerste regel aan te passen naar `zijde = 5`

### Kommagetallen
Kommagetallen, of **floating-point numbers**, zorgen voor een computer al meteen een probleem. Een computer kan moeilijk overweg met getallen die een *onbegrensde decimale vorm* hebben. Probeer het volgende stukje code uit, merk hierbij op dat komma's in Python met behulp van een **punt** geschreven worden.

```python
x = 3.5
print( type( x ) )
```
Je merkt dat `x` van het type `float` is.

Merk op dat ook indien een deling geheel is, Python dit toch als een kommagetal behandelt. Beschouw het volgende voorbeeld:

```python
x = 18/3
print( x )
print( type( x ) )
```

Door de manier waarop Python floats opslaat, kunnen bepaalde getallen niet precies vastgelegd worden. Probeer bijvoorbeeld eens:
```python
print( (431 / 100) * 100 )
```
Wat merk je op?

### Booleaanse waarden
Booleaanse waarden worden in wiskunde verder onder de loep genomen, het is een datatype dat enkel de waarde `True` of `False` kan aannemen en wordt vooral gebruikt bij het maken van keuzes.

```python
x = True
print( type( x ) )
```
Je merkt dat `x` van het type `bool` is.

Dit type is vooral belangrijk indien we bepaalde *voorwaarden* willen controleren.
```python
x = 5
print( x > 0 )
```

### Tekst
Een reeks tekens of tekst noemt men in het Engels een **string**. Werk je met tekst dan moet je de tekens steeds tussen aanhalingstekens `'` plaatsen.

```python
x = 'Expecto patronum!'
print( type( x ) )
```
Je merkt dat `x` van het type `str` is.

Een getal hoeft niet altijd van het type integer zijn. Zo heeft het bijvoorbeeld weinig zin om een huisnummer op te slaan als een geheel getal. Logischer is in dit geval:

```python
huisnummer = '7'
print( type( huisnummer ) )
```

Let op dat je variabelen niet tussen aanhalingstekens plaatst. Onderstaande code maakt het verschil duidelijk.
```python
x = 5
print( x )
print( 'x' )
```

## Datatypes casten

Het kan nuttig zijn om gegevens naar een ander datatype om te zetten. Daarvoor bestaan de *functies* `int()`, `float()` en `str()`. Beschouw bijvoorbeeld:

```python
x = int( 18/3 )
print( x )
print( type(x) )
```

## Opgave
Onderstaande code bevat verschillende fouten. Pas deze aan zodat van het getal `a` eerst het dubbele en daarna het kwadraat op het scherm weergegeven wordt.