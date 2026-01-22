## Descripción del experimento
- Autor: diego
- Modelo: XGBoost
- Dataset: 2019–2024
- Features: temporales + aerolínea

## Resultados

- Accuracy : 0.62
- Precision: 0.26
- Recall   : 0.62
- F1       : 0.36

## Observaciones

* El modelo detecta correctamente el 62% de los retrasos reales → Ideal para el objetivo del cliente: alertar con antelación a pasajeros, aerolíneas y aeropuertos.
* La precisión de 0.26 en retrasados es típica en datasets históricos sin variables externas (clima, tráfico en tiempo real, mantenimiento).
* Modelo final seleccionado: XGBoost con undersampling + feature ES_HORA_PICO (mejor balance y recall).
Threshold: 0.5 (default) – si se desea más sensibilidad, probar 0.4 (recall sube a ~0.80, pero más alertas falsas).
