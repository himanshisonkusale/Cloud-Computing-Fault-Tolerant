# **********************
# *
# * Program Name: MP1. Membership Protocol.
# * File: submit.py (Python 3)
# * Purpose: Submission script for Coursera MP2 assignment
# *
# ***********************

import urllib.request
import urllib.error
import json
import subprocess
import os


class NullDevice:
    def write(self, s):
        pass


def submit():
    print('==\n== [sandbox] Submitting Solutions \n==')

    (login, password) = loginPrompt()
    if not login:
        print('!! Submission Cancelled')
        return

    # Try running part 0 first to generate dbg.0.log
    try:
        subprocess.run(['sh', 'run.sh', '0'], check=True)
    except FileNotFoundError:
        print('!! Error: run.sh not found. Make sure it exists and is executable.')
        return
    except subprocess.CalledProcessError:
        print('!! Error running run.sh script.')
        return

    submissions = [source(i) for i in range(4)]
    submitSolution(login, password, submissions)


# =========================== LOGIN HELPERS ===========================

def loginPrompt():
    login = input('Login (Email address): ')
    password = input("One-time Password (from the assignment page. This is NOT your own account's password): ")
    return login, password


def partPrompt():
    print('Hello! These are the assignment parts that you can submit:')
    for idx, name in enumerate(partFriendlyNames):
        print(f"{idx + 1}) {name}")
    partIdx = int(input(f"Please enter which part you want to submit (1-{len(partFriendlyNames)}): ")) - 1
    return (partIdx, partIds[partIdx])


def submit_url():
    return "https://www.coursera.org/api/onDemandProgrammingScriptSubmissions.v1"


def submitSolution(email_address, password, submissions):
    values = {
        "assignmentKey": akey,
        "submitterEmail": email_address,
        "secret": password,
        "parts": {
            partIds[0]: {"output": submissions[0]},
            partIds[1]: {"output": submissions[1]},
            partIds[2]: {"output": submissions[2]},
            partIds[3]: {"output": submissions[3]},
        }
    }

    url = submit_url()
    data = json.dumps(values).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    req.add_header('Content-Type', 'application/json')
    req.add_header('Cache-Control', 'no-cache')

    try:
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode('utf-8')
            print('== Submission response ==')
            print(response_data)
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")


def source(partIdx):
    try:
        with open(f"dbg.{partIdx}.log", 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Warning: dbg.{partIdx}.log not found.")
        return ""


def cleanup():
    for i in range(4):
        try:
            os.remove(f"dbg.{i}.log")
        except:
            pass


# Assignment identifiers
akey = 'Lm64BvbLEeWEJw5JS44kjw'
partIds = ['PH3Q7', 'PIXym', 'mUKdC', 'peNB6']
partFriendlyNames = ['Create Test', 'Delete Test', 'Read Test', 'Update Test']

# Entry point
if __name__ == "__main__":
    submit()
    cleanup()
