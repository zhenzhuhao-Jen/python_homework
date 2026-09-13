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
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON p.product_id = li.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id  
    LIMIT 5
    """

    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        order_id = row[0]
        total = row[1]
        print(f"order_id: {order_id}, total_price: {total}")
    


    #Task 2: Understanding Subqueries

    #For each customer, find the average price of their orders.
    #price of each order : by order_id  SUM(p.price * li.quantity) AS 
    query = """
    SELECT c.customer_name, AVG(subquery.total_price) AS average_total_price
    FROM customers c 
    LEFT JOIN (
        SELECT o.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON p.product_id = li.product_id
        GROUP BY o.order_id, o.customer_id
        )  AS subquery
    ON c.customer_id = subquery.customer_id_b 
    GROUP BY c.customer_id, c.customer_name;
    """

    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(f"customer: {row[0]}, average_total_price: {row[1]}")



    #Task 3: An Insert Transaction Based on Data
    

    try:
        
        
        # find customer_id
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
        customer_id = cursor.fetchone()[0]
        #find employee_id
        cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
        employee_id = cursor.fetchone()[0]

        #find five cheapest products
        cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
        product_rows = cursor.fetchall()
        product_ids = [row[0] for row in product_rows]

        #begin traction:
        conn.execute("BEGIN")
        #insert step 1
        cursor.execute("""INSERT INTO orders (customer_id, employee_id, date) VALUES (?, ?, CURRENT_DATE) RETURNING order_id""", (customer_id, employee_id))
        new_order_id = cursor.fetchone()[0]
        #insert step 2
        for product_id in product_ids:
            cursor.execute(
            "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
            (new_order_id, product_id, 10)
            )
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
    rows = cursor.fetchall()
    for row in rows:
        print(row)




        


    #Task 4
    
    
    query = """
    SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS count_of_orders
    FROM employees AS e
    JOIN orders AS o ON e.employee_id = o.employee_id
    GROUP BY e.employee_id, e.first_name, e.last_name
    HAVING COUNT(o.order_id) > 5;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        employee_id, first_name, last_name, count_of_orders = row
        print(employee_id, first_name, last_name, count_of_orders)
    

