class Instructor:
    def __init__(self):
        self.__instructor_name = ""
        self.__technology_skill = []
        self.__experience = None
        self.__avg_feedback = None

    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name

    def set_technology_skill(self, technology_skill):
        self.__technology_skill = technology_skill

    def set_experience(self, experience):
        self.__experience = experience

    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback

    def get_instructor_name(self):
        return self.__instructor_name

    def get_technology_skills(self):
        return self.__technology_skills

    def get_experience(self):
        return self.__experience

    def get_avg_feedback(self):
        return self.__avg_feedback

    def check_eligibility(self):
        if self.__experience > 3 and self.__avg_feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__avg_feedback >= 4:
            return True
        else:
            return False

    def allocate_course(self, technology):

        if technology in self.__technology_skill and self.check_eligibility():
            return True
        else:
            return False


obj = Instructor()
list1 = ["a", "b", "c", "d", "e", "f"]
obj.set_instructor_name("Tony")
obj.set_technology_skill(list1)
obj.set_experience(4)
obj.set_avg_feedback(3)
if obj.allocate_course("b"):
    print("Allocated")
else:
    print("Not Allocated")
