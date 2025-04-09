from flask import Flask, render_template, request, redirect, url_for
from models import KnowledgeBase, Matchmaker

# Initialize Flask app and dependencies
app = Flask(__name__)

kb = KnowledgeBase()# KnowledgeBase instance to store user profiles
matchmaker = Matchmaker(kb)  # Matchmaker instance to calculate compatibility

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get input from the form
        user1_profile = {
            'age': int(request.form['age1']),
            'faith_importance': int(request.form['faith_importance1']),
            'faith': request.form['faith1'],
            'values': request.form['values1'],
            'education': request.form['education1'],
            'height': int(request.form['height1']),
            'weight': int(request.form['weight1']),
            'relationship_goals': request.form['relationship_goals1'],
            'hobbies': request.form['hobbies1'].split(','),
            'places': request.form['places1'].split(',')
        }
        user2_profile = {
            'age': int(request.form['age2']),
            'faith_importance': int(request.form['faith_importance2']),
            'faith': request.form['faith2'],
            'values': request.form['values2'],
            'education': request.form['education2'],
            'height': int(request.form['height2']),
            'weight': int(request.form['weight2']),
            'relationship_goals': request.form['relationship_goals2'],
            'hobbies': request.form['hobbies2'].split(','),
            'places': request.form['places2'].split(',')
        }

        # Add profiles to the knowledge base
        user1_id = kb.add_profile(user1_profile)
        user2_id = kb.add_profile(user2_profile)

        # Calculate compatibility score
        match_score = matchmaker.calculate_compatibility(user1_profile, user2_profile)

        # Return the results
        return render_template("results.html", match_score=match_score)

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
