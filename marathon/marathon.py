import dcos.marathon


def callMarathon():
    client = dcos.marathon.create_client()

    apps = client.get_apps()

    for key, value in apps:
        print("key: "+key)
        print("value: "+value)