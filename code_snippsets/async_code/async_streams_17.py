import asyncio

async def tcp_echo_client():
    reader, writer = await asyncio.open_connection('www.google.com', 80)

    print("Send request started...")
    request = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
    writer.write(request.encode())
    await writer.drain()

    data = await reader.read(1000)
    print(f"Get: {data.decode()!r}")

    print("Closing connection...")
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client())