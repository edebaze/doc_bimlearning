# Bim Learning

### Installation
__Installation linux__ : Récupérez le fichier "init" (dans le dossier "doc_init/linux" et placez le à l'endrois où vous souhaitez installer l'API Bim Learning.
Ouvrez le shell (Ctrl + alt + T) et lancez la commande 
> (path to init file)/init

En cas d'erreur, suivez l'instruction manuelle (doc_init/linux/linux_manual_install.rtf)



### Fonctionnement de l'API
> __Lancer le serveur__ : python api.py \
__Web Services__ : 	*description détaillée dans doc_init/doc/*<br>

<br>

___
##### Entrainer un modèle: [(documentation détaillée)](doc_init/doc/MODELS.md)
[GET] /models : retourne tous les models <br>
[GET] /models/id : retourne un model <br>
[POST] /models/train : entraine un nouveau model <br>
[PUT] /models/feed/id : entraine dynamiquement un model avec de nouvelles données <br>
[PUT] /models/id : change les paramètres d'un model <br>
[DELETE] /models/id : Supprime un model <br>
<br>

___
##### Créer un dataset: [(documentation détaillée)](doc_init/doc/DATASETS.md)
[GET] /datasets : retourne tous les datasets <br>
[GET] /datasets/id : retourne un dataset <br>
[POST] /datasets : crée un nouveau dataset <br>
[PUT] /datasets/id : ajoute de nouvelles images dans le dataset <br>
[DELETE] /datasets/id : Supprime un dataset <br>
<br>

___
##### Ajouter des images: [(documentation détaillée)](doc_init/doc/IMAGES.md)
[GET] /images : retourne toutes les images <br>
[GET] /images/id : retourne une image <br>
[POST] /images : ajoute de nouvelles images dans la base de données <br>
[POST] /images/from_rfa : ajoute de nouvelles images dans la base de données depuis un fichier rfa <br>
[PUT] /images : modifier le "label" des images liées à un objet <br>
[PUT] /images/id : modifier le "label" d'une image en particulier <br>
[DELETE] /images/id : Supprime une image <br>
<br>

___
##### Effectuer une prédiction: [(documentation détaillée)](doc_init/doc/PREDICTIONS.md)
[GET] /predictions : retourne toutes les prédictions <br>
[GET] /predictions/id : retourne la prédiction avec un id=id <br>
[POST] /predictions : effectue une nouvelle prédiction <br>
[POST] /predictions/test : effectue une prédiction sur un dossier de test <br>
