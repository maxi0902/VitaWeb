import streamlit as st
from datetime import date
#CAMBIAR LOS COLORES DE MODO CLARO, COLOCAR % AL MONTO DE PIE, REVISAR PORQUE NO SALE AUTOFIN
st.markdown("""
<style>
    /* Estilo del cuerpo de la página */
    .stApp {
        background-color: #F2F2F2;
        color: #333333;
    }
    /* Estilo para la barra lateral (sidebar) */
    .stSidebar {
        background-color: #000000; /* Color de fondo oscuro, casi negro */
        color: #F2F2F2; /* Color de las letras, blanco-grisáceo claro */
    }
    
    /* Estilo para el título de la barra lateral */
    .stSidebar .css-1d391kg h2 {
        color: #F2F2F2; /* Asegura el color del título de sección */
    }
    
    /* Estilo para los títulos de las entradas (Año de Nacimiento, etc.) */
    .stSidebar .st-ag {
        color: #F2F2F2;
    }
    
    /* Estilo para el texto de los checkboxes */
    .stSidebar .st-bb {
        color: #F2F2F2;
    }

    .results-container {
        height: 400px; /* <--- Ajusta esta altura a tu gusto */
        overflow-y: auto;
    }
    st.set_page_config(layout="wide")

    /* Estilos generales para ambos modos */
    body {
        color: #2e4053; /* Color de texto base (azul oscuro) */
        background-color: #f2f2f2; /* Color de fondo claro */
    }

    /* Estilo para los títulos (h1, h2, h3) */
    h1, h2, h3, h4, h5, h6 {
        color: #f2f2f2; /* Color azul más oscuro para títulos */
    }

    /* Estilo para el texto dentro del expander/contenedor */
    .st-emotion-cache-1r4qj8m { /* Clase de Streamlit para el texto de st.write */
        color: #f2f2f2; /* Color de texto oscuro para mayor legibilidad */
    }

    /* Estilos específicos para el MODO OSCURO */
    @media (prefers-color-scheme: dark) {
        body {
            color: #f2f2f2; /* Texto claro en modo oscuro */
            background-color: #f2f2f2; /* Fondo oscuro en modo oscuro */
        }
        
        .st-emotion-cache-1r4qj8m {
            color: #d6eaf8; /* Texto claro para los resultados en modo oscuro */
        }
    }

    /* Estilo para los iconos de validación (el círculo verde y rojo) */
    /* Para asegurar que se vean bien en cualquier modo */
    .st-emotion-cache-1r4qj8m > p {
        color: inherit !important;
    }

    /* Cambia el color de la barra del sidebar */
    .st-emotion-cache-1j03l40 {
        background-color: #2c3e50 !important;
    }

    /* Cambia el color del texto en el sidebar */
    .st-emotion-cache-1d388s2, .st-emotion-cache-79elbk {
        color: #d6eaf8 !important;
    }

    /* Cambia el color de los números en los inputs del sidebar */
    .st-emotion-cache-q0n6l8, .st-emotion-cache-116h11g {
        color: #1a5276 !important;
    }
    /* 🟢 ESTILO ESPECÍFICO PARA EL MENSAJE DE ÉXITO (EL CUADRO VERDE) 🟢 */
    div[data-testid="stAlert"] {
        background-color: #4caf50 !important; /* Un verde claro menos intenso */
        color: #000000 !important; /* Un verde más oscuro para el texto */
    }
    /* 🟢 ESTILO DE MENSAJE DE ÉXITO EN MODO OSCURO 🟢 */
        div[data-testid="stAlert"] {
            background-color: #4caf50 !important; /* Verde medio para el fondo */
            color: #ffffff !important; /* Texto blanco */
    }
</style>
""", unsafe_allow_html=True)
# ======================================================================
# LOGICA DE VALIDACION BASADA EN TABLAS
# ======================================================================

# ======================================================================
# LOGICA DE VALIDACION BASADA EN TABLAS
# ======================================================================
#Perfil financiero:  
##Año del vehículo:  
#Valor de venta:  
#Pie:  
#Monto a financiar:  
#¿Acredita ingresos?:  


