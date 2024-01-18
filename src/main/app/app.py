from flask import Flask, render_template, Markup, request, jsonify

import os
import pandas as pd
import folium
from folium.plugins import MarkerCluster # for clustering the markers
import joblib

app = Flask(__name__)

model = joblib.load('./data/model.pkl')

def predict(form):
    lat = form.get('latitude')
    long = form.get('longitude')
    borough = form.get("borough")
    c1 = form.get("c1").lower()
    c2 = form.get("c2").lower()
    c3 = form.get("c3").lower()
    c4 = form.get("c4").lower()
    price = form.get("price")
    if price == '$':
        price = '1'
    elif price == '$$':
        price = '2'
    elif price == '$$$':
        price = '3'
    elif price == '$$$$':
        price = '4'
    xtest = {
        'latitude': lat,
        'longitude': long,
        'borough': borough, 
        'category1': c1, 
        'category2': c2, 
        'category3': c3, 
        'category4': c4, 
        'price': price }
    x_test = pd.DataFrame(data=xtest, index=[0])
    # predict = model.predict(x_test)
    accuracy = model.predict_proba(x_test)
    percentage = accuracy[0][1] * 100
    percentage = round(percentage, 2)
    return f'{percentage}% Chance of Being Successful'

@app.route('/')
def home():
    return render_template('index.html', prediction='')

@app.route('/predict', methods=['POST'])
def response():
    form = request.form
    prediction = predict(form)
    return render_template('index.html', prediction=prediction)


@app.route('/map')
def map():
    map = folium.Map(location=[40.693943, -73.985880], default_zoom_start=12, min_zoom=10)
    path = os.path.join(app.root_path, 'data.pickle')
    df = pd.read_pickle(path)
    df = df.drop_duplicates(subset='id', keep="last")
    marker_cluster = MarkerCluster().add_to(map)  # create marker clusters
    for i in range(df.shape[0]):
        row = df.iloc[i]
        if row['coordinates']['latitude'] and row['coordinates']['longitude']:
            tooltip = "Name: {}<br> Address: {}<br> Rating: {} <br> Click for more".format(row["name"],
                                                                                           row["location"]["address1"],
                                                                                           row["rating"])
            location = [row['coordinates']['latitude'], row['coordinates']['longitude']]
            folium.Marker(location, popup=row["price"], tooltip=tooltip).add_to(marker_cluster)
    return map._repr_html_()


if __name__ == '__main__':
    # app.run(debug=True)
    joblib.load('./data/model.pkl')
    app.run("0.0.0.0", port=80, debug=False)