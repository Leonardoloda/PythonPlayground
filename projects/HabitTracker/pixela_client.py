from requests import post, put, delete


class PixelaClient:
    URL = "https://pixe.la"
    USERS_ENDPOINT = f"{URL}/v1/users"

    def __init__(self, token: str, username: str = None) -> None:
        self._token = token
        self._username = username
        pass

    def generate_graphs_endpoint(self, graph_id: str = None) -> str:
        if graph_id:
            return f"{self.URL}/v1/users/{self._username}/graphs/{graph_id}"

        return f"{self.URL}/v1/users/{self._username}/graphs"

    def generate_auth_header(self):
        return {
            "X-USER-TOKEN": self._token
        }

    def create_user(self, username: str) -> str:
        self._username = username

        body = {
            "username": username,
            "token": self._token,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }

        response = post(url=self.URL, json=body)

        response.raise_for_status()

        return response.text

    def set_current_user(self, username: str) -> str:
        self._username = username

    def get_current_user(self) -> str:
        return self._username

    def create_graph(self, id: str, graph_name: str, unit: str, color: str, type: str = "int") -> str:
        graph_config = {
            "id": id,
            "name": graph_name,
            "unit": unit,
            "color": color,
            "type": type
        }

        headers = {
            "X-USER-TOKEN": self._token
        }

        response = post(url=self.generate_graphs_endpoint(), json=graph_config, headers=headers)

        response.raise_for_status()

        return response.text

    def create_pixel(self, date: str, quantity: int, graph_id: str) -> str:
        header = self.generate_auth_header()

        body = {
            "date": date,
            "quantity": str(quantity)
        }

        response = post(url=self.generate_graphs_endpoint(graph_id), json=body, headers=header)

        response.raise_for_status()

        return response.text

    def update_pixel(self, graph_id: str, date: str, quantity: int) -> str:
        header = self.generate_auth_header()

        body = {
            "quantity": str(quantity)
        }

        response = put(url=f"{self.generate_graphs_endpoint(graph_id)}/{date}", headers=header, json=body)

        print(response.text)

        response.raise_for_status()

        return response.text

    def delete_pixel(self, graph_id: str, date: str) -> str:
        response = delete(url=f"{self.generate_graphs_endpoint(graph_id)}/{date}", headers=self.generate_auth_header())

        response.raise_for_status()

        return response.text
