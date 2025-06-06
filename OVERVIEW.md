# Spike: Poetry vs Hatch for Dependency and Environment Management

This document provides an overview of Poetry, its pros and cons, usage scenarios, and a comparison with Hatch to justify its selection for this project.

---

## Overview of Poetry

Poetry is a dependency and environment management tool for Python projects. It simplifies dependency resolution, virtual environment management, and project packaging.

### Pros

- **Dependency Management**: Handles dependency resolution with a lock file (`poetry.lock`) for reproducible builds.
- **Virtual Environment Integration**: Automatically creates and manages virtual environments.
- **Ease of Use**: Intuitive CLI commands for common tasks like `poetry install`, `poetry add`, and `poetry update`.
- **Project Configuration**: Centralized configuration in `pyproject.toml`.
- **Built-in Publishing**: Simplifies publishing packages to PyPI.

### Cons

- **Performance**: Slower than Hatch for some operations, especially in large projects.
- **Limited Hooks**: Fewer pre-commit and post-commit hooks compared to Hatch.
- **Learning Curve**: Slightly steeper for developers unfamiliar with its workflow.

---

## Usage Scenarios

Poetry is ideal for:

- Projects requiring strict dependency resolution and reproducibility.
- Teams that value simplicity and an all-in-one tool for dependency, environment, and packaging management.
- Applications where publishing to PyPI is a priority.

---

## Comparison: Poetry vs Hatch

| Feature                    | Poetry                         | Hatch                           |
| -------------------------- | ------------------------------ | ------------------------------- |
| **Dependency Management**  | Strong lock file support       | Strong lock file support        |
| **Environment Management** | Automatic virtual environments | Requires explicit configuration |
| **Ease of Use**            | Intuitive CLI                  | CLI can be less intuitive       |
| **Performance**            | Slower for large projects      | Faster for large projects       |
| **Hooks**                  | Limited                        | Extensive                       |
| **Publishing**             | Built-in                       | Requires additional setup       |

---

## Managing Multiple APIs with Poetry

Poetry supports managing multiple APIs in the same repository by leveraging its `packages` and `scripts` configuration in `pyproject.toml`. Each API can be treated as a separate package with its own entry point, while shared utilities or models can be placed in a common package.

### Key Features:

1. **Isolation**: Each API resides in its own directory, ensuring clean separation of concerns.
2. **Shared Code**: Common utilities or models can be placed in a shared package for reuse.
3. **Scalability**: Adding new APIs is straightforward—just create a new package and update `pyproject.toml`.
4. **Unified Management**: Poetry's dependency and script management simplifies running and maintaining multiple APIs.

### Example:

- Define separate scripts for each API in `pyproject.toml`:
  ```toml
  [tool.poetry.scripts]
  api_one = "api_one.main:start"
  api_two = "api_two.main:start"
  ```
- Run each API using:
  ```bash
  poetry run api_one
  poetry run api_two
  ```

This approach ensures modularity and scalability while maintaining simplicity in managing dependencies and environments.

---

## Why Poetry?

Poetry may be a good choice because:

1. **Simplicity**: Its all-in-one approach reduces the need for additional tools.
2. **Reproducibility**: The lock file ensures consistent environments across machines.
3. **Community Adoption**: Widely used and supported in the Python ecosystem.
4. **Ease of Onboarding**: Intuitive for new developers to get started quickly.

While Hatch offers better performance and more hooks, Poetry's comprehensive feature set and ease of use make it a better fit for this project's requirements.
