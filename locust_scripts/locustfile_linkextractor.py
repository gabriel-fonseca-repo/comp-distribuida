from locust import HttpUser, between

urls_for_testing = [
    "https://en.wikipedia.org/wiki/Wikipedia",
    "https://en.wikipedia.org/wiki/Semrush",
    "https://en.wikipedia.org/wiki/Kellam_Review",
    "https://en.wikipedia.org/wiki/Llanmaes",
    "https://en.wikipedia.org/wiki/Thick-billed_raven",
    "https://en.wikipedia.org/wiki/Russian_Armed_Forces",
    "https://en.wikipedia.org/wiki/Shadow_Warrior_(2013_video_game)",
    "https://en.wikipedia.org/wiki/Grey_Eye_Glances",
    "https://en.wikipedia.org/wiki/Berrostegieta",
    "https://en.wikipedia.org/wiki/Desi_DNA",
    "https://en.wikipedia.org/wiki/Henning_Conle",
    "https://en.wikipedia.org/wiki/Br%C4%83tuleni",
    "https://en.wikipedia.org/wiki/Paul_J._Griffiths",
    "https://en.wikipedia.org/wiki/Gaumont_State_Cinema",
    "https://en.wikipedia.org/wiki/Road-powered_electric_vehicle",
]


def load_test(self):
    for url in urls_for_testing:
        self.client.get(f"/?url={url}")


class WikipediaUser(HttpUser):
    host = "http://localhost:80"
    wait_time = between(5, 10)
    tasks = [load_test]
