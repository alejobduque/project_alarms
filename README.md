### README

Esta prueba de alarmas se desarrolló con el lenguaje de programación **Python**, utilizando el ORM **SQLAlchemy** para realizar la administración de base de datos para la cual se utilizó **PostgreSQL**

#### Funcionamiento

- En el repositorio se encuentra tanto un backup de la base de datos utlizada para el desarrollo, como los scripts requeridos en la prueba los cuales son (Tener en cuenta el nombre de la base de datos, el cual debe ser **db-senior** o en su defecto en el archivo config.json puede modificar la llave _"POSTGRESQL_DB_ALARM"_ para configurar el nombre de la base de datos):
  -- **Creacion.sql**: Creación de la tabla, creación de función para el trigger y el trigger para almacenar _start_date_utc_ o _end_date_utc_ en utc.
  -- **Consulta.sql**: Consulta para obtener las alarmas donde alguna fracción o la totalidad del período de la alarma se encuentre dentro del intervalo escogido por el usuario.

- Antes de iniciar la ejecución del proyecto debe instalar las librerías descritas en el archivo **_requirements.txt_**

- Para la ejecución del proyecto se debe tener en cuenta punto de inicio que es el archivo **app.py**. Este está configurado en la carpeta _.vscode/launch.json_ por si desea utilizar este para su ejecución.

- Una vez realizadas las configuraciones mencionadas anteriormente, puede dar inicio a la ejecución del proyecto.

### Endpoints implementados

- **/get_alarms**:
  -- **method**: GET
  -- **body**: Se debe enviar un json con las claves _start_date_ y _end_date_ en el siguiente formato "dd/mm/Y". A continuación un ejemplo:

```javascript
{
    "start_date": "01/03/2022",
    "end_date": "01/05/2022"
}
```

-- **returns**: Este endpoint regresa la información de las alarmas las cuales se encuentran configuradas al menos en una fracción de tiempo en el intervalo enviado.

- **/add_alarms**:
  -- **method**: POST
  -- **body**: Se debe enviar una lista de diccionarios que contengan la información de las alarmas a añadir: - alarm_name: Requerido - start_date: Requerido - comment: Opcional - start_date_utc: Opcional - end_date_utc: Opcional
  Los campos _start_date_utc_ y _end_date_utc_ deben enviarse en el siguiente formato

```javascript
"dd/mm/Y H:\M:S";
```

    A continuación se presenta un ejemplo

```javascript
[
  {
    alarm_name: "NewAlarm1",
    start_date: "01/03/2022",
  },
  {
    alarm_name: "NewAlarm2",
    start_date: "01/03/2022",
    comment: "Test comment",
  },
  {
    alarm_name: "NewAlarm3",
    start_date: "01/03/2022",
    end_date: "14/05/2022",
    start_date_utc: "01/03/2022 05:00:00",
  },
  {
    alarm_name: "NewAlarm4",
    start_date: "01/03/2022",
    comment: "Test comment",
    end_date: "14/05/2022",
  },
];
```

-- **returns**: Este endpoint regresa los ids de las alarmas que se ingresaron.

- **/delete_alarms**:
  -- **method**: PUT
  -- **body**: Se deben enviar las claves **date** y **oldest**. El campo _date_ establece el punto de referencia para la eliminación lógica y el campo _oldest_ se envía en true si se requiere eliminar los más antiguos, en false si los más nuevos (La eliminación se realiza con base en el startd_date) A continuación un ejemplo:

```javascript
{
    "date": "01/03/2022",
    "oldest": false
}
```

-- **returns**: Este endpoint regresa true si la eliminación lógica se realizó correctamente.
