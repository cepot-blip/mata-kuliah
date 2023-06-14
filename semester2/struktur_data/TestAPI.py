from flask import Flask, jsonify, request

app = Flask(__name__)

obats = [
    {"id": 1, "title": "Obat A", "pembuat": "Pembuat A"},
    {"id": 2, "title": "Obat B", "pembuat": "Pembuat B"},
    {"id": 3, "title": "Obat C", "pembuat": "Pembuat C"}
]
next_id = 4

# Endpoint untuk mendapatkan semua obat


@app.route('/obats', methods=['GET'])
def get_obats():
    return jsonify(obats)

# Endpoint untuk mendapatkan obat berdasarkan ID


@app.route('/obats/<int:id>', methods=['GET'])
def get_obat(id):
    for obat in obats:
        if obat['id'] == id:
            return jsonify(obat)
    return jsonify({"message": "Obat tidak ditemukan"}), 404

# Endpoint untuk menambahkan obat baru


@app.route('/obats', methods=['POST'])
def add_obat():
    global next_id
    title = request.json['title']
    pembuat = request.json['pembuat']
    obat = {"id": next_id, "title": title, "pembuat": pembuat}
    obats.append(obat)
    next_id += 1
    return jsonify({"message": "Obat berhasil ditambahkan", "obat": obat}), 201

# Endpoint untuk mengubah obat berdasarkan ID


@app.route('/obats/<int:id>', methods=['PUT'])
def update_obat(id):
    for obat in obats:
        if obat['id'] == id:
            obat['title'] = request.json['title']
            obat['pembuat'] = request.json['pembuat']
            return jsonify({"message": "Obat berhasil diupdate", "obat": obat})
    return jsonify({"message": "Obat tidak ditemukan"}), 404

# Endpoint untuk menghapus obat berdasarkan ID


@app.route('/obats/<int:id>', methods=['DELETE'])
def delete_obat(id):
    for obat in obats:
        if obat['id'] == id:
            obats.remove(obat)
            return jsonify({"message": "Obat berhasil dihapus"})
    return jsonify({"message": "Obat tidak ditemukan"}), 404


if __name__ == '__main__':
    app.run(debug=True)
