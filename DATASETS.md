_______________________________________________________________________________________
									             	                                    
 #####  /DATASETS 		 	                    
_______________________________________________________________________________________

Description : \
   _Créer des datasets d'images pour l'entrainement de modèles de prédiction_

___
#### [GET] - /datasets
DESCRITPION : Retourne tous les datasets \
INPUTS : None \
OUTPUTS :  

    [
        {
            "classification_table": "Omniclass",        - (String) Nom de la classification
            "id": 1,                                    - (Integer) Id du dataset
            "image_ids": [                              - (Array) Liste d'ids des images composant le dataset
                  1,
                  2,
                  3,
                  4,
                  13,
                  14
            ],
            "name": "dataset_test"                      - (String) Nom du dataset
        },
        {
            "classification_table": "Bim&Co",
            "id": 2,
            "image_ids": [
                  7,
                  8,
                  9,
                  10,
                  15,
                  16,
                  2,
                  17
            ],
            "name": "proto_v1"
        }
    ]
    
    
<br>
    
___    
#### [GET] - /datasets/\<id>
DESCRITPION : Retourne un dataset grâce à son id \
INPUTS : None \
OUTPUTS :  

    {
        "classification_table": "Omniclass",        - (String) Nom de la classification
        "id": 1,                                    - (Integer) Id du dataset
        "image_ids": [                              - (Array) Liste d'ids des images composant le dataset
              1,
              2,
              3,
              4,
              13,
              14
        ],
        "name": "dataset_test"                      - (String) Nom du dataset
    }
    
<br>
    
___
#### [POST] - /datasets
DESCRITPION : Créer un dataset \
INPUTS :

    {
	    "name": "dataset_test",                     - (String) Nom du dataset
        "classification_table": "Omniclass",        - (String) Nom de la classification
        "images": [                                 - (Array) Liste d'images (ou d'id d'images) composant le dataset
            {
                "image_b64": "QAFE4NQO[...]AAAAA",
                "label": "Baignoire",
                "node_id": 1,
                "name": "blabla",
                "object_id": 1
            },
            {
                "image_b64": "iVBORw[...]0KGgo=",
                "label": "Portes",
                "node_id": 43,
                "name": "sqdsqdsqd",
                "object_id": 189
            },
            {
                "id" = 17
            }
        ]
    }
    
OUTPUTS : Dataset créé (cf [GET] /datasets)

<br>

___
#### [DELETE] - /datasets/\<id\> 
DESCRITPION : Supprime un dataset \
INPUTS : None \
OUTPUTS: "Dataset [id] deleted with success"