def print_sample(dataset, n=3):
    for i in range(min(n, len(dataset))):
        print(f"Instruction: {dataset[i]['instruction']}")
        print(f"Input: {dataset[i]['input']}")
        print(f"Output: {dataset[i]['output']}")
        print('-' * 50)
