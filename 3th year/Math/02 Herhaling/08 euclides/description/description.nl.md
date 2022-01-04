Het algoritme van **Euclides** is één van de oudste algoritmes ter wereld. Het algoritme dat beschreven werd in zijn legendarische [handboek](https://nl.wikipedia.org/wiki/Euclides_van_Alexandri%C3%AB) is een efficiënte manier om de grootste gemene deler (ggd) van twee getallen te bepalen.

Het algoritme werkt als volgt:

- Noem het grootste van de twee getallen $$A$$ en het andere $$B$$
- Bepaal de rest $$R$$ bij deling van $$A$$ door $$B$$
- is $$R$$ nul, dan is $$B$$ de ggd
- indien $$R$$ niet nul is, herhaal het algoritme dan voor $$B$$ en de rest $$R$$

Een voorbeeld zal dit duidelijker maken:

Beschouw $$A = 28$$ en $$B = 16$$. Een getraind oog ziet meteen in dat de $$\text{ggd}(28,16) = 4$$. Het algoritme toepassen werkt nu als volgt:

- De rest bij deling van $$28$$ en $$16$$ is $$12$$
- De rest bij deling van $$16$$ en $$12$$ is $$4$$
- De rest bij deling van $$12$$ en $$4$$ is $$0$$, zodat $$4$$ de ggd is.

## Opgave

Schrijf een programma dat twee gehele getallen als invoer krijgt en vervolgens de grootste gemene deler bepaalt.

#### Voorbeelden
Voor de invoer `28` en `16` verschijnt:
```
De grootste gemene deler van 28 en 16 is 4
```
Voor de invoer `16` en `28` verschijnt:
```
De grootste gemene deler van 28 en 16 is 4
```
Voor de invoer `1140` en `900` verschijnt:
```
De grootste gemene deler van 1140 en 900 is 60
```