# FastAPI TODO API - Developer Guide

This repository provides a starter template for building and running a FastAPI-based TODO API. Follow the steps below to set up, run, and test the application.

---

## Prerequisites

Ensure the following tools are installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Poetry**: [Install Poetry](https://python-poetry.org/docs/#installation)

---

## Table of Contents

- [Rationale](#Rationale)
- [Installation](#installation)
- [Running the Unit Tests](#running-the-unit-tests)
- [Code Linting](#code-linting)
- [Supported Scripts](#supported-scripts)
- [Folder Structure](#folder-structure)

## Dependencies

- Docker
- Poetry - [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

## Installation

1. Install the project dependencies using Poetry:

   ```console
   poetry install
   ```

2. Run Docker Compose to start the PostgreSQL server:

   ```console
   docker compose up
   ```

3. Run the database migrations:

   ```console
   poetry run alembic upgrade head
   ```

4. Seed the database with initial data:

   ```console
   poetry run seed_db
   ```

5. Run the FastAPI development server:

   ```console
   poetry run dev
   ```

## Running the Unit Tests

Unit tests require Docker to be installed, as they use Testcontainers. These tests are self-contained, using a clean database that rollbacks test data after each test.

1. Run the unit tests:
   ```console
   poetry run pytest
   ```

## Code Linting

We have two ways to ensure that our code is linted and formatted.

1. Use Poetry scripts after making changes:

   ```console
   poetry run ruff check        # Run Ruff checks
   poetry run ruff fix          # Fix Ruff formatting issues
   poetry run bandit -r src     # Run Bandit for security checks
   poetry run pyright           # Run Pyright for type checking
   ```

2. Use the pre-commit hook:
   ```console
   pre-commit install          # Install the pre-commit hooks
   pre-commit run --all-files  # Run the pre-commit hooks
   ```

## Supported Scripts

The project supports a variety of scripts to streamline development, database operations, testing, and code quality checks.

### Development and Database Operations

- **dev**: Runs the FastAPI development server.

```console
  poetry run dev
```

- make_migrations: Creates a new database migration with Alembic.

```console
  poetry run alembic revision --autogenerate
```

- upgrade: Applies all pending database migrations.

```console
  poetry run alembic upgrade head
```

- seed_db: Seeds the database with initial data.

```console
  poetry run seed_db
```

### Testing

- pytest: Executes all unit tests using Pytest.

```console
  poetry run pytest
```

### Code Quality and Linting

- ruff check: Checks code formatting and linting issues.

```console
  poetry run ruff check
```

- ruff fix: Automatically fixes code formatting issues.

```console
  poetry run ruff fix
```

- bandit: Runs Bandit for security checks.

```console
  poetry run bandit -r src
```

- pyright: Runs Pyright for type checking.

```console
  poetry run pyright
```

## Folder Structure

This structure highlights the main components of your FastAPI Poetry Template:

- `alembic/`: Contains database migration scripts and configurations.
- `seeds/`: Stores seed data files for populating the database.
- `src/`: The main source code directory.
  - `todos/`: Core application package.
    - `api/`: Defines API routes and endpoints.
    - `db/`: Manages database connections and sessions.
    - `entities/`: Contains Pydantic models for request/response validation.
  - `models/`: Defines SQLAlchemy ORM models.
  - `scripts/`: Holds utility scripts, such as data seeding.
  - `tests/`: Contains test files and configurations.
- `docker-compose.yml`: Docker Compose configuration for setting up the development environment.
- `pyproject.toml`: Project configuration and dependency management.
