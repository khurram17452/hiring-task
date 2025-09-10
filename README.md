# 🚀 FastAPI + PostgreSQL Hiring Task  

This project demonstrates a production-ready backend setup using **FastAPI**, **PostgreSQL**, and **Docker Compose**.  
It includes database integration, validations, and automatically generated API docs.  

---

## ⚡ Quick Start  
Quickly setup and run the app if you are a pro.

```bash
git clone git@github.com:khurram17452/hiring-task.git
cd hiring-task
echo "DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/fastapi_db" > .env
docker compose build
docker compose up -d
```


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

---

### 2. 🛠 Environment Variables  

Create a `.env` file in the root:  

```ini
DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/fastapi_db

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

### 4. 📖 API Documentation  

FastAPI provides auto-generated docs:  

- Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)  
- ReDoc → [http://localhost:8000/redoc](http://localhost:8000/redoc)  

---

### 5. 🐘 Database Access  

From your host machine:  

```bash
psql -h localhost -U postgres -d fastapi_db
```

Password: `postgres`  

---

### 6. 📜 Example Endpoints  

- `POST /items/` → Create an item  
- `GET /items/` → List all items  
- `GET /items/{id}` → Get item by ID  
- `PUT /items/{id}` → Update item  
- `DELETE /items/{id}` → Delete item  

---

## ✅ Testing Without Docker (Optional)  

If you prefer running locally:  

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Make sure Postgres is running locally and update `.env` accordingly.  

---

## 🏆 Notes  

- Built with **FastAPI**, **SQLAlchemy**, and **Pydantic v2**  
- Uses **Docker Compose** for one-command startup  
- Clean, modular project layout for easy extension  
