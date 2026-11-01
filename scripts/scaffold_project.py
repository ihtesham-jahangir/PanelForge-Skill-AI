"""Scaffold a PanelForge full-stack application without overwriting files."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "frontend/package.json": """{
  "name": "panelforge-frontend",
  "private": true,
  "scripts": {"dev": "next dev", "build": "next build", "lint": "next lint"},
  "dependencies": {"next": "latest", "react": "latest", "react-dom": "latest"},
  "devDependencies": {"@types/node": "latest", "@types/react": "latest", "typescript": "latest", "autoprefixer": "latest", "postcss": "latest", "tailwindcss": "^3.4.17"}
}
""",
    "frontend/app/layout.tsx": """import "./globals.css";

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
""",
    "frontend/app/page.tsx": """export default function Home() {
  return <main className="min-h-screen p-8"><h1 className="text-3xl font-bold">PanelForge application</h1></main>;
}
""",
    "frontend/app/globals.css": """@tailwind base;
@tailwind components;
@tailwind utilities;
""",
    "frontend/tsconfig.json": """{
  "compilerOptions": {"target": "ES2020", "lib": ["dom", "esnext"], "strict": true, "noEmit": true, "jsx": "preserve", "module": "esnext", "moduleResolution": "bundler", "esModuleInterop": true, "isolatedModules": true},
  "include": ["**/*.ts", "**/*.tsx"]
}
""",
    "frontend/tailwind.config.ts": """import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: { extend: {} },
  plugins: [],
};

export default config;
""",
    "frontend/postcss.config.mjs": """export default {
  plugins: { tailwindcss: {}, autoprefixer: {} },
};
""",
    "frontend/lib/api.ts": """const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export async function getHealth(): Promise<{ status: string }> {
  const response = await fetch(`${API_URL}/health`, { cache: "no-store" });
  if (!response.ok) throw new Error("API request failed");
  return response.json();
}
""",
    "frontend/Dockerfile": """FROM node:22-alpine
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev", "--", "--hostname", "0.0.0.0"]
""",
    "backend/pyproject.toml": """[project]
name = "panelforge-backend"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
  "fastapi",
  "uvicorn[standard]",
  "pydantic",
  "sqlalchemy>=2.0",
  "alembic",
  "psycopg[binary]"
]

[tool.pytest.ini_options]
testpaths = ["tests"]
""",
    "backend/app/main.py": """from fastapi import FastAPI

app = FastAPI(title="PanelForge API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
""",
    "backend/app/__init__.py": "",
    "backend/alembic.ini": """[alembic]
script_location = alembic
sqlalchemy.url = %(DATABASE_URL)s
""",
    "backend/alembic/env.py": """from alembic import context

config = context.config


def run_migrations() -> None:
    context.configure(url=config.get_main_option("sqlalchemy.url"), target_metadata=None)
    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations()
else:
    run_migrations()
""",
    "backend/tests/test_health.py": """from fastapi.testclient import TestClient

from app.main import app


def test_health() -> None:
    response = TestClient(app).get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
""",
    "backend/Dockerfile": """FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml ./
RUN pip install --no-cache-dir fastapi uvicorn[standard] pydantic 'sqlalchemy>=2.0' alembic 'psycopg[binary]' pytest
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
""",
    "database/README.md": """# PostgreSQL

The backend connects to PostgreSQL through SQLAlchemy 2.0. Store the connection
URL in `DATABASE_URL`; manage schema changes with Alembic migrations.
""",
    "docker-compose.yml": """services:
  frontend:
    build: ./frontend
    ports: ["3000:3000"]
  backend:
    build: ./backend
    ports: ["8000:8000"]
    environment:
      DATABASE_URL: ${DATABASE_URL}
    depends_on:
      postgres:
        condition: service_healthy
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: ${POSTGRES_DB:-app}
      POSTGRES_USER: ${POSTGRES_USER:-app}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:?Set POSTGRES_PASSWORD}
    volumes: [postgres-data:/var/lib/postgresql/data]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-app} -d ${POSTGRES_DB:-app}"]
      interval: 5s
      timeout: 5s
      retries: 10

volumes:
  postgres-data:
""",
    ".env.example": """DATABASE_URL=postgresql+psycopg://app:change-me@postgres:5432/app
POSTGRES_DB=app
POSTGRES_USER=app
POSTGRES_PASSWORD=change-me
""",
    "README.md": """# PanelForge application

This project uses a separate Next.js/React/TypeScript/Tailwind CSS frontend,
Python/FastAPI backend, and PostgreSQL database. The frontend communicates with
the backend through documented REST APIs. Add authentication, authorization,
tenant isolation, migrations, and domain tests before production deployment.

## Local development

1. Copy `.env.example` to `.env` and set a non-default database password.
2. Start PostgreSQL with `docker compose up postgres`.
3. Run the API with `uvicorn app.main:app --app-dir backend --reload --port 8000`.
4. Run the frontend with `npm install && npm run dev --prefix frontend`.

The starter API documents its contract at `http://localhost:8000/docs` and
exposes `GET /health`. Keep business logic and authorization in FastAPI.
""",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="Directory to scaffold")
    parser.add_argument("--dry-run", action="store_true", help="List files without writing")
    args = parser.parse_args()
    target = args.target.expanduser().resolve()
    existing = [path for path in FILES if (target / path).exists()]
    if existing:
        print("Refusing to overwrite existing files:")
        print("\n".join(f"- {path}" for path in existing))
        return 2
    if args.dry_run:
        print(f"Would scaffold {len(FILES)} files in {target}")
        return 0
    for relative, content in FILES.items():
        path = target / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Scaffolded {len(FILES)} files in {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
