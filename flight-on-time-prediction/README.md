# Flight on time 2019 - 2023

Sistema predictivo para estimar retrasos en vuelos comerciales usando Machine Learning

## 🎯 Objetivo del proyecto
Desarrollar una solución predictiva capaz de estimar si un vuelo despegará a tiempo o con retraso, utilizando datos históricos del periodo 2019–2023 y técnicas de ciencia de datos y aprendizaje automático.

---


## 🛠️ Tecnologías y herramientas

| Categoría                    | Herramientas                         |
|-----------------------------|--------------------------------------|
| Lenguaje                    | Python                               |
| Análisis de datos           | Pandas, NumPy                        |
| Machine Learning            | Scikit-learn, XGBoost                |
| Visualización               | Matplotlib, Seaborn                  |
| Desarrollo                  | Jupyter Notebook                     |
| Control de versiones        | Git, GitHub                          |

---
## Estructura del Proyecto
```
📦 flight-on-time-prediction
│
├── 📁 backend
│   └── 📁 dictionaries
│       ├── airport_iata_coords.csv
│       └── diccionario_variables_2009_2023.csv
│
├── 📁 data
│   ├── 📁 raw
│   │   ├── airline_delay_2009_2018.csv
│   │   ├── flight_delay_2019_2023.csv
│   │   └── flight_data_2024.csv
│   │
│   ├── 📁 processed
│   │   ├── flights_2016.parquet
│   │   └── historico_flight_on_time_2009_2024.parquet
│
├── 📁 notebooks
│   ├── 📁 eda
│   │   ├── eda_2009_2018.ipynb
│   │   ├── eda_2016.ipynb
│   │   ├── eda_2023_part1.ipynb
│   │   ├── eda_2023_part2.ipynb
│   │   └── eda_2024.ipynb
│   │
│   ├── 📁 feature_engineering
│   │   └── feature_engineering.ipynb
│   │
│   └── 📁 modeling
│       └── experiments.ipynb
│
├── 📁 models
│   ├── 📁 experiments
│   │   ├── andres/
│   │   ├── diego/
│   │   ├── gustavo/
│   │   ├── jean/
│   │   ├── saul/
│   │   └── william/
│   │
│   └── 📁 production
│       ├── model_xgboost_final.pkl
│       └── model_metadata.json
│
├── 📁 reports
│   ├── eda_summary.md
│   ├── model_evaluation.md
│   └── conclusions.md
│
├── 📁 docs
│   ├── project_overview.md
│   └── next_steps.md
│
├── README.md
└── requirements.txt
```
---
# Resumen del proyecto

## 🧠 Feature Engineering
Se realizó la creación y transformación de variables relacionadas con:
- Variables temporales (hora, día del año, estacionalidad)
- Variables operativas del vuelo
- Variables históricas de retraso

## 📊 Análisis Exploratorio de Datos (EDA)
Se analizaron patrones históricos de retrasos considerando:
- Aerolíneas
- Aeropuertos
- Franja horaria
- Estacionalidad

## 🤖 Entrenamiento y evaluación de modelos
Se probaron diferentes algoritmos de Machine Learning, destacando modelos basados en árboles de decisión como XGBoost, evaluados mediante métricas de clasificación.

## 🚀 Próximos pasos
- Incorporación de variables meteorológicas
- Mejor tratamiento de variables temporales
- Optimización de hiperparámetros
- Preparación del modelo para despliegue productivo

