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
├── .vscode/
│   └── settings.json           # VS Code workspace settings
├── src/                        # Main source code (installed as package)
│   ├── dataset/
│   │   └── check_dataset_imports.py
│   ├── models/
│   │   └── check_model_imports.py
│   ├── utils/
│   │   ├── common.py
│   │   └── io.py
│   └── main.py
├── tests/
│   └── check_imports.py        # Import verification tests
├── data/
│   ├── raw/                    # Raw data files
│   │   └── .gitkeep
│   └── processed/              # Processed data files
│       └── .gitkeep
├── configs/
│   └── config.yaml             # Configuration files
├── experiments/                # Experiment outputs
│   └── .gitkeep
├── results/                    # Overall results
│   └── .gitkeep
├── .gitignore
├── pyproject.toml              # Package configuration
└── README.md
```