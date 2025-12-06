"""Dataset loader using utility functions."""

from src.utils.common import greet
from src.utils.io import read_config


def load_dataset(name: str) -> dict:
    """Load dataset with config."""
    config = read_config(f"data/{name}.yaml")
    message = greet(name)
    print(f"Dataset: {message}")
    return {"dataset": name, "config": config}


if __name__ == "__main__":
    result = load_dataset("mnist")
    print(f"Loaded: {result}")
