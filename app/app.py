from flask import Flask
from flask_restplus import Resource, Api

import math

app = Flask(__name__)
api = Api(app)


@api.route('/distance/<string:coord>')
# https://www.kompf.de/gps/distcalc.html
class CalcDistance(Resource):
    def post(self, coord):
        result = coord.split(',')
        distance = 0.0
        if len(result) == 4:
            try:
                lat1 = float(result[0])
                lon1 = float(result[1])
                lat2 = float(result[2])
                lon2 = float(result[3])

                dx = 111.3 * math.cos((lat1 + lat2) / 2 * 0.01745) * (lon1 - lon2)
                dy = 111.3 * (lat1 - lat2)
                distance = math.sqrt(dx * dx + dy * dy)
            except ValueError:
                distance = "Value Error"
        return {'distance': distance}


if __name__ == '__main__':
    app.run()
