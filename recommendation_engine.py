import json

def load_agents_db():
    with open('agents_db.json', 'r') as file:
        return json.load(file)

def recommend_agents(task_description):
    agents = load_agents_db()
    recommendations = []

    for agent in agents:
        score = 0
        for capability in agent['capabilities']:
            if capability.lower() in task_description.lower():
                score += 1

        recommendations.append({
            'name': agent['name'],
            'score': score,
            'strengths': agent['strengths']
        })

    recommendations = sorted(recommendations, key=lambda x: x['score'], reverse=True)[:3]
    return recommendations
