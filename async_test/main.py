import asyncio 
from util import delay
 
 
async def hello_every_second(): 
    for i in range(12): 
        await asyncio.sleep(0.1) 
        print("Ich führe anderen Code aus, während ich warte!") 
 
 
async def main(): 
    first_delay = asyncio.create_task(delay.delay(3)) 
    second_delay = asyncio.create_task(delay.delay(3)) 
    await hello_every_second() 
    await first_delay 
    await second_delay

asyncio.run(main())