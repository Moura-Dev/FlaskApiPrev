# APi-FLASK-PYTHON
Desafio BrasilPrev :


# Modelo de Uso com Docker:

no terminal execute o build:

docker-compose -f "docker-compose.yml" up -d --build

Apos subir o docker a aplicação esta pronta para uso.



# Endpoint Consultar Usuarios (Listar todas as usuarios no banco):

Method: Get
url =  /User/ (GET)


# Endpoint POST Usuario :

Method: POST

url = /User/ (POST)

modelo de url = User


 {
        "name": "Nome",
        "lastname": "SobreNome"
    }




# Endpoint Update Usuario pelo campo id:

Method: PUT, PATCH

url = /User/id"/ (Put)

modelo de url = User/1/


 {
        "name": "Nome",
        "lastname": "SobreNome"
    }




# Endpoint Delete Usuario pelo campo id:

Method: PUT, PATCH

url = /User/id"/ (Put)

modelo de url = User/1/ 




# Endpoint Consultar Product (Listar todas as produtos no banco):

Method: Get
url =  /Product/ (GET)



# Endpoint POST Produto :

Method: POST

url = /Product/ (POST)

modelo de url = Produto


  {
        "title": "carro",
        "price": 200.93,
        "description": "descricao "
    }




# Endpoint Update Produto pelo campo id:

Method: PUT, PATCH

url = /Product/id"/ (Put)

modelo de url = Product/1/ 


   {
        "title": "carro",
        "price": 200.93,
        "description": "descricao"
    }




# Endpoint Delete Produto pelo campo id:

Method: PUT, PATCH

url = /Product/id"/ (Put)

modelo de url = Product/1/




# Endpoint Consultar Order (Listar todas as Orders no banco):

Method: Get
url =  /Orders (GET)



# Endpoint POST Orders :

Method: POST

url = /Orders/ (POST)

modelo de url = Orders

  {
        "ammount": 2,
        "data": "2015/02/01",
        "value_total": 235,
        "user_id": 1,
        "product_id": 1
    }





# Endpoint Delete Orders pelo campo id:

Method: PUT, PATCH

url = /Orders/id"/ (Put)

modelo de url = Orders/1/ 





# Modo de uso sem docker:

# Crie um virtualenv 
python3 -m virtualenv venv

# Ativar virtualenv
source /venv/bin/activate

# Para usar o sistema
pip install -r requirements.txt

# Exportar flask:
Export FLASK_APP=app

# Conectar e Criar Banco de Dados
Edit app.conf app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/api' no arquivo __init__.py com suas configuraçoes


no terminal execute:
flask db init
flask db migrate
flask db upgrade
e pode ligar o aplicativo usando o comando flask run



