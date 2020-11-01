from flask import Flask ,render_template
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

class H(Resource):
    def get(self):
        return {"data" : "Test"}
        # return render_template("Covid.html")

api.add_resource(H, "/covid_test")
if __name__ == "__main__":
    app.run(debug=True)