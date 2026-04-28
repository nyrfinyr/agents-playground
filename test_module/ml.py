class ImageDataset:

    def __init__(self, name:str, num_images:int):
        self.name = name 
        self.num_images = num_images

    def print_summary(self):
        print(f"Dataset: {self.name} | Numero di immagini: {self.num_images}")


from dataclasses import dataclass

@dataclass
class EvaluationMetric:
    metric_name: str 
    value: float
    is_validation: bool = True

from typing import Any, Protocol

class Trainable(Protocol):
    def train(self, data:Any) -> None:
        ...

class Random_Forest:
    def train(self, data:Any):
        print(f"Addestramento Random Forest con i dati: {data}")

class CNN:
    pass 
    
def addestra_qualsiasi_modello(modello:Trainable, data:Any):
    modello.train(data)

def crea_mappatura(class_names: list[str]) -> dict[str, int]:
    return {}


type Batch[T] = list[T]

def crea_batches[T](dati: list[T], dimensione_batch:int) -> list[Batch[T]]: # type: ignore
    pass

from typing import Callable

def filtra_dataset(dati: list[str], criterio:Callable[[str], bool]) -> list[str]:
    return [x for x in dati if criterio(x)]