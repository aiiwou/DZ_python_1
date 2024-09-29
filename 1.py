import requests

BASE = "https://fakestoreapi.com"
prod_response = requests.get(f"{BASE}/products")
prod_data = prod_response.json()
print("Продукты дешевле 20")
for prod in prod_data:
    if prod['price'] < 20:
        print(f"{prod['title']} - {prod['price']}")
print()

cat_response = requests.get(f"{BASE}/products/categories")
cat_data = cat_response.json()
print("Категории продуктов")
for cat in cat_data:
    print(cat)
print()

prod_jewelery_response = requests.get(f"{BASE}/products/category/jewelery")
prod_jewelery_data = prod_jewelery_response.json()
print("Все продукты категории jewelery")
for prod in prod_jewelery_data:
    print(f"{prod['title']} - {prod['category']}")
print()

users_response = requests.get(f"{BASE}/users")
print("Все пользователи")
for user in users_response.json():
    print(f"{user['name']['firstname']} {user['name']['lastname']}")
print()

new_user = {
    "name" : {
        "firstname": "Максим",
        "lastname": "Советов"
    }
}

post = requests.post(f"{BASE}/users", json=new_user)
print("Код:", post.status_code, "ID Добавленного:", post.json())