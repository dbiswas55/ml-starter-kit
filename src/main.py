"""Main entry point."""

from src.dataset.check_dataset_imports import load_dataset
from src.models.check_model_imports import train_model


def main() -> None:
	"""Run ML pipeline."""
	print("=== ML Starter Kit ===")
	data = load_dataset("mnist")
	print(f"\nData loaded: {data['dataset']}")
	
	result = train_model("mnist")
	print(f"\nTraining complete: {result['accuracy']*100}% accuracy")


if __name__ == "__main__":
	main()
