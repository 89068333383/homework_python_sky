from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Бабушка старушка", "Тряпочная", "+79000000000"))
catalog.append(Smartphone("Зайкины ушки", "Лесная", "+79000000001"))
catalog.append(Smartphone("Стукачек", "По тарелочкам", "+79000000002"))
catalog.append(Smartphone("Голубиная", "Перелетом", "+79000000003"))
catalog.append(Smartphone("Телетайп", "Фонфон", "+79000000004"))

for fhone in catalog:
    print(f"{phone.brand} - {fhone.model}. {fhone.number}")
