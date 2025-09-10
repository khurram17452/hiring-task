# 🚀 FastAPI + PostgreSQL Hiring Task  

This project demonstrates a production-ready backend setup using **FastAPI**, **PostgreSQL**, and **Docker Compose**.  
It includes database integration, validations, and automatically generated API docs.  

---

## ⚡ Quick Start  
Quickly setup and run the app if you are a pro.

```bash
git clone git@github.com:khurram17452/hiring-task.git
cd hiring-task
echo .env
docker compose build
docker compose up -d
```

---

## 📂 Project Structure  

```
hiring-task/
│── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI entrypoint
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # DB operations
│   ├── database.py      # DB engine/session
│── .env                 # Environment variables
│── requirements.txt     # Python dependencies
│── Dockerfile           # App container setup
│── docker-compose.yml   # Orchestrates app + db
│── README.md            # Documentation
```

---

## ⚙️ Setup Instructions  

### 1. 📦 Prerequisites  
Make sure you have installed:  
- [Docker](https://www.docker.com/)  
- Python 3.10+ (only if you want to run without Docker)  
- Dependencies listed in `requirements.txt` if running locally  

---

### 2. 🛠 Environment Variables  

Create a `.env` file in the root:  

```ini
# .env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=fastapi_db
POSTGRES_PORT=5432
POSTGRES_HOST=db

# For FastAPI connection
DATABASE_URL=postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

```

---

### 3. ▶️ Run with Docker  

Build and start everything (API + Database):  

**1. Clone the repository**  

```bash
git clone git@github.com:khurram17452/hiring-task.git
cd hiring-task
```

**2. Build the Image**  
```bash
docker compose build
```

**3. Run the Container**  
```bash
docker compose up -d
```

The app will now be available at:  
👉 [http://localhost:8000](http://localhost:8000)  

---

## 📖 API Documentation  

FastAPI provides auto-generated docs:  

- Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)  
- ReDoc → [http://localhost:8000/redoc](http://localhost:8000/redoc)  

---

## 🐘 Database Access  

From your host machine:  

```bash
psql -h localhost -U postgres -d fastapi_db
```

Password: `postgres`  

---

## 📜 Example Endpoints  

- `POST /users/` → Create a user  
- `GET /users/` → List all users  
- `GET /users/{id}` → Get user by ID  
- `PUT /users/{id}` → Update user  
- `DELETE /users/{id}` → Delete user  

---

## ✅ Testing Without Docker (Optional)  

If you prefer running locally:  

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Make sure Postgres is running locally and update `.env` accordingly.  

---

## 🧪 How to Test the API  

- **Browser** → Open [http://localhost:8000/docs](http://localhost:8000/docs) and try endpoints interactively.  
- **curl** →  
  ```bash
  curl -X POST http://localhost:8000/users/ -H "Content-Type: application/json" -d '{"name":"Alice","email":"alice@example.com"}'
  curl http://localhost:8000/users/
  ```
- **Postman** → Import `http://localhost:8000/docs` as a collection.  

---

## 🏆 Why This Stack / Approach  

- **FastAPI** → Modern, high-performance web framework with automatic OpenAPI docs.  
- **PostgreSQL** → Reliable, production-grade database with strong support for relational data.  
- **SQLAlchemy ORM** → Clean database access layer with models that map directly to Python classes.  
- **Pydantic v2** → Ensures request/response validation and type safety.  
- **Docker Compose** → One command to start both the API and DB, ensuring consistent environment setup.  
- **Modular Project Structure** → Separation of concerns (API, CRUD, schemas, DB) for maintainability and clarity.  

---

## 🏅 Notes  

- Built with **FastAPI**, **SQLAlchemy**, and **Pydantic v2**  
- Uses **Docker Compose** for one-command startup  
- Clean, modular project layout for easy extension  
