#Task5

import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    #line_item_id, quantity, product_id, product_name, and price
    sql_statement = """SELECT li.line_item_id, li.quantity, p.product_id, p.product_name, p.price FROM line_items li JOIN products p ON li.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(df)
    print(f'first 5 rows: \n{df.head()}')
    #add column 'Total'
    df['total'] = df['quantity'] * df['price']
    print(f'first 5 rows after add column total: \n{df.head()}')

    #group dataframe
    df = df.groupby('product_id').agg({'line_item_id': 'count', 'total': 'sum', 'product_name': 'first'}).reset_index()
    print(f'first 5 rows after group dataframe: \n{df.head()}')

    #Sort the DataFrame by the product_name column.
    df = df.sort_values(by='product_name')

    #write this dataframe to csv file
    df.to_csv('order_summary.csv')

    conn.close()
    
