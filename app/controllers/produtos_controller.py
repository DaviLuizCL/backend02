import requests

def get_produtos():
    url = "https://dummyjson.com/products"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("products", [])
    except requests.RequestException as e:
        print(f"Erro ao buscar produtos: {e}")
        return []
