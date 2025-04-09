# models.py

class KnowledgeBase:
    def __init__(self):
        self.profiles = {}
        self.next_id = 1

    def add_profile(self, profile_data):
        profile_id = self.next_id
        self.profiles[profile_id] = {'id': profile_id, **profile_data}
        self.next_id += 1
        return profile_id

    def get_profile(self, profile_id):
        return self.profiles.get(profile_id)

    def get_all_profiles(self):
        return list(self.profiles.values())

class Matchmaker:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.weights = {
            'age': 0.2, 'faith': 0.15, 'values': 0.15, 'education': 0.1,
            'bmi': 0.1, 'relationship_goals': 0.1, 'hobbies': 0.075, 'places': 0.075
        }
        self.max_age_diff = 20

    def calculate_bmi(self, weight, height):
        return round(weight / ((height / 100) ** 2), 2)

    def calculate_compatibility(self, profile_a, profile_b):
        age_diff = abs(profile_a['age'] - profile_b['age'])
        age_score = max(0, 1 - (age_diff / self.max_age_diff)) * self.weights['age']
        faith_importance = (5 - abs(profile_a['faith_importance'] - profile_b['faith_importance'])) / 5
        faith_match = 1 if profile_a['faith'] == profile_b['faith'] else 0
        faith_score = (faith_importance * 0.7 + faith_match * 0.3) * self.weights['faith']
        values_score = self.weights['values'] if profile_a['values'] == profile_b['values'] else 0
        education_score = self.weights['education'] if profile_a['education'] == profile_b['education'] else 0
        bmi_a = self.calculate_bmi(profile_a['weight'], profile_a['height'])
        bmi_b = self.calculate_bmi(profile_b['weight'], profile_b['height'])
        bmi_diff = abs(bmi_a - bmi_b) / max(bmi_a, bmi_b)
        bmi_score = (1 - bmi_diff) * self.weights['bmi']
        goals_score = self.weights['relationship_goals'] if profile_a['relationship_goals'] == profile_b['relationship_goals'] else 0
        hobbies_a = set(profile_a['hobbies'])
        hobbies_b = set(profile_b['hobbies'])
        hobbies_jaccard = len(hobbies_a & hobbies_b) / len(hobbies_a | hobbies_b) if hobbies_a | hobbies_b else 0
        hobbies_score = hobbies_jaccard * self.weights['hobbies']
        places_a = set(profile_a['places'])
        places_b = set(profile_b['places'])
        places_jaccard = len(places_a & places_b) / len(places_a | places_b) if places_a | places_b else 0
        places_score = places_jaccard * self.weights['places']
        return round(
            age_score + faith_score + values_score + education_score +
            bmi_score + goals_score + hobbies_score + places_score, 2
        )
