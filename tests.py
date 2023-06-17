import request

#Добрыдина Наталья, 5-ая когорта "Финальный проект, инженер по тестированию"
# Тест проверки создания заказа
def test_order_creation():
    creation_response = request.create_new_order
    track_id = creation_response.json['track_id']
    response = request.get_orders_track
    assert response.status.code == 200
