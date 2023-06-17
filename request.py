import configuration
import request
import data


def create_new_order(): # запрос на создание нового заказа
    return request.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,  # подставялем полный url
                         json=data.order_body)  # а здесь тело



def get_orders_track(track_id): # запрос на получение заказа по его трек номеру
    return request.get(configuration.URL_SERVICE + configuration.RECEIVING_ORDER_BY_ID + str(track_id))
