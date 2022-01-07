# sqlaichemy_operation


# Creating Session #
When using SQLAlchemy ORM, we interact with the database using the Session object. The Session object also wraps the database connection and transaction. The transaction implicitly starts as soon as the Session starts communicating with the database and will remain open until the Session is committed, rolled back or closed.
One way to create a Session object is to use the Session class from the sqlalchemy.orm package.

from sqlalchemy.orm import create_engine, Session
engine = create_engine("postgres+psycopg2://postgres:pass@localhost/mydb")
session = Session(bind=engine)

To make things easier, SQLAlchemy provides sessionmaker class which creates Session class with default arguments set for its constructor.

You should call call sessionmaker once in your application at the global scope.

# Querying Data
To query database we use the query() method of the session object. The query() method returns an object of type sqlalchemy.orm.query.Query, simply called Query. The Query object represents the SELECT statement that will be used to query the database. The following table lists some common methods of the Query class.

# all() method
In its simplest form, the query() method can take one or more model class or columns as arguments.

# filter() method
The filter() method allows us to filter the result by adding WHERE clause to the query. At the minimum, it accepts a column, an operator and a value.

# IN
session.query(Customer).filter(Employee.first_name.in_(['Toby', 'Sarah'])).all()


