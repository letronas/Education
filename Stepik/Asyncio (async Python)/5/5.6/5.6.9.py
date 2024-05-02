import asyncio
import time

equipment_list = ['#001 ps5f6537c5-506f-43c2-b095-1890ef579c52: 265 units',
                  '#002 ps5ec3020b-022f-466b-845a-a8f11161a6d1: 39 units',
                  '#003 psb5c6c090-4f1a-4741-936e-5fe2b3e8d181: 242 units',
                  '#004 ps10c90127-a4a5-4f85-b23f-66421ab04b09: 108 units',
                  '#005 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units']


def query_time():
    return time.time()


# Корутина для отправки запроса.
async def equipment_request(request: str):
    await asyncio.sleep(1)
    return request.split(" ")[0]+" is Ok!"

# Корутина для управления отправкой запросов на заказ оборудования
async def send_requests():
    tasks = [equipment_request(equipment) for equipment in equipment_list]
    res = await asyncio.gather(*tasks)
    waiting_time = query_time() # В метод ничего передавать не нужно!
    # print(*res, sep='\n')
    print(f"На отправку {len(equipment_list)} запросов потребовалось {waiting_time} секунд!")


async def main():
    await send_requests()


asyncio.run(main())
