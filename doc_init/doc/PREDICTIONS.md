______________________________________________________________________________________________________
####/PREDICTIONS 
______________________________________________________________________________________________________

_Effectuer une prédiction sur un ensemble de données afin d'en classer le contenu_	
______________________________________________________________________________________________________

####[GET] - /predictions  
DESCRITPION : Retourne toutes les predictions \
INPUTS : None   \
OUTPUTS :   
 
    [
        {
            "id": 3,
            "predictions"
                {
                    "image_b64": "erTesR  [...] efEFfq",                            - Return input image (as string b64)
                    "name": "image 1",                                              - Return given name of the image (can be of any type but multidimensional)
                    "predictions": [                                                - Array of predictions, in order from the most probable to the less likely
                          {
                                "estimated_accuracy": 1.0,                          - Probability that the prediction is correct
                                "label": "Canapé",                                  - Classification as string
                                "node_id": "7039"                                   - Id of the node of the string classification (label)
                          },
                          {
                                "estimated_accuracy": 9.657378896577029e-09,
                                "label": "Chaise",
                                "node_id": "7038"
                          },
                          {
                                "estimated_accuracy": 4.575554102270729e-10,
                                "label": "Refroidisseur",
                                "node_id": "47332"
                          }
                    ]
                },
                {
                    "image_b64": "iVBOR  [...] w0K",
                    "name": 17,
                    "predictions": [
                          {
                                "estimated_accuracy": 0.9,
                                "label": "Canapé",
                                "node_id": "7039"
                          },
                          {
                                "estimated_accuracy": 5.456-03,
                                "label": "Bureau",
                                "node_id": "887"
                          },
                          {
                                "estimated_accuracy": 9.54555e-02,
                                "label": "Table",
                                "node_id": "99532"
                          }
                    ]
                }
        }
    ]


<br>

___
####[GET] - /predictions/<id>   
DESCRITPION : Retourne une prédiction depuis son id \
INPUTS : None   \
OUTPUTS :   

    {
        "id": 3,
        "predictions":
            {
                "image_b64": "erTesR  [...] efEFfq",                            - Return input image (as string b64)
                "name": "image 1",                                              - Return given name of the image (can be of any type but multidimensional)
                "predictions": [                                                - Array of predictions, in order from the most probable to the less likely
                      {
                            "estimated_accuracy": 1.0,                          - Probability that the prediction is correct
                            "label": "Canapé",                                  - Classification as string
                            "node_id": "7039"                                   - Id of the node of the string classification (label)
                      },
                      {
                            "estimated_accuracy": 9.657378896577029e-09,
                            "label": "Chaise",
                            "node_id": "7038"
                      },
                      {
                            "estimated_accuracy": 4.575554102270729e-10,
                            "label": "Refroidisseur",
                            "node_id": "47332"
                      }
                ]
          },
          {
                "image_b64": "iVBOR  [...] w0K",
                "name": 17,
                "predictions": [
                      {
                            "estimated_accuracy": 1.0,
                            "label": "Canapé",
                            "node_id": "7039"
                      },
                      {
                            "estimated_accuracy": 9.657378896577029e-09,
                            "label": "Chaise",
                            "node_id": "7038"
                      },
                      {
                            "estimated_accuracy": 4.575554102270729e-10,
                            "label": "Refroidisseur",
                            "node_id": "47332"
                      }
                ]
          }
    }



<br>

___
[POST] - /predictions ---------------------------------------------------------------------------------------
DESCRITPION : Lit un ensemble d'images (format: base64) et retourne une Prediction (object)
    
    {
        "model_id": 3,                                                          - [NOT REQUIRED] ID of the model to use (do not add this key to the inputs data if you want to use the "default model", or set value to None)
        "array_image_b64": [                                                    - array of images to predict
            {
                "name": "image 1",                                              - name of the imag to predict (can be any type but multidimensional)
                "image_b64": "erTesR[...efEFfq",                                - input image (as string b64)
            },
            {
                "name": 17,
                "image_b64": "iVBOR[...]w0K",
            }
        ]
    }

OUTPUTS : \ 

    [
          {
                "image_b64": "erTesR  [...] efEFfq",                            - Return input image (as string b64)
                "name": "image 1",                                              - Return given name of the image (can be of any type but multidimensional)
                "predictions": [                                                - Array of predictions, in order from the most probable to the less likely
                      {
                            "estimated_accuracy": 1.0,                          - Probability that the prediction is correct
                            "label": "Canapé",                                  - Classification as string
                            "node_id": "7039"                                   - Id of the node of the string classification (label)
                      },
                      {
                            "estimated_accuracy": 9.657378896577029e-09,
                            "label": "Chaise",
                            "node_id": "7038"
                      },
                      {
                            "estimated_accuracy": 4.575554102270729e-10,
                            "label": "Refroidisseur",
                            "node_id": "47332"
                      }
                ]
          },
          {
                "image_b64": "iVBOR  [...] w0K",
                "name": 17,
                "predictions": [
                      {
                            "estimated_accuracy": 0.9,
                            "label": "Canapé",
                            "node_id": "7039"
                      },
                      {
                            "estimated_accuracy": 9.2336597612e-02,
                            "label": "Bureau",
                            "node_id": "3294"
                      },
                      {
                            "estimated_accuracy": 7.76546512548e-03,
                            "label": "Table",
                            "node_id": "45"
                      }
                ]
          }
    ]



<br>

___
[POST] - /predictions/test ---------------------------------------------------------------------------------------
DESCRITPION : Test le modèle avec un dataset de test déjà prêt
INPUTS : 
{
    	"model_id": 1 				-	 (Integer) Id du model à utiliser
}

OUTPUTS :  Retourne la prédiction (cf [GET] /predictions/<id>)
