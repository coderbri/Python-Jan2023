# User

This Python class, `User`, is for practicing Python OOP and designed to represent user profiles with various attributes and includes methods to manage user membership and points. The class has the following attributes and methods:

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

### `spend_points(self, amount_spent)`
This method allows the user to spend gold card points. It checks if the user is a member and if they have enough points to spend the specified `amount_spent`. It handles the following cases:
- If the user is not a member, it informs them that they cannot spend points until they enroll.
- If the user has insufficient points, it informs them of the payment failure.
- If the user is a member and has enough points, it deducts the points and confirms the successful payment.

## Example Usage:

```python
# Creating a user instance and enrolling in the rewards program
user1 = User("Jane", "Doe", "jd@mail.com", 47)
user1.display_info()
user1.enroll()

# Spending points
user1.spend_points(50)

# Creating another user instance
jsmith = User("John", "Smith", "js@dojo.com", 32)
jsmith.enroll()
jsmith.spend_points(80)

# Checking membership and spending points
user1.enroll()  # User is already a member.
user1.spend_points(50)
user1.spend_points(150)
```

In this example, we create user instances, enroll them in the rewards program, and demonstrate spending points. The code correctly handles membership checks and points spending based on the user's membership status and point balance.

---
<p align="right">Completed: ２０２３年１０月０１日（日）</p>