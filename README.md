
# Proyecto Reviglio Schwartz Lozano
Miniblog es una aplicación de blog básica construida con Django por los Alumnos Reviglio, Schwartz y Lozano.

### Caracteristicas:
- Registro y gestión de usuarios
- Creación, edición y eliminación de posts
- Gestión de categorías
- Agregar y ver comentarios en los posts

### Instalacion:
1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual: `python3 -m venv venv`
3. Activa el entorno virtual: `source venv/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Realiza las migraciones de la base de datos: `python manage.py migrate`

### Inicializacion:
1. Inicia el servidor de desarrollo: `python manage.py runserver`
2. Accede a la aplicación en tu navegador: `http://127.0.0.1:8000/home`

### Credenciales para ingresar al administrador de Django
- Usuario: admin
- Contraseña: admin

## Nuevas Funcionalidades
Este proyecto es una aplicación de miniblog que ha sido extendido para incluir una API utilizando Django Rest Framework. A continuación, se detallan las nuevas funcionalidades y cambios realizados.

### 1. API para el Miniblog

Se ha implementado una API utilizando `ModelViewSet` para los modelos `Categoria` y `Post`. A continuación, se detallan los endpoints disponibles:

- **Categorías:**
  - Crear nueva categoría: `POST /api/categorias/`
  - Obtener lista de categorías: `GET /api/categorias/`

- **Posts:**
  - Crear nuevo post: `POST /api/posts/`
  - Obtener lista de posts: `GET /api/posts/`

### 2. Pruebas Adicionales con pytest

Se han agregado pruebas adicionales utilizando `pytest` para cubrir las nuevas funcionalidades y la lógica de la API. Puedes ejecutar las pruebas con el siguiente comando:

```bash
pytest Proyecto_Reviglio_Schwartz_Lozano/miniblog/tests/
```

### 3. Actualización del README

Este README se ha actualizado para reflejar los cambios realizados en el proyecto. Asegúrate de seguir las instrucciones proporcionadas para configurar y utilizar la API.

## Uso de la API

### Endpoints Disponibles

- Categorías:
  - Crear nueva categoría: `POST /api/categorias/`
  - Obtener lista de categorías: `GET /api/categorias/`

- Posts:
  - Crear nuevo post: `POST /api/posts/`
  - Obtener lista de posts: `GET /api/posts/`

### Autenticación en la API y en vistas editar, crear, eliminar del Miniblog

- Autenticación en el Administrador de Django:
Las vistas en views.py dentro de la aplicación miniblog ahora requieren que los usuarios estén autenticados para acceder. Se ha utilizado el decorador @login_required para implementar esta funcionalidad.

- Autenticación en la API:
La API ahora utiliza SessionAuthentication en lugar de TokenAuthentication para requerir que los usuarios inicien sesión en cada sesión del navegador. Esto se ha configurado en el archivo settings.py.



## Ejecución del Proyecto

1. Asegúrate de tener todas las dependencias instaladas:

```bash
pip install -r requeriments.txt
```

2. Realiza las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

3. Ejecuta el proyecto:

```bash
python manage.py runserver
```
=======
# efi-mini-blog

