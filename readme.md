# Mi Proyecto Django: Chatbot con OpenAI

## Descripción  
Este proyecto es una aplicación web en Django que incluye:  
- Una página **Home** con la descripción general del proyecto.  
- Un perfil de usuario (**Profile**) donde el usuario registrado puede actualizar su nombre y correo.  
- Un chat (**Chat**) integrado con la API de OpenAI (ChatGPT).  
- Una lista de todos los **Users** registrados.  
- Una sección **About Me** con información sobre el autor.

---

## Tecnologías  
- **Backend**: Python 3.10+, Django 5.2  
- **Frontend**: HTML5, Bootstrap 
- **API**: OpenAI Python SDK (`openai`)  
- **Base de datos**: SQLite.  

---

## Vistas / URL  
| Nombre de la vista | URL estándar          | Descripción                                    |
|--------------------|-----------------------|------------------------------------------------|
| Home               | `/` o `{% url 'home' %}`    | Página inicial con descripción del proyecto.   |
| Profile            | `/profile/`           | Perfil del usuario; permite editar nombre y email. |
| Chat               | `/chat/`              | Interfaz de chat que envía y recibe mensajes de OpenAI. |
| Users              | `/users/`             | Listado de todos los usuarios registrados.     |
| About Me           | `/about/`             | Página “Sobre mí”.   |
| Login              | `/login/`             | Página para logearte.   |
| Register           | `/register/`          | Puedes registrarte aquí.   |

## Enlace del video
https://drive.google.com/drive/folders/1mlgBMnrgDiHCedJqAPHY-tqqrZHZYGoh?usp=sharing

Sebastián López
Full Stack Developer