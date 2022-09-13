import asyncio
import time

get_time = time.time()


async def tes():
    print("Thread Pertama")
    print(f"selesai pada {time.time() - get_time} detik\n")
    await asyncio.sleep(4) # Menunggu selama 4 detik
    print("Thread kedua")
    print(f"selesai pada {time.time() - get_time} detik\n")

async def get():
    await asyncio.gather(tes())

asyncio.run(get())
