"""Model training using dataset loader."""

from src.dataset.check_dataset_imports import load_dataset
from src.utils.common import greet


def train_model(dataset_name: str) -> dict:
    """Train model on dataset."""
    data = load_dataset(dataset_name)
    print(f"Model: {greet('Trainer')}")
    print(f"Training on {data['dataset']}...")
    return {"model": "trained", "accuracy": 0.95}


if __name__ == "__main__":
    result = train_model("mnist")
    print(f"Result: {result}")
