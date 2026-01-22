# EDA - Hallazgos relevantes
## Conociendo los datos

Dataset 2019 - 2023
RangeIndex: 3000000 entries, 0 to 2999999 Data columns (total 32 columns):

| # | Column | Dtype |
 |:---:|:---|:---| 
 | 0 | FL_DATE | object |
 | 1 | AIRLINE | object | 
 | 2 | AIRLINE_DOT | object |
 | 3 | AIRLINE_CODE | object | 
 | 4 | DOT_CODE | int64 | 
 | 5 | FL_NUMBER | int64 | 
 | 6 | ORIGIN | object | 
 | 7 | ORIGIN_CITY | object | 
 | 8 | DEST | object | 
 | 9 | DEST_CITY | object | 
 | 10 | CRS_DEP_TIME | int64 | 
 | 11 | DEP_TIME | float64 | 
 | 12 | DEP_DELAY | float64 | 
 | 13 | TAXI_OUT | float64 | 
 | 14 | WHEELS_OFF | float64 | 
 | 15 | WHEELS_ON | float64 | 
 | 16 | TAXI_IN | float64 | 
 | 17 | CRS_ARR_TIME | int64 | 
 | 18 | ARR_TIME | float64 | 
 | 19 | ARR_DELAY | float64 | 
 | 20 | CANCELLED | float64 | 
 | 21 | CANCELLATION_CODE | object | 
 | 22 | DIVERTED | float64 | 
 | 23 | CRS_ELAPSED_TIME | float64 | 
 | 24 | ELAPSED_TIME | float64 | 
 | 25 | AIR_TIME | float64 | 
 | 26 | DISTANCE | float64 | 
 | 27 | DELAY_DUE_CARRIER | float64 | 
 | 28 | DELAY_DUE_WEATHER | float64 | 
 | 29 | DELAY_DUE_NAS | float64 | 
 | 30 | DELAY_DUE_SECURITY | float64 | 
 | 31 | DELAY_DUE_LATE_AIRCRAFT | float64 |


### Descripción de variables numéricas
|index|count|mean|std|min|25%|50%|75%|max|
|---|---|---|---|---|---|---|---|---|
|DOT\_CODE|3000000\.0|19976\.294095|377\.284619113086|19393\.0|19790\.0|19930\.0|20368\.0|20452\.0|
|FL\_NUMBER|3000000\.0|2511\.5355186666666|1747\.2580396345143|1\.0|1051\.0|2152\.0|3797\.0|9562\.0|
|CRS\_DEP\_TIME|3000000\.0|1327\.0619843333334|485\.8788538345186|1\.0|915\.0|1320\.0|1730\.0|2359\.0|
|DEP\_TIME|2922385\.0|1329\.775913166814|499\.3100515550735|1\.0|916\.0|1323\.0|1739\.0|2400\.0|
|DEP\_DELAY|2922356\.0|10\.123326179288219|49\.251834875076064|-90\.0|-6\.0|-2\.0|6\.0|2966\.0|
|TAXI\_OUT|2921194\.0|16\.643045617648127|9\.192901205790536|1\.0|11\.0|14\.0|19\.0|184\.0|
|WHEELS\_OFF|2921194\.0|1352\.3609886916104|500\.8726874878942|1\.0|931\.0|1336\.0|1752\.0|2400\.0|
|WHEELS\_ON|2920056\.0|1462\.499568501426|527\.2368180480947|1\.0|1049\.0|1501\.0|1908\.0|2400\.0|
|TAXI\_IN|2920056\.0|7\.678982183903322|6\.269639312182482|1\.0|4\.0|6\.0|9\.0|249\.0|
|CRS\_ARR\_TIME|3000000\.0|1490\.5606646666668|511\.5475663438886|1\.0|1107\.0|1516\.0|1919\.0|2400\.0|
|ARR\_TIME|2920058\.0|1466\.511162449513|531\.8383494685141|1\.0|1053\.0|1505\.0|1913\.0|2400\.0|
|ARR\_DELAY|2913802\.0|4\.260858150279257|51\.17482436058268|-96\.0|-16\.0|-7\.0|7\.0|2934\.0|
|CANCELLED|3000000\.0|0\.02638|0\.16026260998639438|0\.0|0\.0|0\.0|0\.0|1\.0|
|DIVERTED|3000000\.0|0\.002352|0\.04844036414290527|0\.0|0\.0|0\.0|0\.0|1\.0|
|CRS\_ELAPSED\_TIME|2999986\.0|142\.27580728710066|71\.55668973499687|1\.0|90\.0|125\.0|172\.0|705\.0|
|ELAPSED\_TIME|2913802\.0|136\.6205411349158|71\.67581550996262|15\.0|84\.0|120\.0|167\.0|739\.0|
|AIR\_TIME|2913802\.0|112\.31083958347205|69\.75484349770514|8\.0|61\.0|95\.0|142\.0|692\.0|
|DISTANCE|3000000\.0|809\.3615516666666|587\.8939382450038|29\.0|377\.0|651\.0|1046\.0|5812\.0|
|DELAY\_DUE\_CARRIER|533863\.0|24\.759086132584578|71\.77184461926316|0\.0|0\.0|4\.0|23\.0|2934\.0|
|DELAY\_DUE\_WEATHER|533863\.0|3\.9852602634009098|32\.41079577067676|0\.0|0\.0|0\.0|0\.0|1653\.0|
|DELAY\_DUE\_NAS|533863\.0|13\.164727654847779|33\.16112154909827|0\.0|0\.0|0\.0|17\.0|1741\.0|
|DELAY\_DUE\_SECURITY|533863\.0|0\.14593069757596985|3\.5820528160364797|0\.0|0\.0|0\.0|0\.0|1185\.0|
|DELAY\_DUE\_LATE\_AIRCRAFT|533863\.0|25\.471281958105358|55\.76689203517002|0\.0|0\.0|0\.0|30\.0|2557\.0|

