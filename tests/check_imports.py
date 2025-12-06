"""Test imports work from tests folder."""

from src.dataset.check_dataset_imports import load_dataset
from src.models.check_model_imports import train_model
from src.utils.common import greet


def test_imports():
    """Verify all src imports work from tests."""
    assert greet("Test") == "Hello, Test!"
    data = load_dataset("test_data")
    assert data["dataset"] == "test_data"
    result = train_model("test_data")
    assert result["model"] == "trained"
    print("✓ All imports working from tests/")


if __name__ == "__main__":
    test_imports()
