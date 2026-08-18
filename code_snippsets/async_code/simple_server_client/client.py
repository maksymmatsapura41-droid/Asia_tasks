import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f'Отправка: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Получено: {data.decode()!r}')

    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hi!'))