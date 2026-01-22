from flask import Flask, jsonify
import subprocess
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "logs/firewall_audit.log"
MITIGATION_SCRIPT = "services/mitigation.ps1"


@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "KNS API ONLINE"}), 200


@app.route("/mitigate", methods=["POST"])
def mitigate():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        subprocess.run(
            ["powershell", "-ExecutionPolicy", "Bypass", "-File", MITIGATION_SCRIPT],
            check=True
        )

        with open(LOG_FILE, "a") as log:
            log.write(f"[{timestamp}] ARP triggered via API – Firewall rules applied\n")

        return jsonify({"result": "ARP executed successfully"}), 200

    except Exception as e:
        with open(LOG_FILE, "a") as log:
            log.write(f"[{timestamp}] ERROR: {str(e)}\n")

        return jsonify({"error": "ARP execution failed"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