### Descripción de variables categóricas

|index|count|unique|top|freq|
|---|---|---|---|---|
|FL\_DATE|3000000|1704|2019-07-25|2379|
|AIRLINE|3000000|18|Southwest Airlines Co\.|576470|
|AIRLINE\_DOT|3000000|18|Southwest Airlines Co\.: WN|576470|
|AIRLINE\_CODE|3000000|18|WN|576470|
|ORIGIN|3000000|380|ATL|153556|
|ORIGIN\_CITY|3000000|373|Chicago, IL|157368|
|DEST|3000000|380|ATL|153569|
|DEST\_CITY|3000000|373|Chicago, IL|158087|
|CANCELLATION\_CODE|79140|4|B|28772|

## Criterios de imputación de valores nulos

#### Cantidad de valores nulos en el Data Set
|index|0|
|---|---|
|CANCELLATION\_CODE|2920860|
|DELAY\_DUE\_WEATHER|2466137|
|DELAY\_DUE\_NAS|2466137|
|DELAY\_DUE\_SECURITY|2466137|
|DELAY\_DUE\_LATE\_AIRCRAFT|2466137|
|DELAY\_DUE\_CARRIER|2466137|
|AIR\_TIME|86198|
|ELAPSED\_TIME|86198|
|ARR\_DELAY|86198|
|TAXI\_IN|79944|
|WHEELS\_ON|79944|
|ARR\_TIME|79942|
|TAXI\_OUT|78806|
|WHEELS\_OFF|78806|
|DEP\_DELAY|77644|
|DEP\_TIME|77615|
|CRS\_ELAPSED\_TIME|14|

### Distribución de las variables con valores nulos
<img width="1259" height="913" alt="Image" src="https://github.com/user-attachments/assets/3f2e8627-8391-4173-9344-b436495fcccc" />

<<img width="1245" height="913" alt="Image" src="https://github.com/user-attachments/assets/e3fac722-35e3-4e2e-bae6-fd2a4a88c142" />


## Justificación de la modificación de variables

