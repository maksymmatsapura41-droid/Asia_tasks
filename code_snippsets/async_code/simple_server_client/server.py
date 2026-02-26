import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Получено {message!r} от {addr!r}")

    print(f"Отправка: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Закрываем соединение")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Слушаю на {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())