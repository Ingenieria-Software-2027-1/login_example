# Módulo de espacios

es una app en  Django que sirve para publicar espacios como anfitrión y  poder revisr los espacios  que existen y están disponibles como "arrendatario"

## Instalación en Ubuntu

 necesité Python 3.12 y Git (ya lo tení)


Comandos que se ejecutaron en mi terminal;
```bash
git clone --branch feature/modulo-espacios https://github.com/BelenDiaz-web/login_example.git
cd login_example
python3 -m venv login_example/.venv
source login_example/.venv/bin/activate
python -m pip install -r requirements.txt
cd login_example
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Al ir a la página de `http://127.0.0.1:8000/admin/` se pueden crear usuarios y asignarles el rol de anfitrión o arrendatario con las opciones para marcar la casilla q se elija

## Como se usa...

- Inicio de sesión: `http://127.0.0.1:8000/cuentas/login/`
- Publicar un espacio como anfitrión: `http://127.0.0.1:8000/espacios/crear/`
- Consultar el catálogo como arrendatario: `http://127.0.0.1:8000/espacios/`

Los espacios publicados aparecen en el catálogo cuando están marcados como disponibles

La restricción de publicación es xitosa, ya que cuando el uusario no es anfitrión tiene que regresarlo a: `/cuentas/dashboard/`

Por eso lo importante es que `/espacios/crear/` pide iniciar sesión cuando no hay una cuenta activa

Por lo tanto se muestra que la restricción por rol si funciona...