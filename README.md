# GymMember Class – Object-Oriented Gym Membership Manager 🏋️‍♂️

This Python class `GymMember` is designed to model a gym membership system using object-oriented programming principles like encapsulation, class vs instance variables, and data hiding.

## 🧠 Features

- **Auto-generated Member ID:** Each new member gets a unique ID, assigned automatically.
- **Validated Membership Tiers:** Only allows valid membership types: `"Basic"`, `"Plus"`, or `"Elite"`.
- **Gym Capacity Limit:** Prevents adding new members once the maximum capacity (default: 100) is reached.
- **Full Name Update Limit:** A member can only change their name up to **4 times**.
- **Check-In System:** Tracks how many times a member checks into the gym.
- **Commitment Badges:** Earned every 10 check-ins; check-in count resets after each badge.
- **Encapsulation:** All internal variables are private and accessed only via methods.
- **Class Stats:** Track total members and maximum gym capacity using class methods.

---

## 🛠️ How to Use

```python
# Create a new member
member1 = GymMember("Alice Johnson", "Plus")

# Get member info
print(member1.get_member_id())        # e.g., 1
print(member1.get_full_name())        # "Alice Johnson"

# Update name (max 4 times)
member1.update_full_name("Alice J.")  # True

# Update tier
member1.update_membership_tier("Elite")  # True

# Simulate check-ins
for _ in range(10):
    member1.check_in()

# Get commitment badges
print(member1.get_commitment_badges())  # 1

# Get gym stats
print(GymMember.get_total_members())    # e.g., 1
print(GymMember.get_max_capacity())     # 100
