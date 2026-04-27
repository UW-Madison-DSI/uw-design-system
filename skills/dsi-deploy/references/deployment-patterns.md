# Deployment Patterns

## Decision Tree

Use this to determine which deployment pattern fits a project.

```
Does the project need a database, cache, or other backend service?
├── NO  --> Single Network Pattern
└── YES
    ├── Is the backend service managed externally (e.g., cloud DB, shared instance)?
    │   └── YES --> Single Network Pattern (connect to external service via env vars)
    └── NO (backend runs alongside the app)
        └── Multi-Network Pattern
```

## Pattern 1: Single Network

**Use when:** The application is self-contained or connects to external services via URLs/env vars.

**Examples:**
- Static site served by nginx
- API server that connects to an external database
- Web app with embedded SQLite
- Proxy or gateway service
- Dashboard that reads from external data sources

**Characteristics:**
- One or more services, all on `traefik_network`
- No `internal_network` needed
- Simpler configuration

## Pattern 2: Multi-Network

**Use when:** The deployment includes backend services (databases, caches, workers) that should NOT be accessible from the internet.

**Examples:**
- Web app + PostgreSQL database
- API server + Redis cache
- Frontend + backend API + database
- Application + background worker + message queue

**Characteristics:**
- Public-facing services join both `traefik_network` and `internal_network`
- Backend services join only `internal_network`
- Requires `traefik.docker.network=traefik_network` label on public services
- Services communicate via Docker DNS (service name as hostname)

## Common Deployment Architectures

### Web Application + Database

```
[Internet] --> [Traefik] --> [Web App] --> [Database]
                              (both nets)   (internal only)
```

- Web app: `traefik_network` + `internal_network`
- Database: `internal_network` only
- Web app connects to database via service name (e.g., `postgres:5432`)

### API + Frontend (separate containers)

```
[Internet] --> [Traefik] --> [Frontend (serves static)]
                         --> [API Server] --> [Database]
```

Options:
- **Option A**: Single domain, frontend proxies API requests. Only frontend needs Traefik labels.
- **Option B**: Two subdomains (e.g., `app.services.dsi.wisc.edu` and `api-app.services.dsi.wisc.edu`). Both get Traefik labels with different router names.

### Static Site

```
[Internet] --> [Traefik] --> [nginx serving static files]
```

- Single network
- Use `nginx:alpine` or similar as base image
- Copy built assets into the container

### Background Worker Pattern

```
[Internet] --> [Traefik] --> [Web App] --> [Queue] --> [Worker]
                              (both nets)   (internal)  (internal)
```

- Only the web app gets Traefik labels
- Queue (Redis, RabbitMQ) and worker are internal only

## Port Mapping

Traefik auto-detects the container's exposed port. If the container exposes multiple ports or uses a non-standard port, add this label:

```yaml
- "traefik.http.services.<router_name>.loadbalancer.server.port=<port>"
```

This is only needed when Traefik can't auto-detect the right port.

## Volume Patterns

For services that need persistent storage:

```yaml
services:
  web:
    image: myapp
    volumes:
      - app_data:/app/data    # Named volume for app data

  postgres:
    image: postgres:17
    volumes:
      - pg_data:/var/lib/postgresql/data   # Named volume for database

volumes:
  app_data:
  pg_data:
```

Named volumes persist across `docker compose down` and `docker compose up`. They are stored on the host filesystem managed by Docker.
