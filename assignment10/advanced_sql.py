#Task1

import sqlite3

#open file

with sqlite3.connect("../db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") 
    cursor = conn.cursor()


    #Find the total price of each of the first 5 orders. total for each order   
    # You need to join the orders table with the line_items table and the products table. 
    # You need to GROUP_BY the order_id.  
    # You need to select the order_id and the SUM of the product price times the line_item quantity.  
    # Then, you ORDER BY order_id and LIMIT 5.  You don't need a subquery. 
    # Print out the order_id and the total price for each of the rows returned.
    query = """
    SELECT order_id, SUM(products.price * line_items.quantity)
    FROM orders
    RIGHT JOIN line_items ON orders.order_id = line_items.order_id
    JOIN products ON products.product_id = line_items.product_id
    GROUP BY order_id
    ORDER BY order_id and LIMIT 5
    """

    cursor.execute(query)
    print(cursor.fetchall())

    #conn.close()
     