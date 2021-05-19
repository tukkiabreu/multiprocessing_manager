# MULTIPROCESSING MANAGER

``multiprocessing_manager`` é uma classe genérica que pode receber qualquer __função__ e __*n*__ tuplas de argumentos.

Para cada tupla de argumento recebida, o pacote irá rodar a função recebida paralelamente.

Logo, se passar uma função e três tuplas de argumentos, a classe irá 
automaticamente rodar a função três vezes ao mesmo tempo, com uma tupla de argumentos passada em cada uma dessas
execuções.

Exemplo:

```python
from multiprocessing_manager.run_function import RunFunctions
 
 #caso queira executar as funções "func(*arg1)", "func(*arg2)", "func(*arg3)" paralelamente:
 
exc_paralela = RunFunctions(func, *arg1, *arg2, *arg3)

 #caso as funçoes tenham retorno, os retornos serão salvos na mesma ordem das tuplas de argumentos no atributo:
 
retornos = exc_paralela.return_values

#OBS: Como esse pacote cria subprocessos, ele não pode ser usado em um subprocesso ou dentro de uma execução de si mesmo.
 ```



