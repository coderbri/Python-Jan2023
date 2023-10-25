### ２０２３年１０月０６日（金）
---

## Topics to Cover

- **D6: SQL and ERD**
    - Overview
    - Database Design
    - One to One
    - One to Many
    - Many to Many
    - Normalization
    - Conventions
    - Data Types

### One-to-One

Relationships go in two directions. For example, one address has only one ZIP code, but one ZIP code can have many addresses, thus making it a different type of relationship. Below are some examples of One-to-One relationships:

- **Customers and Credit Cards** - Every Customer has one Credit Card, every Credit Card belongs to one Customer.
- **User and Email** - Every User has one Email Address, every Email Address has one User.
- **Product and Image** - Every Product has an Image, every Image is of a Product.


### One-to-Many

One-to-Many is probably the most common relationship used while making web applications. Often times a One-to-One relationship is actually much more similar to a One-to-Many. Below are a few examples:

- **Messages and Comments** - One Comment belongs to one Message, but one Message can have many Comments.
- **States and Cities** - One City is only in one State, but one State can have many Cities.
- **Customers and Orders** - One Order only has one Customer, but one Customer can have many Orders.

### Many-to-Many

Many-to-Many is often the most confusing type of relationship for lots of people, but if you make sure to talk-out the relationship out loud, you'll quickly find if it works or not. Remember, anytime you have a Many-to-Many, it will require some sort of joining table! Check out the below examples and use how we describe the relationship as a guide:

- **Users and Interests** - One User can have many Interests, one Interest can be applied to many Users.
- **Actors and Movies** - One Movie can have many Actors, one Actor can be in many Movies.
- **Businesses and Cities** - One Business can be spread across many Cities, one City can be home to many Businesses.


## Review Questions

### 1. **What is a database?**

A database in Python is a structured and organized collection of data that can be stored, retrieved, and manipulated using Python programming language. It provides a way to efficiently store and manage large amounts of data, making it accessible for various applications and data-driven tasks.

### 2. **Why use a DB?**

We should use a database for several reasons:
- **Data Persistence:** Databases allow us to store data persistently, meaning data remains available even after the program exits or the computer restarts.
- **Data Integrity:** Databases offer mechanisms to enforce data integrity constraints, ensuring that data remains accurate and consistent.
- **Efficient Data Retrieval:** Databases provide efficient methods to retrieve and query data, making it easier to extract specific information.
- **Concurrency Control:** Databases handle multiple users or processes accessing data simultaneously, ensuring data integrity and consistency.
- **Scalability:** Databases can scale to handle large datasets and high user loads, making them suitable for enterprise-level applications.
- **Data Security:** Databases offer security features like access control and encryption to protect sensitive information.

In summary, using a database enhances data management, reliability, and security while enabling efficient data retrieval and manipulation.
