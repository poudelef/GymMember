class GymMember:
    __id = 1  # Increases when a new member is created
    __valid_tiers = {"Basic", "Plus", "Elite"}
    __total_members = 0
    __max_capacity = 100  # We have a small gym

    def __init__(self, full_name, membership_tier):
        if membership_tier not in GymMember.__valid_tiers:
            raise ValueError("Invalid member tier! Please enter a correct tier.")

        if GymMember.__total_members >= GymMember.__max_capacity:
            raise Exception("House full")

        self.__member_id = GymMember.__id
        GymMember.__id += 1
        GymMember.__total_members += 1

        self.__full_name = full_name
        self.__name_change_count = 0
        self.__membership_tier = membership_tier
        self.__check_in_count = 0
        self.__commitment_badges = 0

    # Instance Methods

    def get_member_id(self):
        return self.__member_id

    def get_full_name(self):
        return self.__full_name

    def update_full_name(self, new_name):
        if self.__name_change_count >= 4:
            raise Exception("You already changed your name 4 times")
        self.__full_name = new_name
        self.__name_change_count += 1
        return True

    def update_membership_tier(self, new_tier):
        if new_tier not in GymMember.__valid_tiers:
            raise ValueError("There is no such tier.")
        self.__membership_tier = new_tier
        return True

    def check_in(self):
        self.__check_in_count += 1
        if self.__check_in_count == 10:
            self.__commitment_badges += 1
            self.__check_in_count = 0

    def get_commitment_badges(self):
        return self.__commitment_badges

    # Class Methods

    @classmethod
    def get_total_members(cls):
        return cls.__total_members

    @classmethod
    def get_max_capacity(cls):
        return cls.__max_capacity
