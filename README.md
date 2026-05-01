# IPScanner

# 🛡️ Sentinel Network Scanner

**Sentinel** es un escáner de puertos ligero con interfaz gráfica (GUI) desarrollado en Python. Este proyecto está diseñado para ser multiplataforma, funcionando tanto en entornos **Linux (Pop!_OS)** como en **Windows**.

Diseñado por **Diego Galdos (CorteX Desings)** como parte de prácticas de Ingeniería en Sistemas Computacionales.

## 🚀 Características
*   **Interfaz Moderna**: Construida con `CustomTkinter` para un look oscuro y profesional.
*   **Multihilo (Threading)**: El escaneo se ejecuta en segundo plano para evitar que la ventana se congele.
*   **Seguro y Rápido**: Utiliza sockets de Python para una verificación eficiente de puertos comunes.

## 🛠️ Requisitos del Sistema
*   **Python 3.12+**
*   **Tkinter** (Librería base del sistema)
*   **CustomTkinter** (Librería de diseño)

## 📦 Instalación y Uso

### En Linux (Pop!_OS / Ubuntu)
1. Instala la dependencia del sistema:
   ```bash
   sudo apt update && sudo apt install python3-tk
