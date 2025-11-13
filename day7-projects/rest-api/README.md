# Project 3: REST API

Build a RESTful API with Flask for managing resources.

## Features
- CRUD operations (Create, Read, Update, Delete)
- User authentication
- Input validation
- Error handling
- JSON responses

## Endpoints
```
GET    /api/items       - List all items
GET    /api/items/:id   - Get item by ID
POST   /api/items       - Create new item
PUT    /api/items/:id   - Update item
DELETE /api/items/:id   - Delete item
```

## Implementation
- Flask for web framework
- SQLite for database
- JWT for authentication
- Request validation
- Status codes

## Run
```bash
pip install -r requirements.txt
python src/api.py
pytest tests/ -v
```
