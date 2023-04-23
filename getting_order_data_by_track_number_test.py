import sender_stand_request
import data

def test_create_new_order_and_get_data_by_track():
    # Создаем заказ
    order_response = sender_stand_request.post_new_order(data.creating_an_order)
    assert order_response.status_code == 201

    # Получаем номер трека заказа и сохраняем его
    order_track_number = order_response.json()["Номер Заказа"]

    # Получаем данные о заказе по треку
    track_response = sender_stand_request.get_order_by_track(order_track_number)
    assert track_response.status_code == 200