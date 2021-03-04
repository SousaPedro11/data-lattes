import unittest
from abc import ABC, ABCMeta

from app import create_app


class TestBase(ABC):
    __metaclass__ = ABCMeta

    class Meta:
        abstract = True

    def setUp(self) -> None:
        self.app = create_app('dev').test_client()


class TestIntegridade(TestBase, unittest.TestCase):

    def test_home_redirect(self):
        self.response = self.app.get('/')
        self.assertEqual(302, self.response.status_code)

    def test_index_home_redirect(self):
        self.response = self.app.get('/index/')
        self.assertEqual(302, self.response.status_code)

    def test_home(self):
        self.response = self.app.get('/home/')
        self.assertEqual(200, self.response.status_code)

    # def test_indicadores(self):
    #     self.response = self.app.get('/indicadores/')
    #     self.assertEqual(200, self.response.status_code)
    #
    # def test_contato(self):
    #     self.response = self.app.get('/contato/')
    #     self.assertEqual(200, self.response.status_code)
    #
    # def test_sobre(self):
    #     self.response = self.app.get('/sobre/')
    #     self.assertEqual(200, self.response.status_code)

    def test_vis1(self):
        self.response = self.app.get('/vis1/')
        self.assertEqual(200, self.response.status_code)

    def test_vis2(self):
        self.response = self.app.get('/vis2/')
        self.assertEqual(200, self.response.status_code)

    def test_vis3(self):
        self.response = self.app.get('/vis3/')
        self.assertEqual(200, self.response.status_code)

    def test_not_found(self):
        self.response = self.app.get('/rotas/')
        self.assertEqual(404, self.response.status_code)
