import requests

BASE = "https://fakestoreapi.com"
prod_responce = requests.get(f"{BASE}/products")
prod_data = prod_responce.json()
print("Продукты дешевле 20")
for prod in prod_data:
    if prod['price'] < 20:
        print(f"{prod['title']} - {prod['price']}")
print()

cat_responce = requests.get(f"{BASE}/products/categories")
cat_data = cat_responce.json()
print("Категории продуктов")
for cat in cat_data:
    print(cat)
print()

prod_jewelery_responce = requests.get(f"{BASE}/products/category/jewelery")
prod_jewelery_data = prod_jewelery_responce.json()
print("Все продукты категории jewelery")
for prod in prod_jewelery_data:
    print(prod)
print()

users_responce = requests.get(f"{BASE}/users")
print("Все пользователи")
for user in users_responce.json():
    print(user)
print()

new_user = {
    "name" : {
        "firstname": "Максим",
        "lastname": "Советов"
    }
}

post = requests.post(f"{BASE}/users", json=new_user)
print(post.status_code)