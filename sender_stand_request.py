
import configuration
import requests


def post_new_order(creating_an_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=creating_an_order)
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_BY_TRACK + f'{track}')