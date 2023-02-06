from flask import Flask, request, send_file, make_response
import json

app = Flask(__name__)

def unredact(log_file, json_file):
    with open(json_file) as f:
        mapping = json.load(f)
    with open(log_file) as f:
        logs = f.readlines()
    unredacted_logs = []
    for log in logs:
        for key, value in mapping.items():
            log = log.replace(key, value)
        unredacted_logs.append(log)
    return unredacted_logs

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        log_file = request.files.get("log_file")
        json_file = request.files.get("json_file")
        log_file.save("log.txt")
        json_file.save("mapping.json")
        logs = unredact("log.txt", "mapping.json")
        response = make_response(''.join(logs))
        response.headers["Content-Disposition"] = "attachment; filename=unredacted_logs.txt"
        return response
    return '''
        <form method="post" enctype="multipart/form-data">
            Log File: <input type="file" name="log_file"><br>
            JSON File: <input type="file" name="json_file"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
