# Online Python compiler (interpreter)
# Write and run Python online using this editor.
# asyncio implements asynchronous programming using a single-threaded event loop.

import asyncio
import time

# KEY POINT 1: DEFINING COROUTINES WITH 'async def'
# Prefixing a function with 'async def' marks it as a coroutine. 
# Calling this function does not run it immediately; it returns a coroutine object 
# that is ready to be scheduled and executed by Python's event loop.
async def download_file(id):
  print(f"Download file started, id:{id}")
  await asyncio.sleep(2)
  # Yields control back to the event loop
   # KEY POINT 2: COOPERATIVE MULTITASKING & NON-BLOCKING I/O
    # 'await asyncio.sleep(1)' simulates an I/O operation (like an API fetch).
    # The 'await' keyword pauses this specific coroutine and yields control back to 
    # the event loop. Unlike 'time.sleep()', it does NOT block or freeze the thread.
  print(f"Download file ended, id:{id}")
  return f"File {id}"

async def main():
  start = time.perf_counter()

    # KEY POINT 3: CONCURRENT EXECUTION WITH 'asyncio.gather()'
    # 'asyncio.gather()' submits all three tasks to the event loop simultaneously.
    # Because the I/O steps are non-blocking, the loop switches context between 
    # tasks instantly. Total time is ~1 second (max single delay) instead of 3 seconds.
  
  results = await asyncio.gather(download_file(1),
                                download_file(2))

  end = time.perf_counter()
  print(f"\nDownloaded {len(results)} files concurrently in {end - start:.2f} seconds!")

if __name__ == "__main__":
      # KEY POINT 4: MANAGING THE EVENT LOOP LIFECYCLE
    # 'asyncio.run(main())' acts as the standard entry point. It creates a brand-new
    # event loop, runs the passed orchestrator coroutine, and gracefully closes the loop
    # after everything finishes.
  asyncio.run(main())



-----------------------------------------------------


You are **exactly right**. In a real production application, you will **never** use `asyncio.sleep()` to fetch data or download files. 

In production, `asyncio.sleep()` is replaced by **real network client libraries** that handle true asynchronous I/O (like calling an API, querying a database, or reading a file). 

---

### 🔄 What Replaces it in Production?

| What we used in the mock code | What we use in Production | Why? |
| :--- | :--- | :--- |
| **`asyncio.sleep()`** | **`await session.get(url)`** (using aiohttp or httpx) | Makes an actual async HTTP request over the network. |
| **`asyncio.sleep()`** | **`await connection.fetch(query)`** (using asyncpg) | Executes an async database query. |
| **`asyncio.sleep()`** | **`await file.read()`** (using aiofiles) | Reads a file from the hard drive without blocking the thread. |

---

### 🚀 Production-Grade Code Example

If you want to blow your interviewer away, show them how this looks using a **real production library** like `httpx` (a popular modern async HTTP client). 

*Note: Remind the interviewer that you would normally run `pip install httpx` first.*

```python
import asyncio
import time
import httpx  # Production-grade async HTTP client

# 1. Real Production Async Fetch
async def fetch_pokemon(client: httpx.AsyncClient, pokemon_id: int) -> dict:
    url = f"https://pokeapi.co{pokemon_id}"
    print(f"Requesting data for Pokémon {pokemon_id}...")
    
    # REPLACEMENT: Instead of asyncio.sleep(), this waits for a REAL network call 
    # non-blockingly while yielding control to other network tasks.
    response = await client.get(url)
    
    print(f"Received data for Pokémon {pokemon_id}!")
    return response.json()

async def main():
    start = time.perf_counter()
    
    # httpx.AsyncClient manages a connection pool efficiently for production
    async with httpx.AsyncClient() as client:
        # Create a list of 3 concurrent network requests
        tasks = [fetch_pokemon(client, i) for i in]
        
        # Fire them all simultaneously over the actual internet
        results = await asyncio.gather(*tasks)
        
    end = time.perf_counter()
    print(f"\nFetched {len(results)} items from real API in {end - start:.2f} seconds!")

if __name__ == "__main__":
    asyncio.run(main())
```

### 🎯 Key Interviewer Talking Point
Tell the interviewer: 
> *"In a real production environment, `asyncio.sleep()` is only used for retry backoff algorithms or rate limiting. 
For actual I/O, we use libraries like `httpx` or `aiohttp` because their core network engines are explicitly written to yield control back to the event loop while waiting for network packets to arrive."*


The difference lies in who freezes while waiting.
time.sleep() freezes your entire program execution thread, 
whereas asyncio.sleep() only freezes that one specific task, leaving the thread free to work on other things.
  
Think of your program like a single chef in a kitchen:

Metric	time.sleep(5) (Blocking)	asyncio.sleep(5) (Pausing / Non-blocking)
The Analogy	The chef puts water on to boil, stands completely still, and stares at the pot for 5 minutes doing absolutely nothing else.	The chef puts water on to boil, sets a timer, and walks away to chop vegetables while the water heats up.
System Behavior	Blocks the OS thread. No other line of Python code in your program can run until the timer ends.	Pauses the current function, returns control to the asyncio event loop, and immediately jumps to run other active tasks.
Resource Usage	Wastes CPU time by forcing it to idle.	Maximizes CPU time by keeping it busy with other waiting work.
Usage Context	Standard, traditional Python code.	Inside an async def function, right after the await keyword.
