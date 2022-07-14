#!/usr/bin/env python
# coding: utf-8

# # Script para limpieza de datos PS🪐
# ###### Proyecto Saturno 

# ### Importar Librerias 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt


# ### Carga de los datos 

# datos=pd.read_csv ('C:/Users/braso/Documents/NBIO/Envialo México Prueba/Python test/Conjunto de datos EMX 2022 Listo.csv', header = None)

# In[2]:


datosEMX=pd.read_excel('C:/Users/braso/Documents/NBIO/Envialo México Prueba/Python test/Conjunto de datos EMX 2022 Listo.xlsx')


# datos.head()
# datosEMX.head()

# print(datos.head())

# ### Tratamiento

# In[3]:


datosEMX.describe()


# #### Eliminar el PLANI Duplicado de la columna PLANI

# In[ ]:





# #### Creación de un nuevo df solo con los datos para el análisis

# In[4]:


datosEMXNew = datosEMX[['NUMERO DE FACTURA CARTA PORTE','FECHA DE EMBARQUE','PLANI' ,'TIPO DE EVIDENCIA','OPERADOR','DESTINO','TIPO DE UNIDAD ', 'PLACAS', 'ESTATUS DEL TRANSPORTE','COMENTARIOS TRANSPORTE','MOTIVO DE RECHAZO','CAJAS EMBARCADAS','FECHA ENTREGA TRANSPORTE','HORA CITADA A CARGA','HORA LLEGADA A CARGA']]
datosEMXNew.head()


# #### Colocación del numero de FCP como índice del nuevo df

# In[5]:


datosEMXNew.index = datosEMXNew["FECHA DE EMBARQUE"]


# In[14]:


type(datosEMXNew.index[0])


# In[15]:


datosEMXNew.head()


# #### Selección de fechas

# In[6]:


datosEMXNew = datosEMXNew.loc["2022":]


# In[8]:


datosEMXNew = datosEMXNew.loc["2022-05":]


# In[9]:


datosEMXNew


# #### Cambio de formato de fecha con pandas

# In[12]:


datosEMXNew["FECHA DE EMBARQUE"] = pd.to_datetime(datosEMXNew["FECHA DE EMBARQUE"], format='%d%m%Y')


# In[ ]:





# In[13]:


datosEMXNew.head()


# In[17]:


print(datosEMXNew["FECHA DE EMBARQUE"])


# In[18]:


datosEMXNew.plot(x="FECHA DE EMBARQUE")


# ### Visualización 

# In[19]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.plot(datosEMX[['CAJAS EMBARCADAS','PLANI']])
datosEMX.head()

plt.show()


# ### Exportación de Archivo

# In[14]:


datosEMXNew.to_excel(excel_writer, sheet_name='Sheet1', na_rep=None, float_format=None, columns=None, header=True, index=True, startrow=0, startcol=0, merge_cells=True, inf_rep=inf, verbose=True, 'Conjunto de Datos EMX 2022 Procesados.xlsx')


# In[16]:


datosEMXNew.to_excel(excel_writer,'Conjunto de Datos EMX 2022 Procesados.xlsx', engine='xlsxwriter')


# In[ ]:




