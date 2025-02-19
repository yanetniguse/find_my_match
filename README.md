# Assignment 3
## Assignment:Developing a Rule-Based Matchmaking System for a Dating Application(In your groups)
## Instructions

### Part 1: System Overview & Design
1. Explain the purpose of a `rule-based` matchmaking system.
2. Define the `attributes` that will be used for matchmaking (e.g., age, location, interests, gender preference).
3. Describe the `scoring rules` for compatibility (e.g., shared interests = +10 points, same city = +5 points, age gap > 10 years = -5 points).
4. Define the `data structure` to store user profiles (e.g., dictionaries, lists, or classes in Python).

### Part 2: Implementation
1. `Create a Profile Management System:`
- Implement a system to add, remove, and retrieve user profiles.
- Each profile should include attributes such as:
  - Name
  - Age
  - Gender
  - Interests (list of hobbies)
  - Location
2. `Develop a Matching Algorithm:`
- Implement a function to compare two profiles based on predefined rules.
- Assign compatibility scores using weighted attributes:
  - `Age difference:` Normalize and assign a score.
  - `Shared interests:` Calculate a similarity score (e.g., Jaccard Index).
  - `Location:` Exact match gets a higher score.
3. `Find Best Matches:`
- Implement a function that takes a user ID and finds the `top 3 best matches` based on compatibility scores.
- Sort matches in `descending order of compatibility.`

### Part 3: Testing & Evaluation
1. `Create at least 5 user profiles` and store them in the system.
2. `Run the matchmaking function` for one of the profiles and display the top matches with scores.
3. `Analyze the output` and explain why certain users were matched.
`Deliverables:`
- Code Implementation: A Python script or Jupyter Notebook with the matchmaking system.
- Report (2-3 pages):
  - System overview and design explanation.
  - Description of rules and scoring logic.
  - Screenshots or outputs of matchmaking results.
  - Reflection on limitations and possible improvements.
`If possible:`
- Implement `gender preferences` in matchmaking.
- Add a `GUI or web interface` for user interaction.
- Allow users to `customize weightings` for different attributes.

## Contributors
- [James Otieno - `jayotieno`]
- [Yanet Niguse - `yanetniguse`]
- [Dhruv Pokhariyal - `P0lcahontas`]
- [Kwame Lucheveli - `luche3002`]