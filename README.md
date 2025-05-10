# 💱 Conversor de Monedas en Python

Este proyecto es un **conversor de monedas** hecho en Python. Permite convertir montos entre distintas monedas desde la consola, usando tasas fijas o dinámicas (con API).

---

## ✅ Objetivo

Crear un conversor funcional y modular que pueda evolucionar desde una versión simple por consola hasta una con interfaz gráfica y tasas de cambio actualizadas automáticamente.

---

## 🧭 Fases del proyecto

### 🔹 Fase 1: Conversor básico en consola

**Funcionalidades mínimas:**

- Pedir al usuario una cantidad.
- Pedir la moneda de origen y destino (ej. USD, EUR, MXN).
- Convertir usando tasas fijas predefinidas.
- Mostrar el resultado.

**Extras recomendados:**

- Validación de entradas.
- Modularización con funciones.

---

### 🔹 Fase 2: Tasas de cambio dinámicas

**Opcionales pero recomendadas:**

- Conexión a una API de tasas de cambio (como `ExchangeRate-API`).
- Mostrar tabla con equivalencias.
- Loop de conversiones hasta que el usuario decida salir.

---

### 🔹 Fase 3 (avanzado): Interfaz gráfica

**Para ir más allá:**

- Crear una GUI con `tkinter`.
- Campos para ingresar monto y elegir monedas.
- Botón para convertir y mostrar el resultado.
- Posibilidad de actualizar tasas desde la interfaz.

---

## 🛠️ Tecnologías

- Python 3
- (Opcional) `requests` para llamadas a APIs
- (Opcional) `tkinter` para interfaz gráfica