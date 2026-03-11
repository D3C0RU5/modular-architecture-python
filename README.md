# 🚀 ONE CLICK

Backend service built with **FastAPI**, following strict engineering standards for **typing, formatting, linting, and reproducible dependencies**.

The project provides a **fully automated development workflow** using **Make** and **pip-tools**, ensuring deterministic builds and consistent development environments.

---

# 📦 Tech Stack

* Python 3.11+
* FastAPI
* PostgreSQL
* Ruff (linting)
* Black (formatting)
* Pyright (strict type checking)
* pip-tools (dependency locking)
* Docker
* DevContainer
* Debugpy

---

# 🧠 Engineering Principles

This project enforces strong engineering standards:

* Strict type checking
* Automatic formatting
* Mandatory linting
* Reproducible dependencies
* Consistent development environments
* Modular monolith architecture

---

# 🛠 Getting Started

## 1️⃣ Using DevContainer (Recommended)

If using **VS Code**:

1. Install **Dev Containers extension**
2. Open the repository
3. Click **Reopen in Container**

The container will automatically:

* create the virtual environment
* install dependencies
* start the API with debugging enabled

Application will be available at:

```
http://localhost:3000
```

Debug port:

```
5678
```

---

# 💻 Manual Setup

Run:

```bash
make setup
```

This will:

1. Create `.venv`
2. Upgrade `pip`
3. Install `pip-tools`
4. Install development dependencies

---

# ⚙️ Make Commands

Run:

```bash
make help
```

Available commands:

| Command             | Description                                             |
| ------------------- | ------------------------------------------------------- |
| `make setup`        | Create virtual environment and install dev dependencies |
| `make install-dev`  | Install development dependencies                        |
| `make install-prod` | Install production dependencies                         |
| `make compile`      | Compile dependency lock files                           |
| `make upgrade`      | Upgrade all dependencies                                |
| `make format`       | Run Black formatter                                     |
| `make lint`         | Run Ruff lint                                           |
| `make typecheck`    | Run Pyright                                             |
| `make check`        | Run format + lint + typecheck                           |
| `make run`          | Run FastAPI locally                                     |
| `make docker-build` | Build docker images                                     |
| `make docker-up`    | Start docker environment                                |
| `make docker-down`  | Stop docker environment                                 |
| `make clean`        | Remove cache directories                                |

---

# ▶️ Running the Application

Run locally:

```bash
make run
```

Application will start at:

```
http://localhost:3000
```

---

# 📦 Dependency Management

Dependencies are managed with **pip-tools** to ensure reproducible builds.

## Dependency Files

```
requirements.in
requirements-dev.in
requirements.txt
requirements-dev.txt
```

| File                   | Purpose                         |
| ---------------------- | ------------------------------- |
| `requirements.in`      | Direct production dependencies  |
| `requirements-dev.in`  | Development dependencies        |
| `requirements.txt`     | Locked production dependencies  |
| `requirements-dev.txt` | Locked development dependencies |

---

# ➕ Adding Dependencies

### Production dependency

Edit:

```
requirements.in
```

Then run:

```bash
make compile
```

---

### Development dependency

Edit:

```
requirements-dev.in
```

Then run:

```bash
make compile
```

---

# 🔄 Upgrading Dependencies

Upgrade all packages:

```bash
make upgrade
```

---

# ⚠️ Dependency Rules

* Never edit `requirements.txt` manually
* Never run `pip freeze`
* Always modify `.in` files
* Always run `make compile` after editing `.in`

---

# 🎨 Code Quality

Format code:

```bash
make format
```

Run linter:

```bash
make lint
```

Run type checking:

```bash
make typecheck
```

Run all checks:

```bash
make check
```

---

# 🐳 Docker

Build containers:

```bash
make docker-build
```

Start environment:

```bash
make docker-up
```

Stop environment:

```bash
make docker-down
```

---

# 🧹 Cleanup

Remove cache files:

```bash
make clean
```

Removes:

```
__pycache__
.pytest_cache
```

---

# 📂 Project Structure

In construction

```
src/

  modules/
  application/
  infra/
  api/
```

| Layer         | Responsibility              |
| ------------- | --------------------------- |
| `domain`      | Business rules              |
| `application` | Use cases                   |
| `infra`       | Database and integrations   |
| `api`         | HTTP controllers and routes |

---

# 🔥 Development Workflow

Typical workflow:

1. Create a feature branch

```
git checkout -b feature/my-feature
```

2. Implement changes

3. Run checks

```bash
make check
```

4. Commit changes

5. Open Pull Request

---

# 🚀 Production Notes

Production environments should:

Install only production dependencies:

```bash
make install-prod
```

And follow:

* locked dependencies
* reproducible builds
* strict typing
* enforced linting

---

# 📜 Tests

Executing all tests:

```bash
pytest
```

Executing a specific file:

```bash
pytest path/of/test.py
```

Executing a specific test:

```bash
pytest path/of/test.py::test_name
```
or
```bash
pytest -k test_name
```

Executing only the last failed test:

```bash
pytest --lf
```