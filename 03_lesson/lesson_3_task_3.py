from address import Address
from mailing import Mailing

from_addr = Address("560000", "На деревню дедушке", "Зеленая", "5", "25")
to_addr = Address("560000", "На деревню Бабушке", "Красная Партизанская", "25", "5")
mail = Mailing(
    to_address=to_addr, from_address=from_addr, cost=350, track="286274637r6"
)
print(
    f"Отправление {mail.track} из {mail.from_address.index},"
    f" {mail.from_address.city}, {mail.from_address.street},"
    f" {mail.from_address.house} - {mail.from_address.apartment},"
    f" в {mail.to_address.index}, {mail.to_address.city}, "
    f" {mail.to_address.street}, {mail.to_address.house} -"
    f"{mail.to_address.apartment}. Стоимость {mail.cost} рублей."
)
