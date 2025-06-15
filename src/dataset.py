import json
from torch.utils.data import Dataset

class AlpacaDataset(Dataset):
    def __init__(self, data_path, filter_topic=None):
        with open(data_path, 'r') as f:
            data = json.load(f)

        if filter_topic:
            self.data = [
                item for item in data
                if filter_topic.lower() in item['instruction'].lower()
            ]
        else:
            self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return {
            "instruction": self.data[idx]["instruction"],
            "input": self.data[idx]["input"],
            "output": self.data[idx]["output"]
        }
