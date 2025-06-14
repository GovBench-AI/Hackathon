from inspect_ai.dataset import Dataset, FieldSpec, MemoryDataset, json_dataset
from inspect_ai.dataset import Sample


def sbir_benchmark_questions(file_path: str = "freeform_questions.json") -> Dataset:
    dataset = json_dataset(
        file_path, sample_fields=FieldSpec(input="input", target="target")
    )
    return MemoryDataset(
        samples=list(dataset), name="sbir_freeform_questions", location=file_path
    )

