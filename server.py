import asyncio
import websockets
import subprocess
import sys

# Force Python to flush output immediately
sys.stdout.reconfigure(line_buffering=True)

async def terminal(websocket, path):
    print("Client connected")

    # Run the Python script in unbuffered mode ("-u" flag)
    process = await asyncio.create_subprocess_exec(
        "python", "-u", "/codes/wordle.py",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE
    )

    async def handle_input():
        try:
            async for message in websocket:
                print(f"Received input: {message.strip()}")  # Debugging
                process.stdin.write(f"{message}\n".encode())
                await process.stdin.drain()
        except websockets.exceptions.ConnectionClosed:
            print("Client disconnected (input stream closed)")

    async def read_output(stream, prefix=""):
        """ Reads output from process and sends it to WebSocket. """
        while True:
            line = await stream.readline()
            if not line:
                break
            output = prefix + line.decode()
            print(f"Sending output: {output.strip()}")  # Debugging
            await websocket.send(output)

    try:
        await asyncio.gather(
            handle_input(),
            read_output(process.stdout),
            read_output(process.stderr, "Error: ")
        )
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        print("Closing process...")
        process.terminate()
        await process.wait()  # Ensure clean exit

# Start WebSocket server
start_server = websockets.serve(terminal, "localhost", 5000)

print("✅ WebSocket server started on port 5000")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
