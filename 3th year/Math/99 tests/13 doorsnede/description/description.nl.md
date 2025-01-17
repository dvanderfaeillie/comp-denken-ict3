{: .callout.callout-danger}
> De doorsnede van twee verzamelingen $$A$$ en $$B$$ is gedefinieerd als:
>
> $$A \cap B = \{ x: x\in A \text{ en } x \in B \}$$

## Opgave
Schrijf een functie `doorsnede( interval1 , interval2 )` die gegeven twee **gesloten** intervallen voor de juiste uitvoer zorgt.

De *gesloten* intervallen worden voorgesteld door middel van *tupels*.


#### Voorbeelden
```
>>> doorsnede( ( 3, 5 ), ( -1, 4 ) )
De doorsnede van [ 3 , 5 ] en [ -1 , 4 ] is [ 3 , 4 ]
```
```
>>> doorsnede( ( -8, 0 ), ( 5, 10 ) )
De doorsnede van [ -8 , 0 ] en [ 5 , 10 ] is ledig
```
```
>>> doorsnede( ( -2, 6 ), ( 6, 7 ) )
De doorsnede van [ -2 , 6 ] en [ 6 , 7 ] is singleton 6
```

{: .callout.callout-info}
> #### Tip
> Je kan dit efficiënt programmeren met behulp van de functies `min()` en `max()` om enerzijds het minimum en het maximum te bepalen. Je hoeft dit zeker niet te gebruiken, andere manieren zijn ook mogelijk.