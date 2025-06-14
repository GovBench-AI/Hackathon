from inspect_ai import Task, task, eval
from inspect_ai.scorer import exact, model_graded_fact,choice,answer,includes
from inspect_ai.solver import (chain_of_thought, generate, self_critique,multiple_choice,
                               system_message)

from dataset import sbir_benchmark_questions

SYSTEM_MESSAGE = """You are an AI assistant designed to assist with answering questions about the Small Business Innovation Research.

## Response instructions
Please answer questions factually and provide a clear answer alongside relevant reasoning. If you're not sure, please say so — do not try to make up an answer.
"""

@task
def sbir_bench_freeform():
    return Task(
        dataset=sbir_benchmark_questions(),
        solver=[
            system_message(SYSTEM_MESSAGE),
            chain_of_thought(),
            generate(),
            self_critique(),
        ],
        scorer=model_graded_fact()
    )

# eval(sbir_bench_freeform(), model="openai/o3-2025-04-16", limit=10)
