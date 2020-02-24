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
          },
          {
                "id": 15,                           
                "image_b64": "ddgw[...]jfe",
                "label": "Table",
                "name": "11",
                "node_id": 784,
                "object_id": 17
          },
          {
                "id": 16,
                "image_b64": "dqsdazr[...]sggOqsdfaz",
                "label": "Table",
                "name": "qsdfqsgsd",
                "node_id": 784,
                "object_id": 17
          },
          {
                "id": 17,
                "image_b64": "ezae[...]zaezae",
                "label": "Chaise",
                "name": "chaise.jpg",
                "node_id": 45,
                "object_id": 98
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
        },
        {
            "image_b64": "ezae[...]zaezae",
            "label": "Chaise",
            "name": "ezaeedqsdza",
            "node_id": 45,
            "object_id": 98
        }
    ]
    
      
OUTPUTS : Retourne toutes les images ajoutées (cf [GET] /images)

        
<br>

___
#### [PUT] - /images
DESCRITPION : Modifie le label de toutes les images d'un objet \
INPUTS : 
    
    {
        "object_id": 1,
        "label": "Baignoires"
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
    }
      
OUTPUTS : Retourne l'image modifiée (cf [GET] /images/\<id>)
      
        
<br>

___
#### [DELETE] - /images/\<id\>
DESCRITPION : Supprime une image grâce à son id \
INPUTS : None \
OUTPUTS : "Image [id] deleted with success"