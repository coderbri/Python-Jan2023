# User Class with Chaining Methods

This Python class, `User`, has been updated to include chaining methods, allowing for more concise and readable code when managing user profiles with membership and points systems. The class retains the following attributes and methods:

## User Attributes:

- `first_name`
- `last_name`
- `email`
- `age`

**Default Attributes:** (These are preset upon User instance)
- `is_rewards_member` (Default: False): Indicates if the user is a rewards program member.
- `gold_card_points` (Default: 0): Stores the user's gold card points.


## User Methods:

### `display_info(self)`
This method displays all user details on separate lines.

### `enroll(self)`
This method changes the user's member status to True and sets their gold card points to 200 if they are not already a member. If the user is already a member, it prints a message indicating that they are already enrolled and returns `False`. Otherwise, it returns `True`.


## Chained Methods:

With the addition of chaining methods, now actions can be performed multiple times on a user instance in a single line of code, making the code more concise and readable.

### `display_info(self) -> User`
This method displays all user details on separate lines and returns the user instance, allowing you to chain it with other methods.

### `enroll(self) -> User`
This method changes the user's member status to True and sets their gold card points to 200 if they are not already a member. If the user is already a member, it prints a message indicating that they are already enrolled and returns the user instance.

### `spend_points(self, amount_spent) -> User`
This method allows the user to spend gold card points. It checks if the user is a member and if they have enough points to spend the specified `amount_spent`. It handles various scenarios and returns the user instance.

## Example Usage:

```python
# Creating user instances and using chaining methods
user1 = User("Jane", "Doe", "jd@mail.com", 47)
user1.display_info().enroll().spend_points(50).enroll().display_info()

jsmith = User("John", "Smith", "js@dojo.com", 32)
jsmith.enroll().spend_points(80).display_info()

user1.enroll().spend_points(50).spend_points(150)
jsmith.spend_points(80).spend_points(121)

a_love = User("Ada", "Lovelace", "al@dojo.com", 24)
a_love.spend_points(40).display_info()
```

In this updated version, chaining methods make it easier to perform a sequence of actions on user instances. The code remains concise and readable, making it more efficient to manage user profiles with membership and points systems.

---
<p align="right">Completed: ２０２３年１０月０３日（火）</p> 