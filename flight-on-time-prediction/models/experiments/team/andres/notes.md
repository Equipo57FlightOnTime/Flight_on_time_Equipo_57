## Descripción del experimento
- Autor: Andres
- Modelo: CatBoost
- Dataset: 2019–2024
- Features: temporales + aerolínea

## Resultados
=== Test 2023: ARR_DELAY > 15 (DELTA + CatBoost + calibración) ===
- Accuracy : 0.6750 
- Precision: 0.3037
- Recall   : 0.3768
- F1       : 0.3363

## Observaciones
- Mejor desempeño en vuelos matutinos
- Posible sobreajuste en aeropuertos pequeños
- Para lograr una correlación fuerte se requerirá de variables de tiempo/clima.
- Se da un dilema entre tener más precisión en pocas alertas, o tener muchas alertas poco fiables.
- Matriz de confusión: No hay tantos datos de retraso versus no retraso, lo cual genera sesgo.
  [ [TN FP]
    [FN TP] ]
[[274662  87528]
 [ 63122  38172]]
- Debido a que no es, y con ningún modelo va a tenerse 100% certeza, se sugiere tener umbrales de probabilidad. Alta, media o baja. De esta manera se maneja mejor las expectativas del usuario.
