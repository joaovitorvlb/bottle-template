from bottle import Bottle, run, response

app = Bottle()

@app.route('/', method='GET')
def get_data():
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'Example City'
    }
    response.content_type = 'application/json'
    return data

if __name__ == '__main__':
    run(app, host='localhost', port=8000)
