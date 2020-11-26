import os
import connexion

def hello(name: str) -> str:
    return f'Hello {name}'

if __name__ == '__main__':
  app = connexion.FlaskApp(__name__, port=int(os.environ.get('PORT', 8080)), specification_dir='swagger/')
  app.add_api('hello.yml')
  app.run()

