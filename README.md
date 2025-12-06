# ml-starter-kit

Machine Learning starter kit with proper Python package structure.

## Setup

1. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv310
   source venv310/bin/activate
   ```

2. **Install the project in editable mode**
   ```bash
   pip install -e .
   ```
   This registers `src` as an importable package, so you can use `from src.utils import ...` anywhere.

3. **Verify imports work**
   ```bash
   python tests/check_imports.py
   python src/main.py
   ```

## Project Structure

```
ml-starter-kit/
├── src/              # Main source code (installed as package)
│   ├── dataset/
│   ├── models/
│   └── utils/
├── tests/            # Test files
├── data/             # Raw and processed data
├── configs/          # Configuration files
└── pyproject.toml    # Package configuration
```