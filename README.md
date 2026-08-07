# GitHub Actions Cheatsheet

Quick reference for YAML and GitHub Actions.

## YAML Basics

* `key: value` — key/value pair
* Indentation — creates nesting
* `- item` — list item
* `|` — multiline value
* Use spaces, not tabs

```yaml
name: Example

items:
  - one
  - two
```

## Workflow Structure

```yaml
name: Workflow Name

on:
  ...

jobs:
  job-name:
    runs-on: ubuntu-latest
    steps:
      ...
```

| Syntax      | Purpose                 |
| ----------- | ----------------------- |
| `name:`     | Workflow/step name      |
| `on:`       | Workflow trigger        |
| `jobs:`     | Define jobs             |
| `runs-on:`  | Runner environment      |
| `steps:`    | Job steps               |
| `run:`      | Execute shell command   |
| `uses:`     | Use an existing Action  |
| `with:`     | Configure an Action     |
| `env:`      | Environment variables   |
| `needs:`    | Job dependency          |
| `strategy:` | Job strategy            |
| `matrix:`   | Multiple configurations |

## Triggers

### Push

```yaml
on:
  push:
```

### Pull Request

```yaml
on:
  pull_request:
```

### Manual

```yaml
on:
  workflow_dispatch:
```

### Branch Filter

```yaml
on:
  push:
    branches:
      - main
```

### Path Filter

```yaml
on:
  push:
    paths:
      - "src/**"
```

### Branch + Path

```yaml
on:
  push:
    branches:
      - main
    paths:
      - "src/**"
```

## Common Actions

### Checkout

```yaml
uses: actions/checkout@v4
```

### Python

```yaml
uses: actions/setup-python@v5
with:
  python-version: "3.12"
```

## Commands

### Single Command

```yaml
run: python app.py
```

### Multiple Commands

```yaml
run: |
  echo "Hello"
  python app.py
```

## Variables & Secrets

### Environment Variable

```yaml
env:
  APP_NAME: github-learning
```

### GitHub Expression

```yaml
${{ github.actor }}
```

### Secret

```yaml
${{ secrets.MY_SECRET }}
```

## Job Dependencies

```yaml
jobs:
  test:
    ...

  build:
    needs: test
```

`test → build`

## Matrix

```yaml
strategy:
  matrix:
    python-version:
      - "3.11"
      - "3.12"
```

## Mental Model

`name:` → What is it?

`on:` → When does it run?

`jobs:` → What work happens?

`runs-on:` → Where does it run?

`steps:` → What does it do?

`run:` → Execute a command

`uses:` → Use an existing Action

`with:` → Configure an Action

`env:` → Provide variables

`${{ ... }}` → GitHub Actions expression

