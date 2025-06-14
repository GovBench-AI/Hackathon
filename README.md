# GovBench Hackathon
June 14, 2025

Welcome to the GovBench hackathon!

### How to Create a New Benchmark
We'll walk through how we create _ConstitutionBench_, a benchmark for evaluating AI models on the US Constitution.

### Step 0: Create new folder for your benchmark assets
You can just duplicate the `constitutionbench` folder and rename it to your benchmark name.

### Step 1: Determine the Foundational Document(s)
Grounding your benchmark in foundational documents is crucial. For ConstitutionBench, we will use:
- [The US Constitution](https://constitutioncenter.org/media/files/constitution.pdf)

### Step 2: Generate Synthetic Questions
Using Google AI studio (because of Gemini's large context window), we'll upload our documents and prompt it to generate questions. For constitutionbench, view the sample prompt [here](./constitutionbench/sample_prompt.txt).

Make sure the following settings are configured:
- Structured output: ON
- Temperature: 1
- Model: Gemini 2.5 Flash Preview 05-20

View full conversation [here](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221nSNC0j4dDgA9czGp1dG6t6odP70rpo5x%22%5D,%22action%22:%22open%22,%22userId%22:%22109827112673159004178%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing).

### Step 3: Save the Generated Questions
Copy the generated questions into a text file named `questions.json` in your folder. For ConstitutionBench, the questions are already provided in [`constitutionbench/sample_questions.json`](./constitutionbench/sample_questions.json).

### Step 4: Set up your Environment
- Install [Inspect VS Code](https://marketplace.visualstudio.com/items?itemName=ukaisi.inspect-ai) extension. 
- Set up virtual environment in your benchmark folder:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```
- Install required packages:
  ```bash
  pip install -r requirements.txt
  ```
- Set your OpenAI API key as an environment variable:
  ```bash
  export OPENAI_API_KEY='your_openai_api_key'
  export ANTHROPIC_API_KEY='your_anthropic_api_key'
  export TOGETHER_API_KEY='your_together_api_key'
  ```

### Step 5: Run the Benchmark
In this case, we are evaluating the OpenAI GPT-3.5 Turbo.
- Run the benchmark script:
  ```bash
  inspect eval eval.py --model openai/gpt-3.5-turbo
  ```

### Step 6: Review Results
After running the benchmark, Inspect AI will automatically generate a log file in your benchmark folder.

### Step 7 (Optional): View Results
Inspect has a built in web UI that visualizes the `*.eval` files. By default, it's on `127.0.0.1:7575`

```bash
inspect view
```
Note: Make sure you run the visualization command in the same working directory as your `logs` directory.

```bash
$ tree -I '__pycache__'              
.
├── dataset.py
├── eval.py
├── logs
│   ├── 2025-06-14T09-21-13-04-00_constitution-bench-freeform_9ViyxURM3ELjzE7xywG7oi.eval
│   └── 2025-06-14T11-57-01-04-00_constitution-bench-freeform_5C4X6LExPEk644Z2CfZmNx.eval
├── requirements.txt
├── results.csv
├── sample_prompt.txt
└── sample_questions.json

2 directories, 8 files
$ inspect view
Inspect View: file:///Users/justinwlin/Projects/personal/Hackathon/constitutionbench/logs
======== Running on http://127.0.0.1:7575 ========
(Press CTRL+C to quit)
```

<img width="1726" alt="image" src="https://github.com/user-attachments/assets/6ce7c08c-63e4-41d1-b7c7-3ce6bf582d0d" />


### Step 7: Copy/paste score to [results.csv](/constitutionbench/results.csv)

### Step 8: Repeat steps 5-7 for other models
### Step 9: Submit Your Benchmark
Submit your results.csv file.
