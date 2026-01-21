## Descripción del experimento
- Autor: william
- Modelo: XGBoost
- Dataset: 2016
- Features: temporales + aerolínea

## Resultados
- Accuracy : 0.7993   
- Precision: 0.3197
- Recall   : 0.1941
- F1       : 0.2416

## Observaciones

| Modelo        | PR-AUC        | Precision@10% | Accuracy* | Tiempo de entrenamiento | Uso de RAM | Estabilidad | Observaciones |
|---------------|---------------|---------------|-----------|--------------------------|------------|-------------|---------------|
| LightGBM      | ~0.26–0.27    | ~0.32         | Alta      | Rápido                   | Bajo       | Alta        | Buen baseline, rápido y estable |
| XGBoost     | **0.2659**    | **0.3197**    | Media-Alta| Medio                    | Medio      | Alta        | Mejor balance general, recomendado |

