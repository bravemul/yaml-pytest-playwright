import yaml

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

print(config["name"])        # MyApp
print(config["server"]["port"])  # 8080
print(config["features"])    # ['login', 'register']
