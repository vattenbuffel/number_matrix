import jsonpickle

def export_json(matrix, name):
    with open(name, 'w') as f:
        f.write(jsonpickle.encode(matrix))

def load_json(name):
    with open(name) as f:
        str_ = f.read()
    return jsonpickle.decode(str_)