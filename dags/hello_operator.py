from airflow.models import BaseOperator

class HelloOperator(BaseOperator):
    
    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name
        
    def execute(self, context) -> None:
        print(f"Hello {self.name}!")