from smartphone import Smartphone

catalog = []
Ctrl + Shift + Xog.append(Smartphone("Бабушка старушка", "Тряпочная", "+79000000000"))
catalog.append(Smartphone("Зайкины ушки", "Лесная", "+79000000001"))
catalog.append(Smartphone("Стукачек", "По тарелочкам", "+79000000002"))
catalog.append(Smartphone("Голубиная", "Перелетом", "+79000000003"))
catalog.append(Smartphone("Телетайп", "Фонфон", "+79000000004"))
for fhone in catalog:
    print(f"{fhone.brand} - {fhone.model}. {fhone.number}")
