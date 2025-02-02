import os
# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from backend.utils.config import ProductionConfig, TestingConfig, DevelopmentConfig
from backend.controller.controller import user_controller, user_expenditure_controller, product_controller, \
    store_controller
from backend.model.model import db



app = Flask(__name__)

# Load configuration based on the environment
if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object(ProductionConfig)
elif os.getenv('FLASK_ENV') == 'testing':
    app.config.from_object(TestingConfig)
else:
    app.config.from_object(DevelopmentConfig)

db.init_app(app)

# Register blueprints
app.register_blueprint(user_controller)
app.register_blueprint(user_expenditure_controller)
app.register_blueprint(product_controller)
app.register_blueprint(store_controller)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

    # text = extract_text_from_images(['backend/files/abc.jpg'])
    # api_key = os.getenv("OPENAI_API_KEY")
    # print(structured_output(text, api_key))

