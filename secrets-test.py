#!/usr/bin/env python3
import json
import sys

secret_request = json.load(sys.stdin)
secret_response = {}
secrets = { "API": "", "secret2": "secret2_val" }

for secret in secret_request["secrets"]:
    if secret in secrets.keys():
      secret_response[secret] = dict({"value": str(secrets[secret]), "error": None})
    else:
      secret_response[secret] = dict({"value": None, "error": "Unable to retrieve secret."})

sys.stdin.close()

print(json.dumps(secret_response))