from src.dataset import AlpacaDataset
from src.utils import print_sample

if __name__ == "__main__":
    data_path = "data/alpaca_data.json"

    print("Loading all data...")
    full_dataset = AlpacaDataset(data_path)
    print(f"Total samples: {len(full_dataset)}")
    print_sample(full_dataset)

    print("\nLoading fairness-related prompts...")
    fairness_dataset = AlpacaDataset(data_path, filter_topic="fairness")
    print(f"Fairness samples: {len(fairness_dataset)}")
    print_sample(fairness_dataset)

    print("\nLoading math-related prompts...")
    math_dataset = AlpacaDataset(data_path, filter_topic="math")
    print(f"Math samples: {len(math_dataset)}")
    print_sample(math_dataset)

