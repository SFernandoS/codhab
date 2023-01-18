# Prova Técnica Codhab


O candidato afim de participar do processo seletivo para compor equipe técnica no contrato da CODHAB, deverá apresentar o conhecimento necessário para integrar ao corpo técnico existente.
Prova técnica consiste na criação de um CRUD utilizando a linguagem "Python” versão 3.10.7 ou superior, para construção de uma API utilizando FASTAPI com o ORM "ORMAR" e banco de dados "POSTGRES".
API deve conter os endpoints para inclusão, alteração, listagem e deleção de "USUÁRIOS" contendo os campos "ID, CPF, NOME, EMAIL E TELEFONE".
Todos os métodos tem que ser testáveis via SWAGGER ou POSTMAN. 
A Prova não tem tempo limite estipulado, mas o tempo será contado a partir da 
Data de recebimento destes requisitos para determinar o nível do candidato.
Ao concluir essa etapa o candidato devera disponibilizar no seu github pessoal a
URL publica do repositório para avaliação técnica. 

Na entrevista técnica, o candidato será, avaliado e questionado sobre a prova. 
Serão observadas boas práticas, organização e qualidade da API entregue.

### Conhecimentos Obrigatórios
 - PYTHON 3 
 - FAST API
 - ORMAR
 - SWAGGER
 - POSTMAN
 - POSTGRES
 - GIT 

### Conhecimentos Desejáveis
 - DOCKER 
 - SOLID 
 - TDD
 - DDD / CLEAN ARCHITECTURE
 - REDIS
 
 
 ## Instalação
 
 ### Docker
 Primeiramente, instalação do Docker de acordo com o s.o neste [link](https://docs.docker.com/get-docker/)
 
 ### Docker Compose
 Depois de instalar o docker, você pode instalar o docker-compose, de acordo com o seu s.o neste [link](https://docs.docker.com/compose/install/)

 ### Executar a API
1. Primeiramente, é necessário a criação de uma rede para os serviços:
``` bash
make network
```

2. Em, seguida, para executar a api e o postgress:
``` bash
make up
```

- Para parar os serviços:
``` bash
make up
```

- Para executar o down e remover os volumes:
``` bash
make down
```

## Cenário de testes

O cenário de testes é executado manualmente, para executar é necessário instalar as depedências. Portanto, é recomendavel o uso de uma virtualenv. Para instalar as depedencias é necessário basta executar o comando:
``` bash
pip install -R requirements.txt
```

Em seguida, é necessário subir o serviço do postgres, mesmo que não o use diretamente para executar os testes:
``` bash
make pg
```

Finalmente, para executar os testes:
``` bash
pytest .
```

## Sobre a API

Foi criado um CRUD de usuário assim como a descrição da prova. Os endpoints podem ser visualizados no /docs. Lá há um swagger do qual pode-se executar fácilmente todos os métodos existentes. 




