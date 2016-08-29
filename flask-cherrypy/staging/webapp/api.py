from flask import Flask, jsonify, abort

svc = Flask(__name__)

things = [
    {
        'id': 1,
        'description': u'First',
        'size': 2.0,
        'color': 'Red',
        'flag': True
    },
    {
        'id': 2,
        'description': u'Middle',
        'size': 0.001,
        'color': 'Blue',
        'flag': False
    },
    {
        'id': 3,
        'description': u'Last',
        'size': 3.14152,
        'color': 'Green',
        'flag': True
    },
]

@svc.route('/things', methods=['GET'])
def get_things():
    return jsonify({'things': things})


@svc.route('/thing/<int:thing_id>', methods=['GET'])
def get_thing(thing_id):
    thing = [thing for thing in things if thing['id'] == thing_id]
    if len(thing) == 0:
        abort(404)
    return jsonify({'thing': thing[0]})


if __name__ == '__main__':
    svc.run(debug=True)
