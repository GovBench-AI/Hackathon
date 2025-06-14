from inspect_ai import Task, task
from inspect_ai.scorer import exact, model_graded_fact,choice,answer,includes
from inspect_ai.solver import (chain_of_thought, generate, self_critique,multiple_choice,
                               system_message)

from dataset import constitution_benchmark_questions

SYSTEM_MESSAGE = """You are an AI assistant designed to assist with answering questions about the US Constitution.

## Response instructions
Please answer questions factually and provide a clear answer alongside relevant reasoning. If you're not sure, please say so — do not try to make up an answer.
"""


@task
def constitution_bench_freeform():
    return Task(
        dataset=constitution_benchmark_questions(),
        solver=[
            system_message(SYSTEM_MESSAGE),
            chain_of_thought(),
            generate(),
            self_critique(),
        ],
        scorer=model_graded_fact(model="openai/gpt-4.1-mini")
    )


# inspect eval eval.py --model openai/gpt-3.5-turbo