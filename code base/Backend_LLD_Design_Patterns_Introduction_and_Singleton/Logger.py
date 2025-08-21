'''
Logger
Problem Statement
You are tasked with developing a logging module for a complex software application. The logging module needs to maintain a single log file
throughout the application's execution to avoid file access conflicts and ensure consistency. To prevent multiple instances of the logging
module and ensure thread-safe access to the log file, you need to implement the Singleton design pattern along with the logging functionality.

Assignment
Your task is to complete the implementation of the Logger interface that follows the Singleton design pattern to manage logging operations
and maintain a single log file.

Part 1: Implementing Singleton and Logger
Implement the Singleton design pattern: There is a class LoggerImpl that implements the Logger interface. Implement the Singleton design pattern
 within this class to ensure that only one instance of the logger can exist within the program.

Implement the get_instance() and reset_instance() methods: Implement the get_instance() method in the LoggerImpl class. This method should
return the singleton instance of the logger class. Also, implement the reset_instance() method to reset the singleton instance to null.

Part 2: Logging Operations
The logger module is responsible for recording log messages of different levels in a single log file. Think of it as a central place where
various parts of your software can write messages for debugging or monitoring purposes.

You have to implement the following methods:

set_log_file(filePath): This method sets the log file path. The logger will write log messages to this file. Look at using the TextIO classes
to write to the log file. You can initialise them at the class level.
log(level, message): This method is responsible for logging a message with a specified log level. The log message should include a timestamp,
log level, and the provided message. Throw an Error if the logger is not initialised using the set_log_file() method.
get_log_file(): This method returns the current log file path.
flush(): This method flushes any buffered log entries to the log file. Find the appropriate method to use from the TextIO class.
close(): This method closes the logger and releases any resources. Find the appropriate method to use from the TextIO class.
Instructions
Clone this repository to your local machine.
Implement the Logger interface and the required methods as specified above.
Ensure that your implementation follows the Singleton design pattern and provides proper logging functionality.
Run the provided test cases in the LoggerTest class to verify the correctness of your implementation.
'''

import threading

# create a logger interface...
class Logger:

    def set_log_file(self,filePath):
        raise NotImplementedError

    def log(self,level, message):
        raise NotImplementedError

    def get_log_file(self):
        raise NotImplementedError

    def flush(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

class LoggerImpl(Logger):
    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        self.log_filepath = None
        self.file = None

    @classmethod
    def get_instance(cls)-> "LoggerImpl":
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = LoggerImpl()
        return cls.__instance

    @classmethod
    def reset_instance(cls):
        with cls.__lock:
            if cls.__instance and cls.__instance.file:
                cls.__instance.file.close()
            cls.__instance = None

    def set_log_file(self,filePath):
        with self.__lock:
            if self.file:
                self.file.close()
            self.log_filepath = filePath
            self.file = open(self.log_filepath, 'a')

    def log(self,level, message):
        with self.__lock:
            if self.log_filepath:
                from datetime import datetime
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_entry = f"{timestamp} - {level} - {message}\n"
                self.file.write(log_entry)
            else: raise Exception("Logger not initialized. Please set the log file path using set_log_file().")

    def get_log_file(self)-> str:
        return self.log_filepath

    def flush(self):
        with self.__lock:
            if self.file:
                self.file.flush()
            else: raise Exception("Logger not initialized. Please set the log file path using set_log_file().")

    def close(self):
        with self.__lock:
            if self.file:
                self.file.close()
                self.file = None
            else: raise Exception("Logger not initialized. Please set the log file path using set_log_file().")



if __name__ == "__main__":
    log = LoggerImpl.get_instance()
    log.set_log_file('app.log')
    log.log('INFO', 'This is an info message.')
    log.log('ERROR', 'This is an error message.')
    print(f"Log file path: {log.get_log_file()}")
