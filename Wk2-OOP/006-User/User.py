class User:
    
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # Default  Attributes
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def display_membership_status(self):
        print(f"- Membership: {self.is_rewards_member}")
        print(f"- Gold Card Points: {self.gold_card_points}pts")
    
    def display_info(self):
        print(f"\n==== DISPLAY INFO: { self.display_full_name() } ====")
        print(f"- First Name: {self.first_name}")
        print(f"- Last Name: {self.last_name}")
        print(f"- Email: {self.email}")
        print(f"- Age: {self.age}")
        print("-----------------------------\nMEMBERSHIP STATUS")
        self.display_membership_status()
    
    def enroll(self):
        print(f"\n===== ENROLLEMENT STATUS =====")
        if self.is_rewards_member:
            print(f"This user [{ self.display_full_name() }] is already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            self.display_membership_status()
            print(f"-----------------------------\nThank you for enrolling, {self.first_name}.\nYou are now a member!")    
    
    def spend_points(self, amount_spent):
        print(f"\n====== SPENDING HISTORY ======")
        if not self.is_rewards_member:
            print("This function cannot be performed at this time ㅠ_ㅠ.\nEnroll today to spend your gold card points!")
        else:
            if amount_spent > self.gold_card_points:
                print(f"Payment Failed. You have insufficent gold card points.\nRemaining: {self.gold_card_points}pts.")
            else:
                self.gold_card_points -= amount_spent
                print(f"Thank you, {self.first_name}. You've spent {amount_spent}pts.\nRemaining: {self.gold_card_points}pts.")
    

# * TESTING GROUND
user1 = User("Jane", "Doe", "jd@mail.com", 47)
user1.display_info()
user1.enroll()

jsmith = User("John", "Smith", "js@dojo.com", 32)
a_love = User("Ada", "Lovelace", "al@dojo.com", 24)

user1.spend_points(50)
jsmith.enroll()
jsmith.spend_points(80)

user1.display_info()
jsmith.display_info()

user1.enroll()
user1.spend_points(50)
user1.spend_points(150)
jsmith.spend_points(80)
jsmith.spend_points(121)
a_love.spend_points(40)
