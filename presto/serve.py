from flask import jsonify, request, abort
from tango.app import Tango


app = Tango(__name__)


@app.route('/api/posts/')
def posts():
    stash = app.connector.get('presto', '/posts/')
    source = request.args.get('source', None)
    if source:
        stash['posts'] = [
            entry for entry in stash['posts']
            if entry['source'] == source
        ]
    return jsonify(stash)


@app.route('/api/posts/<int:post_id>/')
def post(post_id):
    stash = app.connector.get('presto', '/posts/')
    for entry in stash['posts']:
        if entry['id'] == post_id:
            return jsonify({'post': entry})
    abort(404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
