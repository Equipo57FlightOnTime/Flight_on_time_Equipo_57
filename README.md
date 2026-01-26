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
│       ├── aerolineas.csv
│       ├── rutas_validas.csv
│       └── aeropuertos.csv
│
├── 📁 data
│   ├── 📁 raw
│   │   └── README.md
│   │
│   └── 📁 processed
│       └── README.md
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
│       ├── modelo_flightontime_xgboost_final.pkl
│       ├── notes.md
│       └── model_metadata.json
│
├── 📁 notebooks
│   ├── 📁 team
│   │   ├── andres/
│   │   ├── diego/
│   │   ├── gustavo/
│   │   ├── jean/
│   │   ├── saul/
│   │   └── william/
│   │
│   └── 📁 consolidated
│       ├── eda_summary.ipynb
│       ├── feature_engineering_final.ipynb
│       └── model_comparison.ipynb
│
│
├── 📁 docs
│   └── Contrato-Integracion.ipynb
│
└── README.md
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

