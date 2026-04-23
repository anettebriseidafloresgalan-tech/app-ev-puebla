import streamlit as st

st.title("Simulador de Freno Regenerativo EV - Puebla (Datos Reales)")

st.write("Modelo basado en condiciones reales de la ciudad de Puebla")

# -------------------------
# DATOS DEL VEHÍCULO
# -------------------------
st.header("Datos del vehículo")

modelo = st.text_input("Modelo del vehículo", "BYD Dolphin")

masa = st.number_input("Masa del vehículo (kg)", 800, 4000, 1500)
eficiencia = st.slider("Eficiencia del sistema (%)", 0, 100, 60) / 100

capacidad_bateria = st.number_input("Capacidad de batería (kWh)", 20, 150, 50)

# -------------------------
# CONDICIONES REALES DE PUEBLA
# -------------------------
st.header("Condiciones basadas en Puebla")

st.write("Altitud promedio de Puebla: 2,140 - 2,233 m")
st.write("Pendiente promedio: 2° a 3.5°")
st.write("Temperatura promedio: 17 °C")

distancia = st.number_input("Recorrido diario (km)", 1, 300, 30)

zona = st.selectbox(
    "Tipo de recorrido en Puebla",
    ["Centro (plano)", "Periferia", "Zona con pendiente", "Bajada prolongada"]
)

# Ajustes reales según Puebla
if zona == "Centro (plano)":
    pendiente = 2
    factor_zona = 0.8
elif zona == "Periferia":
    pendiente = 3
    factor_zona = 1.0
elif zona == "Zona con pendiente":
    pendiente = 5
    factor_zona = 1.3
elif zona == "Bajada prolongada":
    pendiente = 8
    factor_zona = 1.6

velocidad = st.number_input("Velocidad promedio (m/s)", 1.0, 40.0, 15.0)
tiempo = st.number_input("Tiempo de manejo (horas)", 0.1, 10.0, 1.0)

# -------------------------
# CÁLCULOS FÍSICOS
# -------------------------
st.header("Cálculos")

# Energía cinética
energia_cinetica = 0.5 * masa * (velocidad ** 2)

# Energía por pendiente (aproximación)
g = 9.81
altura_aprox = distancia * 1000 * (pendiente / 100)
energia_potencial = masa * g * altura_aprox

# Energía total recuperada
energia_total = (energia_cinetica + energia_potencial) * eficiencia * factor_zona

# Conversión a kWh
energia_kwh = energia_total / 3.6e6

# Consumo real promedio EV
consumo_km = 0.15
consumo_total = distancia * consumo_km

# Ahorro semanal
ahorro_semanal = energia_kwh * 7

# Número de cargas
cargas_semana = (consumo_total * 7) / capacidad_bateria

# -------------------------
# RESULTADOS
# -------------------------
st.header("Resultados")

st.subheader("Energía recuperada por día")
st.write(f"{energia_kwh:.4f} kWh")

st.subheader("Ahorro semanal")
st.write(f"{ahorro_semanal:.4f} kWh")

st.subheader("Cargas necesarias por semana")
st.write(f"{cargas_semana:.2f} cargas")

# -------------------------
# FÓRMULAS
# -------------------------
st.header("Fórmulas utilizadas")

st.latex(r"E = \frac{1}{2}mv^2")
st.latex(r"E_p = mgh")
st.latex(r"E_{total} = (E + E_p) \cdot eficiencia")

st.write("Conversión: 1 kWh = 3.6 x 10^6 Joules")

# -------------------------
# INTERPRETACIÓN
# -------------------------
st.header("Interpretación")

if ahorro_semanal < 2:
    st.write("Ahorro bajo")
elif ahorro_semanal < 5:
    st.write("Ahorro moderado")
else:
    st.write("Ahorro alto")

st.write("Las condiciones de Puebla favorecen una regeneración moderada debido a su altitud y pendientes suaves.")