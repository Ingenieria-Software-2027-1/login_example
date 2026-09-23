# Práctica 03 - Módulo de Espacios (Django)

Este repositorio contiene la implementación del módulo de gestión de espacios para anfitriones y catálogo para arrendatarios.

---

## Requisitos Previos

* Python 3.10 o superior instalado.
* Git instalado.

---

## Instrucciones para Levantamiento Local

### 1. Clonar el Repositorio

` ` `bash
git clone https://github.com/TU_USUARIO/login_example.git
cd login_example
` ` `

### 2. Crear y Activar el Entorno Virtual

* **Linux / macOS:**
  ` ` `bash
  python3 -m venv venv
  source venv/bin/activate
  ` ` `
* **Windows:**
  ` ` `cmd
  python -m venv venv
  venv\Scripts\activate
  ` ` `

### 3. Instalar Dependencias

` ` `bash
pip install -r requirements.txt
` ` `

### 4. Preparar la Base de Datos

Ejecuta las migraciones para crear la estructura de tablas inicial y del módulo de espacios:

` ` `bash
python manage.py migrate
` ` `

---

##Gestión de Usuarios de Prueba

El proyecto **no incluye un formulario público de registro de usuarios (sign up)**. Por lo tanto, el alta y administración de usuarios (Anfitriones y Arrendatarios) debe realizarse a través del **Panel Administrativo de Django**:

1. **Crear el Superusuario / Administrador:**
   ` ` `bash
   python manage.py createsuperuser
   ` ` `
2. **Iniciar el servidor local:**
   ` ` `bash
   python manage.py runserver
   ` ` `
3. **Dar de alta usuarios desde el Admin:**
   * Entra a `http://127.0.0.1:8000/admin/` en tu navegador.
   * Inicia sesión con el superusuario recién creado.
   * Ve a la sección **Usuarios** (`Users`) y haz clic en **Añadir usuario**.
   * Crea un usuario de prueba para cada rol:
     * **Anfitrión:** Asegúrate de marcar el atributo correspondiente a anfitrión (`is_host` o rol equivalente).
     * **Arrendatario:** Crea un usuario estándar sin privilegios de anfitrión.

---

## Rutas Principales de la Aplicación

* **Catálogo de Espacios (Arrendatarios):** `http://127.0.0.1:8000/espacios/catalogo/`
* **Formulario de Registro (Anfitriones):** `http://127.0.0.1:8000/espacios/crear/`
* **Panel de Administración:** `http://127.0.0.1:8000/admin/`