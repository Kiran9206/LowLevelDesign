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
Implement the Singleton design pattern: Create a class that implements the ConnectionPool interface. Implement the Singleton design pattern within
 this class to ensure that only one instance of the connection pool manager can exist within the program.

Implement the getInstance(int maxConnections) and resetInstance() methods: Implement the getInstance(int maxConnections) method in the
ConnectionPoolSolution class. This method should return the singleton instance of the connection pool manager class. Also, implement the
resetInstance() method to reset the singleton instance to null.

Part 2: Connection Pool Management
In connection pooling, the aim is to efficiently handle a group of database connections. This ensures optimal resource usage and effective
sharing of connections across different parts of the software.

Here's an analogy to help you understand the concept of connection pooling. Imagine a library with a large collection of books. The library
has a shelf where all the books are kept. When a reader wants to borrow a book, they go to the shelf, pick up the book, and take it to a reading
 table. When they are done reading, they return the book to the shelf. The library keeps track of which books are available and which ones are
 currently being used by readers.

You have to implement the following methods:

void initializePool(): This method is responsible for initializing the connection pool. It should create a fixed number of connections and add
 them to the pool. Use the DummyConnection class to create dummy connections. Store the connections in a data structure of your choice, but you
  will have to track which connections are available and which ones are currently in use.
Connection getConnection(): This method is responsible for providing a connection to the caller. It should return a connection from the pool of
available connections. Once a connection is returned, it should be marked as "unavailable" so that other parts of the software don't use it.
void releaseConnection(Connection connection): This method is responsible for releasing a connection back to the pool. It should mark the
connection as "available" so that other parts of the software can use it.
int getAvailableConnectionsCount(): Implement this method to count how many "available" connections remain in the pool.
int getTotalConnectionsCount(): This method is about determining the total number of connections, whether they are currently in use or not.
'''
import threading

class DummyConnection:
    def __init__(self, connection_id: int):
        self.connection_id = connection_id

    def __str__(self):
        return f"DummyConnection({self.connection_id})"



class ConnectionPool:

    def initializePool(self):
        raise NotImplementedError("initializePool method is not implemented!!")

    def getConnection(self)-> object:
        raise NotImplementedError("getConnection method is not implemented!!")

    def releaseConnection(self, connection: object):
        raise NotImplementedError("releaseConnection method is not implemented!!")

    def getAvailableConnectionsCount(self)->int:
        raise NotImplementedError("getAvailableConnectionsCount method is not implemented!!")

    def getTotalConnectionsCount(self)-> int:
        raise NotImplementedError("getTotalConnectionsCount method is not implemented!!")


class ConnectionPoolSolution(ConnectionPool):
    __instance = None
    __lock = threading.Lock()

    def __init__(self, maxConnections: int):
        self.maxConnections = maxConnections
        self.availableConnection = []
        self.in_use = []
        self.initializePool()

    @classmethod
    def getInstance(cls, maxConnections: int)-> "ConnectionPoolSolution":
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = ConnectionPoolSolution(maxConnections)
        return cls.__instance


    @classmethod
    def resetInstance(cls):
        cls.__instance = None

    def initializePool(self):
        for i in range(self.maxConnections):
            connection = DummyConnection(i+1)
            self.availableConnection.append(connection)

    def getConnection(self):
        with self.__lock:
            if self.availableConnection:
                connection = self.availableConnection.pop()
                self.in_use.append(connection)
                return connection
            raise ConnectionError("No available connections!")

    def releaseConnection(self, connection: DummyConnection):
        with self.__lock:
            if connection in self.in_use:
                self.in_use.remove(connection)
                self.availableConnection.append(connection)
            else: print(f"{connection} is not in use!")

    def getAvailableConnectionsCount(self):
        return len(self.availableConnection)

    def getTotalConnectionsCount(self):
        return self.maxConnections


if __name__ == "__main__":

    pool = ConnectionPoolSolution.getInstance(5)
    conn1 = pool.getConnection()
    conn2 =pool.getConnection()
    print(f"Available Connections: {pool.getAvailableConnectionsCount()}")
    print(f"Total Connections: {pool.getTotalConnectionsCount()}")
    pool.releaseConnection(conn1)
    pool.releaseConnection(1)





