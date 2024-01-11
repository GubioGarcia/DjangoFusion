from django.test import TestCase
from django.test import Client # simula um cliente navegador para teste
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Teste Nome',
            'email': 'teste@email.com',
            'assunto': 'Assunto teste',
            'mensagem': 'Uma mensagem qualquer para teste'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)
    
    def test_form_invalid(self):
        dados = {
            'nome': 'Teste',
            'assunto': 'Assunto Teste'
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)