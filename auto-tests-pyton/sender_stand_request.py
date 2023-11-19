import requests

import configuration
import data


def post_new_order(body):
    return requests.post(
        url=f"{configuration.URL_SERVICE}{configuration.CREATE_ORDER}",  # подставляем полный url
        json=body,  # тут тело
        headers=data.headers  # а здесь заголовки
    )


def get_order_by_track(track):
    track_params = {"t": f"{track}"}

    return requests.get(
        url=f"{configuration.URL_SERVICE}{configuration.GET_ORDER}",
        params=track_params
    )
