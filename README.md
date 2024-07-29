# Web "Portafolio" en Django

## Descripción
Esta aplicación web, desarrollada con Django, permite gestionar libros, autores y sus categorías. Implementa el patrón MVT (Model-View-Template) y está diseñada para ser un sistema básico para agregar, buscar y listar libros, autores y categorías.

## Requisitos
- Python 3.11.9
- Django 4.2

## Instalación

### Clona el Repositorio
```bash
git clone https://github.com/JulioCisner0s/python-comi-57820
cd Portafolio
```

### Crea un Entorno Virtual
```bash
python -m venv env
source env/bin/activate  # En Windows, usa `env\Scripts\activate`
```

### Instala las Dependencias
```bash
pip install -r requirements.txt
```

### Configura la Base de Datos
Si estás utilizando la base de datos SQLite (por defecto), no es necesario realizar configuraciones adicionales. Si usas otra base de datos, actualiza la configuración en `Portafolio/settings.py`.

### Realiza las Migraciones
```bash
python manage.py migrate
```

### Crea un Superusuario (Opcional)
Para acceder al panel de administración de Django, crea un superusuario con el siguiente comando:
```bash
python manage.py createsuperuser
```
Sigue las instrucciones para ingresar el nombre de usuario, correo electrónico y contraseña.

### Ejecuta el Servidor de Desarrollo
```bash
python manage.py runserver
```
Abre tu navegador y visita [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver la aplicación en funcionamiento.

## Uso

## Estructura del Proyecto
- **Portafolio/**: Directorio del proyecto principal.
  - `settings.py`: Configuración del proyecto Django.
  - `urls.py`: Rutas del proyecto.
  - `wsgi.py`: Punto de entrada WSGI para servidores de aplicaciones.
- **AppCoder/**: Aplicación dentro del proyecto.
  - `models.py`: Definición de los modelos (Autor, Categoría, Libro).
  - `views.py`: Definición de las vistas (funcionalidades).
  - `forms.py`: Formularios para la entrada de datos.
  - `templates/`: Plantillas HTML.
  - `urls.py`: Rutas específicas de la aplicación.

## Contribución
Si deseas contribuir al proyecto, por favor sigue estos pasos:
1. Haz un Fork del Repositorio.
2. Crea una Nueva Rama.
3. Haz tus Cambios.
4. Haz un Pull Request.

Asegúrate de seguir el estilo de código y de agregar pruebas para cualquier nueva funcionalidad.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Puedes usar, modificar y distribuir este software bajo los términos de esta licencia.

## Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:
- **Nombre**: Julio Cisneros
- **Email**: [juliocesarcisnerosrosales@gmail.com](mailto:juliocesarcisnerosrosales@gmail.com)
- **GitHub**: [https://github.com/JulioCisner0s](https://github.com/JulioCisner0s)

---
