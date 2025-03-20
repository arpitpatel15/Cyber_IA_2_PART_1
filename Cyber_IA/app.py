from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def home():
    """ Renders a to-do list web page. """
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append(task)
    return render_template('todo.html', tasks=tasks)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """ API endpoint to return tasks in JSON format. """
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)