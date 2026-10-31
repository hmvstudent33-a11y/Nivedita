name: Basic CI Workflow

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Check Python version
        run: python --version

      - name: Check Python code
        run: python -m py_compile hello.py

      - name: Run Python file
        run: python hello.py
