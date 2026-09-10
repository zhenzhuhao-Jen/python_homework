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
    SELECT o.order_id, SUM(p.price * li.quantity) AS total
    FROM orders o
    RIGHT JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON p.product_id = li.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id  
    LIMIT 5
    """

    cursor.execute(query)
    print(cursor.fetchall())

    #conn.close()


    #Task 2: Understanding Subqueries

    #For each customer, find the average price of their orders.
    #price of each order : by order_id  SUM(p.price * li.quantity) AS 
    query = """
    SELECT c.customer_name, AVG(subquery.total_price) AS average_total_price
    FROM customers c 
    LEFT JOIN (
        SELECT c.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
        FROM customers c
        JOIN orders o ON  c.customer_id = o.customer_id
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON p.product_id = li.product_id
        GROUP BY o.order_id
        )  AS subquery
    ON c.customer_id = subquery.customer_id_b 
    GROUP BY c.customer_id;
    """

    cursor.execute(query)
    print(cursor.fetchall())



    #Task 3: An Insert Transaction Based on Data
    # Then, using a SELECT with a JOIN, print out the list of line_item_ids for the order 
    # along with the quantity and product name for each.

    try:
        cursor.execute("""
        INSERT INTO orders (customer_id, employee_id, date)

        SELECT c.customer_id, e.employee_id, CURRENT_DATE AS date
        FROM customers c, employees e
        WHERE c.customer_name = 'Perez and Sons'
            AND e.first_name = 'Miranda' AND e.last_name = 'Harris'
        RETURNING order_id;
        """)
        new_order_id = cursor.fetchone()[0]
        cursor.execute("""
        INSERT INTO line_items (order_id, product_id, quantity)
        SELECT ?, p.product_id, 10 AS quantity
        FROM products p
        ORDER BY p.price ASC
        LIMIT 5;
        """, (new_order_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print("error:", e)
    
    print( "result after adding the new order:")
    query = """
    SELECT li.line_item_id, li.quantity, p.product_name
    FROM line_items AS li
    JOIN products AS p ON li.product_id = p.product_id
    WHERE li.order_id = ?
    """
    cursor.execute(query,(new_order_id,))
    print(cursor.fetchall())


    #Task 4: Aggregation with HAVING
    
    
    query = """
    SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS count_of_orders
    FROM employees AS e
    JOIN orders AS o ON e.employee_id = o.employee_id
    GROUP BY o.employee_id
    HAVING COUNT(o.order_id) > 5;
    """
    cursor.execute(query)
    print(cursor.fetchall())

