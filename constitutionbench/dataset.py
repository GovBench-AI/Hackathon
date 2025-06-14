from inspect_ai.dataset import Dataset, FieldSpec, MemoryDataset, json_dataset
from inspect_ai.dataset import Sample


def constitution_benchmark_questions(file_path: str = "sample_questions.json") -> Dataset:
    dataset = json_dataset(
        file_path, sample_fields=FieldSpec(input="input", target="expected_output")
    )
    return MemoryDataset(
        samples=list(dataset), name="constitution_questions", location=file_path
    )

