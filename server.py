from openstack.openstack import getToken
from openstack.Nova import Nova
import os
from os import environ as env

from dotenv import load_dotenv
from flask import Flask, json, request
from flask_cors import CORS


load_dotenv()

app = Flask(__name__)
CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})

novaVersion = str(env["OS_NOVA_API_VERSION"])
authUrl = f'{env["OS_AUTH_URL"]}'
novaUrl = f'{env["OS_NOVA_API_URL"]}{novaVersion}/'
projectId = f'{env["OS_TENANT_ID"]}'
app.secret_key = projectId


@app.route("/login", methods=["POST"])
def login():
    global novaUrl, authUrl, projectId
    body = request.get_json()
    username = body["username"]
    password = body["password"]
    try:
        [token, tokenAge] = getToken(username, password, projectId, authUrl)
        if len(token) > 0:
            return json.dumps({
                "success": True,
                "token": token,
                "expires": tokenAge
            })
        return json.dumps({
            "success": False,
        })
    except Exception as e:
        print(e.args)
        return json.dumps({
            "success": False,
            "message": " ".join([*e.args])
        })


@app.route("/servers", methods=["POST"])
def createServer():
    global novaUrl, authUrl, projectId
    try:
        if not "X-Auth-Token" in request.headers.keys():
            return json.dumps({
                "success": False,
                "message": "Auth token required"
            })
        token = request.headers["X-Auth-Token"]
        body = request.get_json()
        name = body["name"]
        flavor = body["flavor"]
        keypair = body["keypair"]
        networks = body["networks"] if "networks" in body.keys() else []
        image = body["image"]
        nova = Nova(projectId)
        server = nova.createServer(
            token, name, keypair, networks, flavor, image)
        return json.dumps({
            "success": True,
            "data": server
        })
    except Exception as e:
        print(e.args)
        return json.dumps({
            "success": False,
            "message": " ".join([*e.args])
        })


@app.route("/keypairs", methods=["POST"])
def createKeyPair():
    global novaUrl, authUrl, projectId

    try:
        if not "X-Auth-Token" in request.headers.keys():
            return json.dumps({
                "success": False,
                "message": "Auth token required"
            })
        token = request.headers["X-Auth-Token"]
        body = request.get_json()
        name = body["name"]
        nova = Nova(projectId)
        keypair = nova.createKeypair(token, name)
        return json.dumps({
            "success": True,
            "data": keypair
        })
    except Exception as e:
        print(e.args)
        return json.dumps({
            "success": False,
            "message": " ".join([*e.args])
        })


@app.route("/servers", methods=["GET"])
def listServers():
    global novaUrl, authUrl, projectId
    nova = Nova(projectId)
    try:
        if not "X-Auth-Token" in request.headers.keys():
            return json.dumps({
                "success": False,
                "message": "Auth token required"
            })
        token = request.headers["X-Auth-Token"]
        detailed = request.args["detailed"]if "detailed" in request.args.keys(
        ) else "false"
        servers = nova.getServerList(token, detailed)
        return json.dumps({
            "success": True,
            "data": servers
        })
    except Exception as e:
        print(e.args)
        return json.dumps({
            "success": False,
            "message": " ".join([*e.args])
        })


@app.route("/flavors", methods=["GET"])
def listFlavors():
    global novaUrl, authUrl, projectId
    nova = Nova(projectId)
    try:
        if not "X-Auth-Token" in request.headers.keys():
            return json.dumps({
                "success": False,
                "message": "Auth token required"
            })
        token = request.headers["X-Auth-Token"]
        detailed = request.args["detailed"]if "detailed" in request.args.keys(
        ) else "false"
        flavors = nova.getFlavorList(token, detailed)
        return json.dumps({
            "success": True,
            "data": flavors
        })
    except Exception as e:
        print(e.args)
        return json.dumps({
            "success": False,
            "message": " ".join([*e.args])
        })


@app.route("/keypairs", methods=["GET"])
def listKeypairs():
    global novaUrl, authUrl, projectId
    nova = Nova(projectId)
    try:
        if not "X-Auth-Token" in request.headers.keys():
            return json.dumps({
                "success": False,
                "message": "Auth token required"
            })
        token = request.headers["X-Auth-Token"]
        keypairs = nova.getKeypairsList(token)
        return json.dumps({
            "success": True,
            "data": keypairs
        })
    except Exception as e:
        print(e.args)
        return json.dumps({
            "success": False,
            "message": " ".join([*e.args])
        })


@app.route("/networks", methods=["GET"])
def listNetList():
    global novaUrl, authUrl, projectId
    nova = Nova(projectId)
    try:
        if not "X-Auth-Token" in request.headers.keys():
            return json.dumps({
                "success": False,
                "message": "Auth token required"
            })
        token = request.headers["X-Auth-Token"]
        nets = nova.getNetworkList(token)
        return json.dumps({
            "success": True,
            "data": nets
        })
    except Exception as e:
        print(e.args)
        return json.dumps({
            "success": False,
            "message": " ".join([*e.args])
        })


@app.route("/images", methods=["GET"])
def listImagesList():
    global novaUrl, authUrl, projectId
    nova = Nova(projectId)
    try:
        if not "X-Auth-Token" in request.headers.keys():
            return json.dumps({
                "success": False,
                "message": "Auth token required"
            })
        token = request.headers["X-Auth-Token"]
        imgs = nova.getImageList(token)
        return json.dumps({
            "success": True,
            "data": imgs
        })
    except Exception as e:
        print(e.args)
        return json.dumps({
            "success": False,
            "message": " ".join([*e.args])
        })


if __name__ == "__main__":
    os.system("clear ||cls")
    app.run(host="0.0.0.0", debug=True)
