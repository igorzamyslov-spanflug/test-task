# Todo Application

A full-stack todo application with a Flask backend and React Router frontend.

## Project Structure

```
├── backend/          # Flask API server
│   ├── app.py       # Main Flask application
│   ├── pyproject.toml
│   └── uv.lock
└── frontend/         # React Router frontend
    ├── package.json
    ├── app/
    │   ├── root.tsx
    │   ├── routes.ts
    │   └── routes/
    └── public/
```

## Prerequisites

- **Python 3.10+** 
- **Node.js 18+**

## Backend Setup

The backend is a Flask API that provides todo management endpoints.

### Installation

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
   
2. Create and activate virtual environment
   ```
         python3 -m venv .venv
         source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   (Alternatively, use `uv` for dependency management)

### Running the Backend

Start the Flask development server:

```bash
python3 app.py
```

(Alternatively run `uv run python app.py` if using `uv`)

The backend will be available at `http://localhost:7999`

## Frontend Setup

The frontend is built with React Router v7 and TypeScript.

### Installation

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

### Running the Frontend

#### Development Mode

Start the development server:

```bash
npm run dev
```

The frontend will be available at `http://localhost:3001`
