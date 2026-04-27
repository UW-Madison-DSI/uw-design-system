# Assessment Checklist

Use this checklist to evaluate whether a project can be deployed on the DSI services infrastructure.

## Hard Requirements

These must all be true for deployment to work:

- [ ] **HTTP-based**: The application serves HTTP traffic (web app, API, dashboard, static site). Non-HTTP services (raw TCP, UDP, gRPC without HTTP gateway) require custom Traefik configuration and are out of scope for the standard template.
- [ ] **Containerizable**: The application can run inside a Docker container. This means no hard dependencies on host-level resources like specific hardware, kernel modules, or GUI displays.
- [ ] **Single entry point**: The application has one primary HTTP port that Traefik should route to. Multiple public-facing ports require multiple router configurations.
- [ ] **Stateless or volume-safe**: The application either stores no local state, or its state can be persisted via Docker volumes without corruption (e.g., SQLite is fine, but the volume mount must be configured).

## Automatic Fit (minimal effort)

Projects that check these boxes deploy with almost no changes:

- Already has a Dockerfile or published Docker image
- Listens on a single HTTP port
- Configuration via environment variables
- No external database dependencies (or brings its own in the compose stack)
- No build-time secrets needed

## Moderate Effort

These need some work but are definitely deployable:

- No Dockerfile yet, but uses a standard framework (FastAPI, Flask, Django, Express, Next.js, Go net/http)
- Needs a database (PostgreSQL, MySQL, Redis) that can run as a sidecar container
- Requires build step (npm build, cargo build) handled by multi-stage Dockerfile
- Needs persistent storage (can be handled with Docker volumes)
- Requires environment variables that must be configured per-deployment

## Significant Effort / Potential Blockers

These may require changes to the application itself:

- **Hard-coded paths**: Application expects files at absolute paths that don't exist in container
- **Localhost assumptions**: Connects to services on localhost instead of using hostnames
- **Large build context**: Huge datasets or model files that shouldn't be in the Docker image
- **GPU requirements**: The services.dsi.wisc.edu server may not have GPU access
- **Long startup time**: Applications that take minutes to start may timeout health checks
- **Non-HTTP protocol**: WebSocket is fine (Traefik handles it), but raw TCP/UDP needs custom config
- **Multi-port**: Application exposes multiple ports that all need public routing
- **Write-heavy local storage**: Application writes heavily to local filesystem (should use external storage)
- **OS-specific dependencies**: Requires specific OS packages, fonts, or libraries not in standard base images (solvable but adds Dockerfile complexity)

## Not Deployable (without major changes)

- Desktop GUI applications
- Applications that require direct hardware access (USB, serial ports)
- Applications that must run on Windows
- Services that need to bind to privileged ports (< 1024) directly (Traefik handles 80/443)
- Applications with licensing that prohibits containerization
