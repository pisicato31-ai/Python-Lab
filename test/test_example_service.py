from python_lab.services.example_service import ExampleService

def test_process():
    service = ExampleService()
    result = service.process("Teste")
    assert result == "Projeto profissional rodando para Teste"