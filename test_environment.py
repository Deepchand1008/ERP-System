from core.application import Environment

env = Environment.load()

print(env.APP_NAME)
print(env.APP_ENV)
print(env.APP_DEBUG)
print(env.APP_VERSION)