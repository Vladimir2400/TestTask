import numpy as np


def distance(point_A, point_B):
    #Формула расстоняия Евклида
    return np.sqrt(point_A[0] - point_B[0] ** 2 + (point_A[1] - point_B[2]) ** 2)

#прочитал не внимательно задание и расчет стоимости доставки можете не смотреть 
def order_cost(order, cost_per_km):
    #Расстояние между точками А и Б
    distance_AB = distance(order['point_A'], order['point_B'])

    #Расчет стоимости заказа
    cost = distance_AB * cost_per_km

    return cost

def order_courier(orders, couriers):
    #Принятые заказы
    accepted_orders = []
    for orders in orders:
        #Расстояние от курьера до точки А
        distances = [distance(courier['location'], order['point_A']) for courier in couriers]
        #Поиск блмжайшего курьера
        nearest_courier = np.argmin(distances)
        #Назначить заказ курьеру
        accepted_orders.append((order, couriers[nearest_courier]))
        #Обновленыые гео-еоординат до точки Б
        couriers[nearest_courier]['location'] = order['point_B']

    return accepted_orders
