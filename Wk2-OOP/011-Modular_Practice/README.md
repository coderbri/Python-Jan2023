# Modular Practice

This project explores the concept of modularizing and importing in Python. Modularizing allows us to organize our code into separate files, making it more manageable and reusable. By importing modules, we can access code from one file in another, facilitating code organization and separation of concerns.

## Project Structure

- `parent.py`: This Python file serves as the parent module and contains a local variable, a function, and a class definition. It demonstrates how to structure a module with various components.

- `child.py`: In this file, we import the `parent` module, showcasing how to use modules in Python and making the code within the `parent` module accessible to the `child` module.

## Running the Code

To see how the code works, you can run the following commands from your terminal:

1. Execute `parent.py`:

   ```bash
   python3 parent.py
   ```

   This will demonstrate the functionality of the `parent` module.

2. Execute `child.py`:

   ```bash
   python3 child.py
   ```

   This will show how to import the `parent` module into the `child` module, making its functions and classes available.

## Understanding Namespace and `__name__`

In Python, the concept of a namespace refers to which variables, functions, and classes are accessible at a specific point during program execution. The `__name__` variable is used to control the behavior of a module when it's executed directly or imported into another module.

1. In `parent.py`, you can observe how `__name__` works:

    ```python
    if __name__ == "__main__":
        print("The file is being executed directly")
    else:
        print("The file is being executed because it is imported by another file. The file is called:", __name__)
    ```
    
   Running `parent.py` directly will display the first message, while running `child.py` will display the second message.

This functionality is useful for ensuring that certain code blocks are only executed when a module is run directly, preventing unintended code execution during imports.

## Example Use Case

Consider a scenario where one class depends on another. By using `__name__`, you can write test code or additional functionality in a module that only runs when the module is executed directly, keeping the imported module clean and focused.

```python
if __name__ == "__main__":
    product = Product([args])
    print(product)
    print(product.add_tax(0.18))
```

This ensures that the test code runs only when the module is executed directly and not when imported by another module.

Enjoy modularizing and organizing your Python code for better maintainability!

---
<p align="right">Completed: ２０２３年１０月２７日（金）</p>