import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Populate staging tables from S3

    Args:
        conn: (connection) instance of connection class
        cur: (cursor) instance of cursor class

    Returns:
        none
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Populate fact and dimention tables from staging tables

    Args:
        conn: (connection) instance of connection class
        cur: (cursor) instance of cursor class

    Returns:
        none
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    # Establish the connection to database
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    
    # Create cusor object
    cur = conn.cursor()
    
    # forming the connection
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()