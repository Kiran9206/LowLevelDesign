'''
Builder Pattern Implementation for Building Queries
Problem Statement
You are tasked with developing a database management system that involves creating and executing SQL queries. Queries can vary in complexity,
involving different SELECT clauses, JOIN operations, WHERE conditions, and more. The current approach of constructing queries using concatenated
strings has proven to be error-prone, difficult to read, and challenging to modify. You should implement the Builder pattern to create instances
of query objects with various configurations, resulting in more maintainable and flexible code.

Assignment
Your task is to implement the Builder pattern to construct query objects with different configurations. The Builder pattern facilitates the
step-by-step construction of complex objects while keeping the creation process separate from the main object.

Implementing the Builder Pattern
Review the original class: You have been provided with a class named Query. This class represents SQL queries with different components. Your
 task is to implement the Builder pattern to create instances of a class with the same properties.

Create the builder class: Develop a new class called QueryBuilder that will implement the Builder pattern for creating query instances.
A starter class has been given for you to begin with. Don't forget to annotate the class with the @WithBuilder annotation. The actual name
of the class doesn't matter, as long as it is annotated.

Test your implementation: Test cases have been provided for you to verify the correctness of your implementation. Execute the test cases to ensure
the accuracy of your code.
'''


# step1: identify the complex object -> Query class
# step2: create a concrete product class -> Query

class Query:

    def __init__(self, select: set, from_table: str, where: set, join: str):
        self._select = select
        self._from_table = from_table
        self._where = where
        self._join = join

    def __str__(self):
        select_clause = ' , '.join(self._select) if self._select else '*'
        where_clause = ' AND '.join(self._where) if self._where else ''
        join_clause = self._join if self._join else ''
        query = f"SELECT {select_clause} FROM {self._from_table}"
        if where_clause:
            query += f" WHERE {where_clause}"
        if join_clause:
            query += f" {join_clause}"
        return query
# step3: create a builder class -> QueryBuilder

class QueryBuilder:

    def __init__(self):
        self._select = set()
        self._from_table = None
        self._where = set()
        self._join = None

    def add_select(self, column):
        if isinstance(column, (set, list, tuple)):
            self._select.update(column)
        else:
            self._select.add(column)
        return self

    def set_from(self, table: str):
        self._from_table = table
        return self

    def add_where(self, condition):
        if not condition:
            return self
        if isinstance(condition, (set, list, tuple)):
            self._where.update(condition)
        else:
            self._where.add(condition)
        return self

    def set_join(self, join_condition: str):
        self._join = join_condition
        return self

    def build(self) -> Query:
        if not self._from_table:
            raise ValueError("From table must be set before building the query.")
        return Query(self._select, self._from_table, self._where, self._join)

# step4: create a client class to use the builder
class Client:

    def __init__(self):
        self._builder = QueryBuilder()

    def create_query(self, select=None, from_table: str = None, where: set = None, join: str = None) -> Query:
        if select is None:
            select = {'*'}
        return (self._builder
                .add_select(select)
                .set_from(from_table)
                .add_where(where)
                .set_join(join)
                .build())

# Example usage
if __name__ == "__main__":
    client = Client()
    query = client.create_query(
        select= ('name', 'age'),
        from_table='users',
        where={'age > 18'},
        join='INNER JOIN another_table ON condition'
    )
    print(query)



