_______________________________________________________________________________________
									             	                                    
 #####  /MODELS: _Créer et Entrainer des models_ 		 	                    
_______________________________________________________________________________________

Description : \
Cette API permet de classifier un ensemble d’images donné grâce à un « model » de neural network

___
####[GET] - /models
DESCRITPION : Retourne tous les models. \
INPUTS : None \
OUTPUTS :  
       
    [   
        {
            "batch_size": 100, 		        - MODEL PARAM (Integer): nombre d'images par "batch" (= étape d'entrainement du model)
            "dataset_id": 3, 		        - MODEL PARAM (String): dataset utilisé pour l'entrainement du model
            "description": "[...]", 		- (String) Description ajoutée par le créateur du model
            "epochs": 1, 			        - MODEL PARAM (Integer): Nombre d'epochs (= réentrainements) utilisées lors de l'entrainement du model
            "id": 1, 				- (Integer - Primary Key) id du model dans la database de l'API
            "image_height": 224, 			- (Integer) Hauteur de l'image (les images fournies seront automatiquement redimmensionnées)
            "image_width": 224, 			- (Integer) Largeur de l'image (les images fournies seront automatiquement redimmensionnées)
            "layer2retrain": 9, 			- MODEL PARAM (Integer): nombre de couches à réentrainer lors d'un nouvel entrainement
            "name": "datasets_test_batch100_epochs1_retrain9.h5", - (String) Nom du model 
            "nn_name": "VGG16", 			- (String) Nom du type de neural network utilisé
            "nn_type": 1, 			        - (Integer) Type de neural network (= indice du nn_name)
            "seed": None,			        - MODEL PARAM (Integer): Nombre de "graines" à utiliser lors de la prédiction et l'entrainement des images
            "shuffle": false, 			- MODEL PARAM (Boolean): Mélanger les datasets
            "plot_loss": "figure_base64" 		- (String) Graphique de la perte lors de l'entrainement du model à chaque époque (format: base 64)
            "use_imageGenerator": false 		- MODEL PARAM (Boolean): Utiliser un générateur d'image
        },
        {
            "batch_size": 100,
            "dataset_id": 1,
            "description": "Test model training",
            "epochs": 10,
            "id": 2,
            "image_height": 224,
            "image_width": 224,
            "layer2retrain": 6,
            "name": "models/VGG16/db_test_bs100_e10_lt6.h5",
            "nn_name": "VGG16",
            "nn_type": 1,
            "seed": null,
            "shuffle": false,
            "use_imageGenerator": false,
            "use_rgb": true
        },
        {
            "batch_size": 100,
            "dataset_id": 17,
            "description": "Test model training",
            "epochs": 2,
            "id": 3,
            "image_height": 224,
            "image_width": 224,
            "layer2retrain": 6,
            "name": "models/VGG16/db_test_bs100_e2_lt6.h5",
            "nn_name": "VGG16",
            "nn_type": 1,
            "seed": null,
            "shuffle": false,
            "use_imageGenerator": false,
            "use_rgb": true
        }
    ]


####[GET] - /models/\<id>  
DESCRITPION : Retourne un model grâce à son id. \
INPUTS : None \
OUTPUTS :    
 
    {
            "batch_size": 100, 			            - MODEL PARAM (Integer): nombre d'images par "batch" (= étape d'entrainement du model)
            "dataset": "datasets_test", 		            - MODEL PARAM (Integer): id du dataset utilisé pour l'entrainement du model
            "description": "[...]", 		            - (String) Description ajoutée par le créateur du model
            "epochs": 1, 				            - MODEL PARAM (Integer): Nombre d'epochs (= réentrainements) utilisées lors de l'entrainement du model
            "id": 1, 				            - (Integer - Primary Key) id du model dans la database de l'API
            "image_height": 224, 			            - (Integer) Hauteur de l'image (les images fournies seront automatiquement redimmensionnées)
            "image_width": 224, 			            - (Integer) Largeur de l'image (les images fournies seront automatiquement redimmensionnées)
            "layer2retrain": 9, 			            - MODEL PARAM (Integer): nombre de couches à réentrainer lors d'un nouvel entrainement
            "name": "datasets_test_batch100_epochs1_retrain9.h5", - (String) Nom du model 
            "nn_name": "VGG16", 			            - (String) Nom du type de neural network utilisé
            "nn_type": 1, 				            - (Integer) Type de neural network (= indice du nn_name)
            "seed": None,				            - MODEL PARAM (Integer): Nombre de "graines" à utiliser lors de la prédiction et l'entrainement des images
            "shuffle": false, 			            - MODEL PARAM (Boolean): Mélanger les datasets
            "use_imageGenerator": false 		            - MODEL PARAM (Boolean): Utiliser un générateur d'image
    }



#### [POST] - /models/train    

DESCRITPION : Crée un model, l'entraine grâce à un ensemble d'images (+ paramètres d'entrainement, si besoin) fournis, et le sauvegarde. \
INPUTS :

    {
        "model_name": "Etienne_cegrosbg", 		- (String) Nom du model lors de la sauvegarde
        "dataset_id": 1,                            - (Integer) Id du dataset à utiliser pour entrainer le modèle
        "description": "Model de test", 	        - (String) Description du modèle
        "parameters": { 			        - [NON OBLIGATOIRE](Array) Array de paramètres de model à modifier lors de l'entrainement ("parameters" : "Default" ou {} pour utiliser les paramètres par défaut)
            "epochs": 2,            -> (nombre de réentrainements du modèle)
            "num_predictions": 3,   -> (nombre de suggestions à retourner)
            "validation_split': 0.1,        
            ...
        } 					
    }

OUTPUTS :  Retourne le modèle créé (cf [GET] /models/<id>)

___
#### [DELETE] - /models/\<id>    

DESCRITPION : Supprime un modèle grâce à son id \
INPUTS : None \
OUTPUTS : "Modèle [id] supprimé"

___
#### [PUT] - /models/feed/\<id>    

DESCRITPION : Envoie des images au modèle afin de l'entrainer dynamiquement. Les images sont automatiquement 
sauvegardées dans le dataset du modèle\
Les images peuvent être de nouvelles images, ou l'id d'une image en base de donnée \
INPUTS : 

    {
	"images":                               - (Array) Liste d'images (nouvelles, ou id)
		{
		    "image_b64": "iVBORw[...]AACAAAAA",     - (String) Image en format base 64
		    "label": "Baignoire",                   - (String) Classe de l'image
		    "node_id": 1,                           - (Integer) id du node de la classe
		    "name": "bfdsfjk.png"                   - (String) nom de l'image
		    "object_id": 5                          - (Integer) id de l'objet duquel l'image a été extraite
		},
		{
		    "id": 3                                 - (Integer) Id de l'image dans la database
		}
		{
		    "id": 15                                - (Integer) Id de l'image dans la database
		}
	]
}
    
OUTPUTS : Retourne le modèle , mis à jour et entrainé par les images fournies (cf [GET] /models/\<id>)