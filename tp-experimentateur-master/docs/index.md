# Tp Expérimentations


## État du TP
Tout le TP a été fait. Les 3 stratégies marchent. Les images sont incluses et une remarque a été faite avant la conclusion en finale en  d'expérience.



## Réponses aux questions
# Question 1-a)
Pour évaluer la complexité de cet algorithme, il convient de compter le nombre de comparaison entre les marqueurs de la liste positif(m) et  ceux de la liste positif(p).


Pour étudier la complexité de cet algorithme il faut compter le nombre de comparaison entre l'ensemble des élements de markers et les élements de positif. 

#### Question 1.b


*Non,il n y'a pas de pire cas pour cet algorithme  car il faudra parcourir tous les markers et les comparer à ceux de la liste de positif. Le parcours étant itératif,l'algorithme ne s'arrête qu'après le parcours  complet des deux liste.*
### Question 1-c

*_c1(m,p)=m\*p_*


### Question 1.3.2
--------------

Non, il n'y a pas de pire des cas, car il faut parcourir tous les éléments de la liste markers et les comparer au premier élément de la liste positive.
Borne supérieure
c2(m,p) = m

### Question 1.4.2

Oui, il y'a un pire des cas, c'est lorsqu'il n'y a pas d'élément négatif dans markers donc il faudra parcourir tout le tableau marker.
Borne supérieure
c3(m,p)=

### Question 2.4.3


### Question 2-2
*Le pire cas à envisager serait que les marqueurs positif sont le plus loin possible (fin de liste par exemple) et pour les trouver il faut parcourir la liste  du début jusqu'à la fin. Toutefois  ce algorithme est meilleur vis à vis du premier car  grâce à la recherche dichotomique, suivant la position et l'element situé situation à cette position, la taille est réduite et le parcours est meilleur*

### Question 3-2
*Il n'y a qu'un seul cas général, puisque le parcours est linéaire (une seule comparaison par marqueur).*
*Une fois la liste des marqueurs parcourue, il n'y a plus rien à faire car l'objectif est atteint. La borne supérieure est donc  c(m,p)=m*
### Question 4,Q5 et Q6
## Inclusion des fichiers photos.


#### Pour 10 markers on a:

![Image_10_marqueur](/images/image1.png)
 

#### Pour 20 markers on a:

![Image_20_marqueur](/images/image2.png)


### Pour 30 markers on a:
![Image_30_marqueur](/images/image3.png)

#### Pour 40 markers on a:
![Image_30_marqueur](/images/image4.png)

#### Pour 50 markers on a:

![Image_30_marqueur](/images/image5.png)


### Pour 60 markers on a:

![Image_30_marqueur](/images/image6.png)

#### Pour 70 markers on a:

![Image_30_marqueur](/images/image7.png)

#### Pour 80 markers on a:
![Image_30_marqueur](/images/image8.png)

#### Pour 90 markers on a:
![Image_30_marqueur](/images/image9.png)
anyway.
#### Pour 100 markers on a:
![Image_30_marqueur](/images/image10.png)

# Remarque
*La stratégie 3 semble avoir un peu  plus de comparaison pour des {m,p}  peu élévés. Ce qui est je pense dû au fait qu'il compte aussi le nombre de comparaison dans le tris de la liste des markeurs et celui du tris de la liste des positifs. Mais cette impression est vite contredite quand m>80.*
![Image_30_marqueur](/images/100_200.png)
*Progamme arrêté manuellement et suppression du debut des nombres afin de continuer avec le rapport et prendre en compte les données élévées*


# Conclusion
**En regardant les diverses images issues de cette expériences je constate que sans un tri préalable des marqueurs la stratégie 1 fait une complexité C(n)= mxp. Quant à la stratégie 2, elle fait une comparaison logarithmique. Cette réduction est due à la recherche dichotomique  dont le but principal est de réduire le nombre de compraisons lors de la mise en oeuvre de la la stratégie2.Par ailleurs, même si la stratégie3 semble être un peu au dessus de la deuxième au débbut de l'expérience, je constate que pour des nombres de marqueurs suffisament élévé, les deux courbes finissent par se croisser et celle de la stratégie3 passe de temps en temps en dessous de la deuxième. Par conjoncture, il est raisonnable de conclure que la courbe de la stratégie3 passera et restera définitivement sous la deuxième**