def obtener_opciones_viables(cliente):
    opciones = {}
    
    reglas = {
        # CREDITOS CONVENCIONALES
        "AUTOFIN CONVENCIONAL": {
            "tipo_credito": "Convencional",
            "ano_min_vehiculo": 2017,
            "pie_min": {"bancarizado": {"sin_casa": 0.35, "con_casa": 0.35}, "no_bancarizado": {"sin_casa": 0.35, "con_casa": 0.35}},
            "monto_max": {"bancarizado": {"sin_casa": 11700000, "con_casa": 11700000}, "no_bancarizado": {"sin_casa": 11700000, "con_casa": 11700000}},
            "edad_rango": range(25, 31),
            "otros_req": {"casa_no": True, "auto_no": True}
        },
        "SANTANDER CONVENCIONAL": {
            "tipo_credito": "Convencional",
            "ano_min_vehiculo": 2015,
            "pie_min": {"bancarizado": {"sin_casa": 0.3, "con_casa": 0.3}, "no_bancarizado": {"sin_casa": 0.3, "con_casa": 0.3}},
            "monto_max": {"bancarizado": {"sin_casa": 30000000, "con_casa": 30000000}, "no_bancarizado": {"sin_casa": 30000000, "con_casa": 30000000}},
            "edad_rango": range(21, 85),
            "otros_req": {}
        },
        "FALABELLA CONVENCIONAL": {
            "tipo_credito": "Convencional",
            "ano_min_vehiculo": 2015,
            "pie_min": {"bancarizado": {"sin_casa": 0.3, "con_casa": 0.3}, "no_bancarizado": {"sin_casa": 0.3, "con_casa": 0.3}},
            "monto_max": {"bancarizado": {"sin_casa": 20000000, "con_casa": 20000000}, "no_bancarizado": {"sin_casa": 20000000, "con_casa": 20000000}},
            "edad_rango": range(21, 85),
            "otros_req": {}
        },
        "FORUM CONVENCIONAL": {
            "tipo_credito": "Convencional",
            "ano_min_vehiculo": 2014,
            "pie_min": {"bancarizado": {"sin_casa": 0.3, "con_casa": 0.3}, "no_bancarizado": {"sin_casa": 0.3, "con_casa": 0.3}},
            "monto_max": {"bancarizado": {"sin_casa": 20000000, "con_casa": 20000000}, "no_bancarizado": {"sin_casa": 20000000, "con_casa": 20000000}},
            "edad_rango": range(21, 85),
            "otros_req": {}
        },
        "BANCALCALLE CONVENCIONAL": {
            "tipo_credito": "Convencional",
            "ano_min_vehiculo": 2015,
            "pie_min": {"bancarizado": {"sin_casa": 0.2, "con_casa": 0.2}, "no_bancarizado": {"sin_casa": 0.2, "con_casa": 0.2}},
            "monto_max": {"bancarizado": {"sin_casa": 20000000, "con_casa": 20000000}, "no_bancarizado": {"sin_casa": 20000000, "con_casa": 20000000}},
            "edad_rango": range(21, 85),
            "otros_req": {}
        },
        
        # CREDITOS EXPRESS
        "AUTOFIN EXPRESS": {
            "tipo_credito": "Express",
            "ano_min_vehiculo": 2014,
            "pie_min": {"bancarizado": 0.4, "no_bancarizado": 0.5},
            "monto_max": {"bancarizado": 30000000, "no_bancarizado": 8000000},
            "edad_rango": range(21, 85),
            "otros_req": {}
        },
        "TANNER EXPRESS": {
            "tipo_credito": "Express",
            "ano_min_vehiculo": 2015,
            "pie_min": {"bancarizado": 0.3, "no_bancarizado": 0.3},
            "monto_max": {"bancarizado": 17000000, "no_bancarizado": "5-7 veces renta"},
            "edad_rango": range(21, 85),
            "otros_req": {}
        },
        "FORUM EXPRESS": {
            "tipo_credito": "Express",
            "ano_min_vehiculo": 2014,
            "pie_min": {"bancarizado": 0.3, "no_bancarizado": 0.3},
            "monto_max": {"bancarizado": 20000000, "no_bancarizado": 10000000},
            "edad_rango": range(21, 85),
            "otros_req": {}
        },
        "SANTANDER BANCO EXPRESS": {
            "tipo_credito": "Express",
            "ano_min_vehiculo": 2014,
            "pie_min": {"bancarizado": 0.3, "no_bancarizado": 0.3},
            "monto_max": {"bancarizado": 18000000, "no_bancarizado": 18000000},
            "edad_rango": range(21, 85),
            "otros_req": {}
        },
        "BANCALCALLE EXPRESS": {
            "tipo_credito": "Express",
            "ano_min_vehiculo": 2015,
            "pie_min": {"bancarizado": 0.2, "no_bancarizado": 0.2},
            "monto_max": {"bancarizado": 18000000, "no_bancarizado": 18000000},
            "edad_rango": range(21, 85),
            "otros_req": {}
        },
    }
    
    opciones_viables = {}

    for nombre, reglas_financiera in reglas.items():
        es_viable = True
        
        # 1. Validación de año del vehículo
        if cliente['ano_del_vehiculo'] < reglas_financiera['ano_min_vehiculo']:
            es_viable = False
        
        # 2. Validación de pie mínimo y bancarización
        tipo_cliente = "bancarizado" if cliente['bancarizado'] else "no_bancarizado"
        
        pie_min_regla = reglas_financiera['pie_min'][tipo_cliente]
        if isinstance(pie_min_regla, dict):
            estado_casa = "con_casa" if cliente['tiene_casa'] else "sin_casa"
            pie_minimo = pie_min_regla[estado_casa]
        else:
            pie_minimo = pie_min_regla

        if cliente['pie_porcentaje'] < pie_minimo:
            es_viable = False

        # 3. Validación de monto máximo a financiar
        monto_max_regla = reglas_financiera['monto_max'][tipo_cliente]
        if isinstance(monto_max_regla, dict):
            estado_casa = "con_casa" if cliente['tiene_casa'] else "sin_casa"
            monto_max = monto_max_regla[estado_casa]
        else:
            monto_max = monto_max_regla

        if isinstance(monto_max, str) and "veces renta" in monto_max:
            multiplicador = int(monto_max.split('-')[1].split(' ')[0])
            monto_max_calculado = cliente['renta_liquida'] * multiplicador
            if cliente['monto_solicitado'] > monto_max_calculado:
                es_viable = False
        elif isinstance(monto_max, (int, float)) and cliente['monto_solicitado'] > monto_max:
            es_viable = False
        
        # 4. Validación de edad
        if cliente['edad'] not in reglas_financiera['edad_rango']:
            es_viable = False

        # 5. Validación de otros requisitos (ej. No tener casa o auto)
        if 'otros_req' in reglas_financiera:
            if reglas_financiera['otros_req'].get('casa_no') and cliente['tiene_casa']:
                es_viable = False
            if reglas_financiera['otros_req'].get('auto_no') and cliente['tiene_auto']:
                es_viable = False
                
        # Si todas las validaciones pasan, agregar a las opciones viables
        if es_viable:
            opciones_viables[nombre] = {
                "tipo_credito": reglas_financiera['tipo_credito'],
                "pie_minimo": pie_minimo,
                "monto_maximo": monto_max
            }
    
    return opciones_viables

