import streamlit as st
import pandas as pd
import numpy as np
import statsmodels as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="ticks", color_codes=True)

st.title('Elastic price based on history')
st.text('This is a app for the optimal prices')

uploaded_file = st.file_uploader('Upload your file here')
if uploaded_file:
	data = pd.read_csv(uploaded_file,sep=";",parse_dates=[10],dayfirst=True)
	df_cantidad=(data.groupby(['Día de semana de fecha_venta','Hora de turno','descuento','fecha_venta','tipo_servicio','precio'])['id_reserva'].count().reset_index(name='cantidad'))
	model = ols("cantidad ~ precio_total", df_cantidad).fit()
	precio_minimo = df_cantidad.precio_total.min() - 1
	precio_maximo = df_cantidad.precio_total.max() + 10
	test = pd.DataFrame(columns = ["precio_total", "cantidad"])
	test['precio_total'] = np.arange(precio_minimo, precio_maximo,0.01)
	test['cantidad'] = modelos['tipo_servicio_3'].predict(test['precio_total'])
	test['ingresos'] = test["precio_total"]  * test["cantidad"]
	test['P'] = (test['precio_total']-test['precio_total'].mean())/(test['precio_total'].max()-test['precio_total'].min())
	test['C'] = (test['cantidad']-test['cantidad'].mean())/(test['cantidad'].max()-test['cantidad'].min())
	test['I'] = (test['ingresos']-test['ingresos'].mean())/(test['ingresos'].max()-test['ingresos'].min())
	test[['P','C','I']].plot(figsize=(12,8),title='Estasticidad del precio - tipo_servicio 3')
	ing = np.where(test['ingresos'] == test['ingresos'].max())[0][0]
	valores_maximo_beneficio = test.drop(['P','C','I'],axis=1).iloc[[ing]]
	print("Valores optimos:")
	print(valores_maximo_beneficio)
