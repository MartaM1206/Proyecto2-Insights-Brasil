# :moneybag: <span style="color:Green">**Ingresos públicos de Brasil**</span>

:book: <span style="color:lightgreen">**Descripción**</span>

El gobierno de Brasil, a través de sus distintos órganos, gestiona la recaudación de ingresos públicos para financiar los servicios y proyectos que benefician a la sociedad. Cada año, se realiza una planificación detallada para prever cuánto se espera recaudar, pero a menudo la recaudación real difiere de lo previsto debido a diversos factores como la evasión fiscal, fluctuaciones económicas, ineficiencias administrativas, entre otros.

Este proyecto analiza los datos históricos de la ejecución de ingresos entre 2013 y 2021 con los siguientes objetivos:  
- Identificar patrones  
- Detectar áreas problemáticas donde la recaudación ha sido consistentemente menor a lo previsto.
- Proponer recomendaciones basadas en los datos que ayuden a mejorar la precisión de las previsiones y la eficiencia de la recaudación.
        

:file_folder: <span style="color:lightgreen">**Estructura del Proyecto**</span>


        ├── datos/               # Datos crudos
        ├── src/                 # Archivo con funciones de soporte
        ├── Proyecto2/           # Jupyter notebook del proyecto
        ├── README.md            # Descripción del proyecto
     

🛠️ <span style="color:lightgreen">**Instalación y Requisitos**</span>

Este proyecto usa:

    - Python: Versión 3.13.0
    - Jupyter Notebook (ejecutado a través de VSCode)
    - Librerías: pandas, numpy, seaborn, matplotlib



📊 <span style="color:lightgreen">**Resultados y Conclusiones**</span>

**Análisis de ingresos:**  
 - En general, la tendencia en los ingresos es creciente, han aumentado entre 2013 y 2021.

 - La mayor parte de los ingresos corresponde en un 50 % a Receitas Correntes (ingresos regulares por tasas e impuestos habituales) y un 48% a Receitas de Capital (ingresos debidos a la venta de activos del gobierno, préstamos y financiación a largo plazo), por lo que son estas dos categorías las más analizadas.    

**Análisis de discrepancias:**

- Considerando el total de ingresos, exceptuando 2018, 2019 y 2021, el valor previsto es mayor que el realizado y este último experimenta una fuerte caída en 2020, posiblemente debido a la pandemia. 

- Las categorías con mayores discrepancias son Receitas Correntes y Receitas de Capital.

- Parece haber una infra recaudación de los impuestos, lo que provocaría las discrepancias en Receitas Correntes, que además son las que mayor porcentaje de ingresos supone.

- En cuanto a unidades gestoras, la que presenta mayor problemática es la Coordenacao De Orcamento E Financas Do Frgps si consideramos la diferencia absoluta entre ingresos previstos y realizados o la Reserva De Contingencia/Mef si consideramos la diferencia media. Si vamos a nivel de organismo superior, el Ministério Da Economia es el que presenta mayor diferencia total entre valor previsto y valor realizado. Sería conveniente analizar estas unidades gestoras y el Ministério Da Economia para encontrar el origen de la infra recaudación o el error en la planificación de las Receitas de Capital.



🔄 <span style="color:lightgreen">**Próximos Pasos**</span>

- Analizar detalladamente las unidades gestoras con mayores discrepancias, especialmente las dependientes del Ministério Da Economia, para identificar posibles causas de la infra recaudación y poder implementar mejoras en este aspecto



🤝 <span style="color:lightgreen">**Contribuciones**</span>

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un pull request o una issue.
Si necesitas acceso a los archivos puedes escribirme mi correo electrónico: mm.llorden@gmail.com  
También puedes encontrarme en LinkedIn


✒️ <span style="color:lightgreen">**Autores y Agradecimientos**</span>

**Marta María Llordén Alonso** - [@MartaM1206](https://github.com/MartaM1206)
     

