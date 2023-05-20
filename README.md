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
env\Scripts\activate # windows
```

Instalar dependencias

```sh
pip install -r requirements.txt
```

Crear y poblar el vectorstore, utilizando resources/document.pdf y cualquier .pdf en /documents

```sh
py setup_vector_db.py
```

Correr el servidor web

```sh
uvicorn app.api:app --reload
```

Importante: Los documentos .pdf que se van a cargar en el vectorstore deben ir en la carpeta "documents"

### Rutas de la aplicación

| Ruta               | Método | Descripción                                         |
| ------------------ | ------ | --------------------------------------------------- |
| /document-qa       | GET    | UI para interactuar con el documento                |
| /query-db          | GET    | UI para interactuar con la base de datos            |
| /hf/prompt         | GET    | UI para interactuar con un modelo de HF selccionado |
| /tools/document-qa | POST   | Realiza la consulta en el documento                 |
| /tools/query-db    | POST   | Realiza la consulta a la base de datos              |
| /tools/hf/prompt   | POST   | Envía una prompt al LLM de HF seleccionado          |
