'''
Connection Pool
Problem Statement
You are tasked with designing a connection pool for a database management module of a complex software application. The connection pool is
responsible for managing database connections efficiently to avoid unnecessary overhead and ensure optimal resource usage. To prevent multiple
instances of the connection pool manager and ensure thread-safe access to connections, you need to implement the Singleton design pattern along
with the connection pool management functionality.

Assignment
Your task is to implement the ConnectionPool interface that follows the Singleton design pattern to manage a pool of database connections.

Part 1: Implementing Singleton and Connection Pool
Implement the Singleton design pattern: Create a class that implements the ConnectionPool interface. Implement the Singleton design pattern
within this class to ensure that only one instance of the connection pool manager can exist within the program.

Implement the get_instance(max_connections) and reset_instance() methods: Implement the get_instance(maxConnections) method in the
ConnectionPoolImpl class. This method should return the singleton instance of the connection pool manager class. Also, implement the
reset_instance() method to reset the singleton instance to null.

Part 2: Connection Pool Management
In connection pooling, the aim is to efficiently handle a group of database connections. This ensures optimal resource usage and effective
sharing of connections across different parts of the software.

Here's an analogy to help you understand the concept of connection pooling. Imagine a library with a large collection of books. The library
has a shelf where all the books are kept. When a reader wants to borrow a book, they go to the shelf, pick up the book, and take it to a
reading table. When they are done reading, they return the book to the shelf. The library keeps track of which books are available and which
ones are currently being used by readers.

You have to implement the following methods:

initialize_pool(): This method is responsible for initializing the connection pool. It should create a fixed number of connections and add
them to the pool. Use the DatabaseConnection class to create dummy connections. Store the connections in a data structure of your choice,
but you will have to track which connections are available and which ones are currently in use.
get_connection(): This method is responsible for providing a connection to the caller. It should return a connection from the pool of
available connections. Once a connection is returned, it should be marked as "unavailable" so that other parts of the software don't use it.
release_connection(connection): This method is responsible for releasing a connection back to the pool. It should mark the connection as
"available" so that other parts of the software can use it.
get_available_connections_count(): Implement this method to count how many "available" connections remain in the pool.
get_total_connections_count(): This method is about determining the total number of connections, whether they are currently in use or not.
Instructions
Clone this repository to your local machine.
Implement the ConnectionPool interface and the required methods as specified above.
Ensure that your implementation follows the Singleton design pattern and provides proper connection pool management.
Run the provided test cases in the ConnectionPoolTest class to verify the correctness of your implementation.
'''

import threading

class DatabaseConnection:
    def __init__(self, connection_id: int):
        self.connection_id = connection_id

    def __str__(self):
        return f"DatabaseConnection({self.connection_id})"

class ConnectionPool:
    def initialize_pool(self):
        raise NotImplementedError("initialize_pool method is not implemented!!")

    def get_connection(self) -> object:
        raise NotImplementedError("get_connection method is not implemented!!")

    def release_connection(self, connection: object):
        raise NotImplementedError("release_connection method is not implemented!!")

    def get_available_connections_count(self) -> int:
        raise NotImplementedError("get_available_connections_count method is not implemented!!")

    def get_total_connections_count(self) -> int:
        raise NotImplementedError("get_total_connections_count method is not implemented!!")

class ConnectionPoolImpl(ConnectionPool):
    __instance = None
    __lock = threading.Lock()

    def __init__(self, max_connections: int):
        self.max_connections = max_connections
        self.available_connections = []
        self.in_use_connections = []
        self._pool_lock = threading.Lock()
        self.initialize_pool()

    @classmethod
    def get_instance(cls, max_connections: int) -> "ConnectionPoolImpl":
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = ConnectionPoolImpl(max_connections)
        return cls.__instance

    @classmethod
    def reset_instance(cls):
        with cls.__lock:
            cls.__instance = None

    def initialize_pool(self):
        for i in range(self.max_connections):
            conn = DatabaseConnection(i + 1)
            self.available_connections.append(conn)

    def get_connection(self):
        with self._pool_lock:
            if self.available_connections:
                conn = self.available_connections.pop()
                self.in_use_connections.append(conn)
                return conn
            raise ConnectionError("No available connections!")

    def release_connection(self, connection: DatabaseConnection):
        if not isinstance(connection, DatabaseConnection):
            print(f"Invalid connection object: {connection}")
            return
        with self._pool_lock:
            if connection in self.in_use_connections:
                self.in_use_connections.remove(connection)
                self.available_connections.append(connection)
            else:
                print(f"{connection} is not in use!")

    def get_available_connections_count(self):
        with self._pool_lock:
            return len(self.available_connections)

    def get_total_connections_count(self):
        return self.max_connections

if __name__ == "__main__":
    pool = ConnectionPoolImpl.get_instance(5)
    conn1 = pool.get_connection()
    conn2 = pool.get_connection()

    print(f"Available Connections: {pool.get_available_connections_count()}")
    print(f"Total Connections: {pool.get_total_connections_count()}")

    pool.release_connection(conn1)
    pool.release_connection(1)  # Should print invalid connection object warning
