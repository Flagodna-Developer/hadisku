from flask import Flask, request, Response
import os

app = Flask(__name__)
DATA_DIR = "data"  # Keep this as "data"


@app.route("/<path:filepath>", methods=["GET"])
def handle_file(filepath):
    full_path = os.path.join(DATA_DIR, filepath)
    full_path = os.path.normpath(full_path)

    print(f"DEBUG - Full Path: {full_path}")

    if not os.path.abspath(full_path).startswith(os.path.abspath(DATA_DIR) + os.sep):
        return "Invalid path", 400

    if os.path.isfile(full_path):
        try:
            with open(full_path, "rb") as f:
                data = f.read()
                return Response(data, mimetype="application/octet-stream")
        except Exception as e:
            return str(e), 500

    return "Not found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
