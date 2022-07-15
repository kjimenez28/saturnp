import numpy as np
import pandas as pd
from  datetime import date

# ### Carga de los datos 
datosEMX=pd.read_excel('Seguimiento.xlsx')

### Tratamiento
datosEMXNew = datosEMX[['NUMERO DE FACTURA CARTA PORTE','FECHA DE EMBARQUE','PLANI' ,'TIPO DE EVIDENCIA','OPERADOR','DESTINO','TIPO DE UNIDAD ', 'PLACAS', 'ESTATUS DEL TRANSPORTE','COMENTARIOS TRANSPORTE','MOTIVO DE RECHAZO','CAJAS EMBARCADAS','FECHA ENTREGA TRANSPORTE','HORA CITADA A CARGA','HORA LLEGADA A CARGA']]

# #### Colocación del numero de FCP como índice del nuevo df
datosEMXNew.index = datosEMXNew["FECHA DE EMBARQUE"]

# #### Cambio de formato de fecha con pandas
datosEMXNew["FECHA_EMBARQUE"]=datosEMXNew["FECHA DE EMBARQUE"].dt.strftime('%d%m%Y')

# #### Selección de fechas
mask = (datosEMXNew["FECHA DE EMBARQUE"] > '2022-05-01') & (datosEMXNew["FECHA DE EMBARQUE"] <= date.today().strftime("%Y-%m-%d"))
datosEMXNew=datosEMXNew.loc[mask]

# #### ELIMINAR COLUMNA
datosEMXNew=datosEMXNew.drop(["FECHA DE EMBARQUE"], axis=1)

# #### Eliminar duplicados por PLANI
datosEMXNew=datosEMXNew.drop_duplicates(['PLANI'], keep='last')

# ### Exportación de Archivo
datosEMXNew.to_excel("output.xlsx",sheet_name='Sheet_1')  