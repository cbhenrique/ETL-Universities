import requests
import sqlite3


class extract:
    def _init_(self):
        pass

    def extract_data(self, country: str) -> list[dict]:
        """
        Método responsável por extrair os dados da API e transformas em uma lista de dicionários.

        Args:
            country: list - Nome do país que sera pesquisado na API
        """

        url = f"http://universities.hipolabs.com/search?country={country}"

        response = requests.get(url)
        response.raise_for_status()
        universities = response.json()

        return universities