# ======================================================================
# INTERFAZ GRAFICA (GUI)
# ======================================================================


# Logo
st.image("assets/vita.jpg", width=400)
st.title("asd")

st.sidebar.title("Datos del Cliente")
st.sidebar.markdown("---")

# Perfil financiero (Bancarizado)
perfil_financiero = st.sidebar.selectbox(
    "Perfil financiero:",
    ["Bancarizado", "No Bancarizado"]
)
es_bancarizado = perfil_financiero == "Bancarizado"

# Edad del cliente
edad = st.sidebar.number_input(
    "Edad del cliente:",
    min_value=18,
    max_value=100,
    value=30,
    step=1
)

# Año del vehículo
ano_del_vehiculo = st.sidebar.number_input(
    "Año del vehículo:",
    min_value=1990,
    max_value=2025,
    value=2020,
    step=1
)

# Valor de venta
valor_de_venta = st.sidebar.number_input(
    "Valor de venta (en $):",
    min_value=100000,
    value=15000000,
    step=100000
)

pie = st.sidebar.number_input(
    "Pie en $:",
    min_value=0,
    value=3000000,
    step=100000
)

# Renta líquida
renta_liquida = st.sidebar.number_input(
    "Renta líquida (en $):",
    min_value=0,
    value=800000,
    step=50000
)

# Preguntar si tiene casa
tiene_casa = st.sidebar.selectbox(
    "¿Tiene casa propia?:",
    ["Sí", "No"]
) == "Sí"

# Preguntar si tiene auto
tiene_auto = st.sidebar.selectbox(
    "¿Tiene auto a su nombre?:",
    ["Sí", "No"]
) == "Sí"

monto_a_financiar = valor_de_venta - pie
pie_porcentaje = (pie / valor_de_venta) * 100 if valor_de_venta > 0 else 0
st.sidebar.write(f"**Monto a financiar (automático):** ${monto_a_financiar:,.0f}")
st.sidebar.write(f"**Pie (automático):** {pie_porcentaje:.2f}%")

cliente = {
    "edad": edad,
    "bancarizado": es_bancarizado,
    "ano_del_vehiculo": ano_del_vehiculo,
    "valor_de_venta": valor_de_venta,
    "pie_monto": pie,
    "monto_solicitado": monto_a_financiar,
    "renta_liquida": renta_liquida,
    "tiene_casa": tiene_casa,
    "tiene_auto": tiene_auto,
    "pie_porcentaje": pie / valor_de_venta if valor_de_venta > 0 else 0
}


st.subheader("Opciones de Financiamiento Viables")

opciones_viables = obtener_opciones_viables(cliente)

if opciones_viables:
    st.success(f"¡Felicitaciones! Tu cliente puede optar por un crédito en {len(opciones_viables)} financieras.")
    
    for nombre_financiera, detalles in opciones_viables.items():
        with st.expander(f"**{nombre_financiera}**"):
            st.write(f"- Tipo de Crédito: **{detalles['tipo_credito']}**")
            st.write(f"- Pie Mínimo: **{int(detalles['pie_minimo'] * 100)}%**")
            monto_max = detalles['monto_maximo']
            if isinstance(monto_max, (int, float)):
                st.write(f"- Monto Máximo a Financiar: **${monto_max:,.0f}**")
            else:
                st.write(f"- Monto Máximo a Financiar: **{monto_max}**")
else:
    st.error("Lo siento, tu cliente no cumple con los requisitos para ninguna financiera.")

    st.info("Intenta ajustar los datos del cliente para ver si califica en alguna opción.")














