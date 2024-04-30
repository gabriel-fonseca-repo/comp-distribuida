from locust import HttpUser, between


def root(self):
    self.client.get("/")


def imagem_300_kb(self):
    self.client.get("/2024/04/17/imagem-nao-tao-bonita/")


def imagem_1_mb(self):
    self.client.get("/2024/04/17/imagens-bonitas/")


def texto_400_kb(self):
    self.client.get("/2024/04/17/6/")


class WordpressUser(HttpUser):
    host = "http://localhost:80"
    wait_time = between(5, 10)
    tasks = [root, imagem_300_kb, imagem_1_mb, texto_400_kb]
