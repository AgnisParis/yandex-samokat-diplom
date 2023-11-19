# Лысенко Агнетта 10-ая когорта - Финальный проект. Инженер по тестированию плюс.
import pytest

import data
import sender_stand_request


class TestClass:

    @pytest.fixture(scope="class")
    def gen_order_track(self):
        """
        Фикстура генерации заказа и получения его трека. Применяется 1 раз для всех тестов класса

        :return: Трек заказа
        """
        body = data.order_body.copy()
        response = sender_stand_request.post_new_order(body)
        return response.json()["track"]

    def test_get_order_by_track(self, gen_order_track):
        """
        Проверка получения запроса на получение заказа по треку заказа

        :return: Соответствие кода запроса статусу 200
        """
        response = sender_stand_request.get_order_by_track(gen_order_track)

        assert response.status_code == 200
