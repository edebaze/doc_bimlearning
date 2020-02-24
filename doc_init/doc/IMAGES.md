______________________________________________________________________________________________________
#### /IMAGES 
______________________________________________________________________________________________________

_Ajouter une image et sa classification dans la base de données_	
______________________________________________________________________________________________________

#### [GET] - /images  
DESCRITPION : Retourne toutes les images \
INPUTS : None   \
OUTPUTS :   

    [
          {
                "id": 14,                           - (Integer) Id de l'image dans la base de données
                "image_b64": "AZvi[...]Bojfspq",    - (String) Image en format base 64
                "label": "Baignoire",               - (String) Label (=classe) de l'image
                "name": "bath_tub.png",             - (String) Nom de l'image (peut être n'importe quoi)
                "node_id": 12,                      - (Integer) Id du label dans la table de classification
                "object_id": 4                      - (Integer) Id de l'objet dont l'image a été extraite
                "id_bimandco": 732                  - (Integer) Id de l'image dans la base de données BIM&Co
          },
          {
                "id": 15,                           
                "image_b64": "ddgw[...]jfe",
                "label": "Table",
                "name": "11",
                "node_id": 784,
                "object_id": 17,
                "id_bimandco": 5
          },
          {
                "id": 16,
                "image_b64": "dqsdazr[...]sggOqsdfaz",
                "label": "Table",
                "name": "qsdfqsgsd",
                "node_id": 784,
                "object_id": 17,
                "id_bimandco": 2121
          },
          {
                "id": 17,
                "image_b64": "ezae[...]zaezae",
                "label": "Chaise",
                "name": "chaise.jpg",
                "node_id": 45,
                "object_id": 98,
                "id_bimandco": 715
          }
    ]
    
<br>

___
#### [GET] - /images/\<id\>  
DESCRITPION : Retourne une image grâce à son id \
INPUTS : None   \
OUTPUTS :   

    {
        "id": 14,                           - (Integer) Id de l'image dans la base de données
        "image_b64": "AZvi[...]Bojfspq",    - (String) Image en format base 64
        "label": "Baignoire",               - (String) Label (=classe) de l'image
        "name": "bath_tub.png",             - (String) Nom de l'image (peut être n'importe quoi)
        "node_id": 12,                      - (Integer) Id du label dans la table de classification
        "object_id": 4                      - (Integer) Id de l'objet dont l'image a été extraite
        "id_bimandco": 732                  - (Integer) Id de l'image dans la base de données BIM&Co
    }    
      
<br>

___
#### [POST] - /images
DESCRITPION : Ajoute des images dans la base de données \
INPUTS : 

    [
        {
            "image_b64": "AZvi[...]Bojfspq",    - (String) Image en format base 64
            "label": "Baignoire",               - (String) Label (=classe) de l'image
            "name": "bath_tub.png",             - (String) Nom de l'image (peut être n'importe quoi)
            "node_id": 12,                      - (Integer) Id du label dans la table de classification
            "object_id": 4                      - (Integer) Id de l'objet dont l'image a été extraite
            "id_bimandco": 789                  - (Integer) Id de l'image dans la bdd BIM&Co
        },
        {
            "image_b64": "ezae[...]zaezae",
            "label": "Chaise",
            "name": "ezaeedqsdza",
            "node_id": 45,
            "object_id": 98
            "id_bimandco": 23                   
        }
    ]
    
      
OUTPUTS : Retourne toutes les images ajoutées (cf [GET] /images)

        
<br>

___
#### [PUT] - /images
DESCRITPION : Modifie le label de toutes les images d'un objet associées à un "node_id" \
INPUTS : 
    
    {
        "object_id": 1,                     - (Integer) id de l'objet de l'image
        "node_id": 17,                      - (Integer) id du label associé à cet objet
        "new_node_id": 55,                  - (Integer) nouvel id de label associé à l'objet
        "new_label": "Baignoires"           - (String) nouveau label associé à l'objet
    }
      
OUTPUTS : Retourne toutes les images modifiées (cf [GET] /images)

      
        
<br>

___
#### [PUT] - /images/\<id\>
DESCRITPION : Modifie les paramètres d'une image (aucun paramètre particulier n'est requis)\
INPUTS : 
    
    {
        "name": "Babar"                 - [NON REQUIS] nouveau nom de l'image
        "label": "Baignoires"           - [NON REQUIS] nouveau label
        "node_id": 15                   - [NON REQUIS] nouvel id du label dans la base de données
        "object_id": 37                 - [NON REQUIS] nouvel id de l'objet dans la base de données
        "id_bimandco": 254              - [NON REQUIS] nouvel id de l'image dans la bdd BIM&Co
    }
      
OUTPUTS : Retourne l'image modifiée (cf [GET] /images/\<id>)
      
        
<br>

___
#### [DELETE] - /images/\<id\>
DESCRITPION : Supprime une image grâce à son id \
INPUTS : None \
OUTPUTS : "Image [id] deleted with success"

<br>

___
#### [DELETE] - /images
DESCRITPION : Supprime toutes les images associées aux id "nodes_id" \
INPUTS : 

    {
        "nodes_id": [15, 92, 11]       - (Array) Id des noeuds à supprimer
    }
    
OUTPUTS : "Images of nodes_id [id] deleted with success"