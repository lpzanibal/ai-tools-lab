# AI Tools Lab 🤖🛠️🧪

##### Conjunto de herramientas experimentales construidas sobre LLMs para realizar tareas específicas

### Primeros pasos
Clonar el proyecto
```sh
git clone https://github.com/lpzanibal/ai-tools-lab.git
```
Crear y activar el entorno virtual (opcional)
```sh
python -m venv env
env\Scripts\activate.bat # windows con cmd
```
Instalar dependencias
```sh
pip install -r requirements.txt
```
Correr el servidor web
```sh
uvicorn app.api:app --reload
```

Importante: Los documentos .pdf que se van a cargar en el vectorstore deben ir en la carpeta "documents"

### Rutas de la aplicación

| Ruta                         | Método | Descripción                                               |
| ---------------------------- | ------ | --------------------------------------------------------- |
| /qa                          | GET    | UI para interactuar con el documento                      |
| /tools/qa                    | POST   | Realiza la consulta en el documento                       |