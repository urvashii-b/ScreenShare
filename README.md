# Python Screen Sharing via VidStream

This project facilitates screen sharing between a client and server using Python. The client (`sender.py`) streams its desktop to the server (`receiver.py`), which processes the image data and displays it. This enables multiple clients to share their screens simultaneously as well. Additionally, the implementation uses threads to allow stopping the sharing process at any time.

## Prerequisites

Ensure you have installed the `vidstream` library. If not, you can install it via pip:

```bash
pip install vidstream
```

## Usage

To run this application:

1. **Run `receiver.py` from VSCode Terminal:**
    - Open VSCode.
    - Open the integrated terminal (Ctrl+` or View -> Terminal).
    - Navigate to the project directory.
    - Run the command:
    ```bash
    python receiver.py
    ```
    The server will await incoming connections from clients.

2. **Run `sender.py` from Command Line:**
    - Open a command prompt or terminal.
    - Navigate to the project directory.
    - Run the command:
    ```bash
    python sender.py
    ```
    The client will initiate screen sharing and transmit the desktop stream to the server.

3. **Stopping the Process:**
    You can stop the screen sharing process at any time by using the appropriate termination command (e.g., keyboard interrupt). 'STOP' is used here.

## Notes

- Ensure proper network connectivity between the client and server for seamless screen sharing.
- Multiple clients can concurrently share their screens with the server.
- Inter computer screen sharing is possible too. Just change the public ipv4 address in the sender.py file
