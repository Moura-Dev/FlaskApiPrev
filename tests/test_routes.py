
from unittest import TestCase
from app import create_app
from app.views import Users

class FlaskBaseTest(TestCase):
     setUp(self):

     def test_acessar_rota_usuarios_retorna_status_200(self):
         resp = self.get("/User/")
         assert resp.status_code == 201


    def test_acessar_rota_products(self):
         resp = self.get("/Products/")
         assert resp.status_code == 201


    def test_acessar_rota_products(self):
         resp = self.get("/Order/")
         assert resp.status_code == 201