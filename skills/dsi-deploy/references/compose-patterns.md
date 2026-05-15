# Compose.yml Patterns

All compose files for the DSI services infrastructure must follow these conventions.

## Required Labels

Every public-facing service needs these Traefik labels:

```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.<ROUTER_NAME>.rule=Host(`<APP_DOMAIN>`)"
  - "traefik.http.routers.<ROUTER_NAME>.entrypoints=websecure"
  - "traefik.http.routers.<ROUTER_NAME>.tls=true"
  - "traefik.http.routers.<ROUTER_NAME>.tls.certresolver=myresolver"
```

Where:
- `<ROUTER_NAME>` = `<netid>-<repo_name>-<service_name>` (globally unique)
- `<APP_DOMAIN>` = `<repo_name>.services.dsi.wisc.edu`

## Pattern 1: Single Service, Single Network

The simplest deployment. One container, public-facing.

```yaml
services:
  <NETID>-<REPO_NAME>-web:
    image: "<IMAGE>"
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.rule=Host(`<REPO_NAME>.services.dsi.wisc.edu`)"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.entrypoints=websecure"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.tls=true"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.tls.certresolver=myresolver"
    networks:
      - traefik_network
    restart: unless-stopped

networks:
  traefik_network:
    external: true
```

## Pattern 2: Single Service with Build Context

When the project has a Dockerfile and needs to be built from source.

```yaml
services:
  <NETID>-<REPO_NAME>-web:
    build:
      context: .
      dockerfile: Dockerfile
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.rule=Host(`<REPO_NAME>.services.dsi.wisc.edu`)"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.entrypoints=websecure"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.tls=true"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.tls.certresolver=myresolver"
    networks:
      - traefik_network
    restart: unless-stopped

networks:
  traefik_network:
    external: true
```

## Pattern 3: App + Database (Multi-Network)

Web application with a database backend. The database is isolated from the internet.

```yaml
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - DATABASE_URL=postgresql://user:password@postgres:5432/appdb
    networks:
      - traefik_network
      - internal_network
    labels:
      - "traefik.enable=true"
      - "traefik.docker.network=traefik_network"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.rule=Host(`<REPO_NAME>.services.dsi.wisc.edu`)"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.entrypoints=websecure"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.tls=true"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.tls.certresolver=myresolver"
    depends_on:
      - postgres
    restart: unless-stopped

  postgres:
    image: postgres:17
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=appdb
    volumes:
      - pg_data:/var/lib/postgresql/data
    networks:
      - internal_network
    restart: unless-stopped

networks:
  traefik_network:
    external: true
  internal_network:
    driver: bridge

volumes:
  pg_data:
```

## Pattern 4: App + Redis Cache

```yaml
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - REDIS_URL=redis://redis:6379
    networks:
      - traefik_network
      - internal_network
    labels:
      - "traefik.enable=true"
      - "traefik.docker.network=traefik_network"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.rule=Host(`<REPO_NAME>.services.dsi.wisc.edu`)"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.entrypoints=websecure"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.tls=true"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.tls.certresolver=myresolver"
    depends_on:
      - redis
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    networks:
      - internal_network
    restart: unless-stopped

networks:
  traefik_network:
    external: true
  internal_network:
    driver: bridge

volumes:
  redis_data:
```

## Pattern 5: Environment Variables from .env

When the service needs secrets or per-deployment configuration:

```yaml
services:
  <NETID>-<REPO_NAME>-web:
    build:
      context: .
      dockerfile: Dockerfile
    env_file:
      - .env
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.rule=Host(`<REPO_NAME>.services.dsi.wisc.edu`)"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.entrypoints=websecure"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.tls=true"
      - "traefik.http.routers.<NETID>-<REPO_NAME>-web.tls.certresolver=myresolver"
    networks:
      - traefik_network
    restart: unless-stopped

networks:
  traefik_network:
    external: true
```

## Pattern 6: Custom Port

When the application exposes a non-standard port that Traefik can't auto-detect:

```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.services.<NETID>-<REPO_NAME>-web.loadbalancer.server.port=8501"
  - "traefik.http.routers.<NETID>-<REPO_NAME>-web.rule=Host(`<REPO_NAME>.services.dsi.wisc.edu`)"
  - "traefik.http.routers.<NETID>-<REPO_NAME>-web.entrypoints=websecure"
  - "traefik.http.routers.<NETID>-<REPO_NAME>-web.tls=true"
  - "traefik.http.routers.<NETID>-<REPO_NAME>-web.tls.certresolver=myresolver"
```

Use this when:
- The Dockerfile exposes multiple ports
- The application runs on a port other than the one in the EXPOSE directive
- Traefik picks the wrong port (visible in logs as connection refused)

## Naming Conventions

- **Router name**: `<netid>-<repo_name>-<service_name>` (e.g., `srwangen-my-app-web`)
- **Service name** (single network): Use the router name as the service name for easier debugging
- **Service name** (multi-network): Use short functional names (`web`, `postgres`, `redis`, `worker`) since the project directory already provides context
- **Domain**: `<repo_name>.services.dsi.wisc.edu` (no underscores allowed)
- **Volume names**: Descriptive, lowercase (e.g., `pg_data`, `app_uploads`, `redis_data`)
