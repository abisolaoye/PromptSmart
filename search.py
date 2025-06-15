from src.dataset import AlpacaDataset

def search_prompts(dataset, keyword):
    matches = [item for item in dataset if keyword.lower() in item["instruction"].lower()]
    print(f"Found {len(matches)} matching prompts:")
    for i, item in enumerate(matches[:5]):  # Show only first 5
        print(f"\n{i+1}. Instruction: {item['instruction']}")
        print(f"   Input: {item['input']}")
        print(f"   Output: {item['output']}")

if __name__ == "__main__":
    data_path = "data/alpaca_data.json"
    dataset = AlpacaDataset(data_path)

    keyword = input("Enter a keyword to search: ")
    search_prompts(dataset, keyword)
