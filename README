# Private Chat Application using WebSocket

This project demonstrates a **private chat application** using **WebSocket** for real-time, bidirectional communication. The system allows multiple users to connect, chat publicly, or send private messages to specific users. The server is implemented in Python, and the client uses HTML and JavaScript.

---

## **What is WebSocket?**

WebSocket is a protocol that enables full-duplex communication between a client and a server over a single, long-lived TCP connection. Unlike HTTP, which is request-response based, WebSocket allows real-time, bidirectional data exchange, making it ideal for chat applications, live updates, and collaborative tools.

### **Key Features of WebSocket**
1. **Real-Time Communication**: Enables instant message delivery without polling the server.
2. **Full-Duplex**: Allows data to flow simultaneously in both directions.
3. **Persistent Connection**: Maintains a single connection for continuous communication.
4. **Lightweight Protocol**: Reduces overhead compared to HTTP requests.

---

## **How This Project Works**

### **Server (Python)**
The WebSocket server:
1. Manages client connections and stores each client’s username.
2. Handles two types of messages:
   - **Public Messages**: Broadcasted to all connected users.
   - **Private Messages**: Sent to a specific user using the `@username` format.
3. Ensures users have unique usernames to avoid conflicts.

### **Client (HTML + JavaScript)**
The client:
1. Connects to the WebSocket server.
2. Allows users to send messages using a simple chat interface.
3. Displays incoming messages in a chat box.
4. Supports private messaging using the `@username <message>` format.

---

## **Project Structure**

```
private-chat-project/
├── chat_server_private.py    # WebSocket server implementation in Python
├── chat_client_private.html  # WebSocket client implementation in HTML + JavaScript
├── requirements.txt          # Python dependencies
```

---

## **Setup Instructions**

### **1. Install Dependencies**
Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### **2. Run the WebSocket Server**
Start the server:
```bash
python chat_server_private.py
```
You should see:
```plaintext
Private chat server running on ws://localhost:6789
```

### **3. Open the WebSocket Client**
Open the `chat_client_private.html` file in multiple browser tabs or windows to simulate different users.

### **4. Chat Commands**
- **Send a Public Message**:
  Type a message and press **Enter** to send it to all connected users.
- **Send a Private Message**:
  Use the format `@username <message>` to send a message to a specific user.

---

## **Example Interaction**

### **User 1 (Alice)**
```plaintext
Enter your username: Alice
> @Bob Hi Bob, this is Alice!
> Hello everyone!
```

### **User 2 (Bob)**
```plaintext
Enter your username: Bob
Private from Alice: Hi Bob, this is Alice!
Alice: Hello everyone!
```

### **User 3 (Charlie)**
```plaintext
Enter your username: Charlie
Alice: Hello everyone!
```

---

## **How WebSocket Works in This Project**

1. **Connection Establishment**:
   - The client initiates a WebSocket connection with the server.
   - The server accepts the connection and registers the client with a unique username.

2. **Message Handling**:
   - **Public Messages**:
     - Broadcasted to all connected clients except the sender.
   - **Private Messages**:
     - Sent directly to the intended recipient based on the `@username` format.

3. **Disconnection**:
   - When a client disconnects, the server removes the client from its list of active connections.

---

## **Enhancements to Consider**

1. **User List**:
   - Show a list of active users to all connected clients.

2. **Security**:
   - Use SSL/TLS for secure communication (`wss://` instead of `ws://`).
   - Add user authentication with JWT.

3. **Persistent Chat**:
   - Store messages in a database for retrieval after disconnection.

4. **Improved UI**:
   - Add separate tabs or sections for private and public chats.

---

## **Conclusion**
This project provides a foundational understanding of how to use WebSocket for real-time communication. It demonstrates:
- Managing multiple clients in a WebSocket server.
- Implementing public and private messaging.
- Creating a simple chat interface using HTML and JavaScript.

WebSocket’s real-time capabilities make it an excellent choice for chat applications, live dashboards, and collaborative tools. Let me know if you’d like assistance with further enhancements! 🚀