Dada la distribución de las variables numéricas se aplicaron métodos estadísticos para realizar la imputación de nulos. 

    # Imputación a variables con valores de la moda
    most_frequent_cols = ["ARR_TIME","DEP_TIME"]
    
    # Imputación a variables con valores de la media
    median_cols = ["AIR_TIME",  "ELAPSED_TIME",  "ARR_DELAY",
    "DEP_DELAY","CRS_ELAPSED_TIME"] 
    
    # Imputación a variables explicativas
    xpl_cols = ["DELAY_DUE_CARRIER","DELAY_DUE_WEATHER","DELAY_DUE_NAS",
    "DELAY_DUE_SECURITY","DELAY_DUE_LATE_AIRCRAFT"]
        
    # Imputadores
    mode_imputer = SimpleImputer(strategy="most_frequent") 
    median_imputer = SimpleImputer(strategy="median")
    xpl_imputer = SimpleImputer(strategy="constant", fill_value=0)
      
    # Aplicar imputación
    
    flight_data[median_cols] = median_imputer.fit_transform(flight_data[median_cols])
    
    flight_data[most_frequent_cols] = mode_imputer.fit_transform(flight_data[most_frequent_cols])
    
    flight_data[xpl_cols] = xpl_imputer.fit_transform(flight_data[xpl_cols])

Aplicando este método de imputación el siguiente paso consistió en retirar las variables que, a consideración del análisis, no aportarían gran valor al modelo predictivo.
       
       columns_to_drop = ['CANCELLED',  'CANCELLATION_CODE',  'DOT_CODE','ORIGIN_CITY',  'DEST_CITY',  'TAXI_OUT',  'TAXI_IN','WHEELS_ON',  'WHEELS_OFF',  'DIVERTED']
       # Eliminar las columnas especificadas
       flight_data = flight_data.drop(columns=columns_to_drop, errors='ignore')


## Comprensión estadística del modelo

En el siguiente gráfico se muestra la probabilidad e retrasos por hora del día. Lo que revelan los datos es que, las 3:00 am tiene una mayor probabilidad de retrasos con respecto a las demás horas de la madrugada. Asimismo, el horario con menos probabilidad de encontrar retrasos en las salidas de vuelos es entre 5 am, siendo el mejor horario para no encontrar contratiempos en los vuelos. Por encima de la línea del promedio global, A partir de las 13:00 hrs. se detectan los horarios con mayor probabilidad de tener retrasos en la salida de vuelos. En la sima de estos horarios se observa que los horarios con mayor probabilidad se encuentran entre las 18:00 y 20:00.

<img width="1021" height="559" alt="Image" src="https://github.com/user-attachments/assets/08ea62fa-a7d2-4a88-b4d4-1a2d3937c63d" />

En el análisis estadístico se detectaron cinco de las principales causas de retrasos en vuelos domésticos en los aeropuertos de la región estadounidense. En el siguiente gráfico se expresa la afectación total en minutos que representa cada una de estas causas. A partir de esta información se observa que las afectaciones en la llegada de los aviones a los aeropuertos (DELAY_DUE_LATE_AIRCRAFT) y las operaciones al interior de los aeropuertos (DELAY_DUE_CARRIER) juegan un papel crucial en el tiempo de retrasos.

<img width="977" height="590" alt="Image" src="https://github.com/user-attachments/assets/122aa245-582d-46d6-9f78-7c21282fa9d9" />

Por último, es importante mencionar que del total de vuelos registrados, alrededor del del 18% presentó tiempos de retraso tanto en la salida del vuelo como en su llegada. Esto, en efecto, representa una atenuante para los algoritmos de predicción. En este sentido, se comentó la necesidad de balancear las clases en caso de que el algoritmo así lo requiera.

<img width="640" height="658" alt="Image" src="https://github.com/user-attachments/assets/35c8d2b0-bd7c-4488-9e33-d8a14fc8ea43" />

## Análisis de correlación
Con el objetivo de comprender la relación de las variables de estudio, se realizaron dos análisis de correlación. A partir de esta información se hallaron las variables predictivas del modelo.

<img width="625" height="528" alt="Image" src="https://github.com/user-attachments/assets/cb6dc9eb-df58-4950-99ee-75aa04748315" />

<img width="625" height="528" alt="Image" src="https://github.com/user-attachments/assets/4a8cb0be-f24b-412e-9a28-abcbb55a580d" />

<img width="946" height="864" alt="Image" src="https://github.com/user-attachments/assets/3c5aa3ed-b619-4880-98a1-2e9752e4b29d" />
