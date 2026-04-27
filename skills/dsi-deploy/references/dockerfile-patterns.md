# Dockerfile Patterns

Use the appropriate pattern based on the project's tech stack. Adapt as needed; these are starting points, not rigid templates.

## Python (uv)

For projects using `pyproject.toml` and `uv`:

```dockerfile
FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY . .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Adjust the CMD for the actual entry point (gunicorn, flask, panel, streamlit, etc.).

## Python (pip/requirements.txt)

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Node.js

```dockerfile
FROM node:22-slim

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci --omit=dev

COPY . .

EXPOSE 3000

CMD ["node", "server.js"]
```

For projects with a build step (Next.js, Vite, etc.), use multi-stage:

```dockerfile
FROM node:22-slim AS build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM node:22-slim

WORKDIR /app

COPY --from=build /app/package.json /app/package-lock.json ./
RUN npm ci --omit=dev

COPY --from=build /app/.next ./.next
COPY --from=build /app/public ./public

EXPOSE 3000

CMD ["npm", "start"]
```

## Go

```dockerfile
FROM golang:1.23 AS build

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 go build -o server .

FROM gcr.io/distroless/static-debian12

COPY --from=build /app/server /server

EXPOSE 8080

CMD ["/server"]
```

## Rust

```dockerfile
FROM rust:1.82 AS build

WORKDIR /app

COPY Cargo.toml Cargo.lock ./
RUN mkdir src && echo "fn main() {}" > src/main.rs && cargo build --release && rm -rf src

COPY . .
RUN cargo build --release

FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*

COPY --from=build /app/target/release/app /usr/local/bin/app

EXPOSE 8080

CMD ["app"]
```

## Static Site (nginx)

For pre-built static files or simple HTML sites:

```dockerfile
FROM nginx:alpine

COPY . /usr/share/nginx/html

EXPOSE 80
```

For sites with a build step:

```dockerfile
FROM node:22-slim AS build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
```

## Python with System Dependencies

For projects needing OS-level packages (e.g., for scientific computing, PDF generation, image processing):

```dockerfile
FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## .dockerignore

Always create a `.dockerignore` alongside the Dockerfile:

```
.git
.env
__pycache__
*.pyc
node_modules
.venv
*.egg-info
.pytest_cache
.mypy_cache
dist
build
```

Adapt based on the project type. The goal is to exclude version control, virtual environments, build artifacts, and secrets from the Docker build context.
