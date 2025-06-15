#  PromptSmart: Analyzing and Preparing Prompt Data for LLM Research

This project focuses on analyzing and preparing the [Alpaca dataset](https://github.com/tatsu-lab/stanford_alpaca) for instruction-tuned Large Language Models (LLMs).
It explores fairness, math reasoning, and prompt formatting which are foundational elements in building more inclusive and reliable AI systems.

## Key Features

- Load and filter LLM prompt datasets (e.g., by topics like *fairness* or *math*)
- View prompt samples (instruction, input, output)
- Perform keyword-based topic filtering
- Format data for instruction-following tasks
- Modular code structure using Python and PyTorch
- Custom keyword search via `search.py`
  

##  Project Structure

PromptSmart/  
├── data/  
│   └── alpaca_data.json  
├── notebook/  
│   └── prompt_exploration.ipynb  
├── src/  
│   ├── dataset.py  
│   ├── utils.py  
├── main.py  
├── search.py  
├── README.md  
├── .gitignore  



## 🔧 Setup Instructions

1. **Clone or download** this repository.  
2. **Install required Python packages**:
3. **Run the main script** to explore prompt samples:
4. **Open the notebook** for prompt analysis and visualization:


## 📈 Sample Insight

After analyzing prompt categories, we found that **"math"** and **"climate"** are the most represented topics in the dataset. 
This insight highlights topic imbalances; a useful signal when designing fair and representative instruction datasets.

## 🙋🏽 About

Created with ❤️ by **Abisola Oyetunji** as part of a research-driven exploration into LLM prompt quality, fairness, and responsible AI design.  




