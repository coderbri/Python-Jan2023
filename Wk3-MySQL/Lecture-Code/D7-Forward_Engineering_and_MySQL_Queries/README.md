# How to Forward Engineer in MySQL Workbench

**Disclaimer:** These instructions are provided for macOS. The steps may vary slightly on different operating systems.

## Forward Engineer to Database

1. On macOS, press ⌘G (Ctrl G on Windows) or navigate to the "Database" menu at the top and select "Forward Engineer."

2. If prompted, enter the legacy password to access the hostname in MySQL Workbench, then click "Next" to proceed.

## Set Options for Database to be Created

3. In the menu, navigate to the section labeled "Code Generation" and ensure the following options are checked:
    - "DROP objects before each create project & Generate DROP SCHEMA": This option replaces any existing database under the current schema name.
    - "Include model-attached scripts."

Click "Next" to continue.

## Review the SQL Script to be Executed

4. This page displays all the SQL code necessary to create the database based on the Entity-Relationship Diagram (ERD) model. Click "Next" to proceed to the next page.

5. You'll be directed to a menu to execute the forward engineering process. If all four checkboxes turn green, it means the process has succeeded. Now you can start adding data to the newly created database and write additional queries.

6. Don't forget to save the .mwb file containing the ERD so that others can generate the database when they download the project.

## Connecting to the Server

7. Return to the MySQL Workbench homepage and click on "LocalInstance" containing the MySQL Server. This is where applications connect when accessing the database.

8. Double-click the database you want to work on to ensure that your queries are directed to the correct database.

Now you are ready to use the forward-engineered database and perform operations on it.
