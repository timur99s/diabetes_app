from flask import Flask , render_template, request
from flask.wrappers import Request
import diagnose


app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def hello():
    if request.method == "POST":
        input_Age = request.form["age"]
        input_Polyuria = request.form["polyuria"]
        input_polydipsia = request.form["polydipsia"]
        input_weight_loss = request.form["weight_loss"]
        input_weakness = request.form["weakness"]
        input_Polyphagia = request.form["Polyphagia"]
        input_genital_thrush = request.form["genital_thrush"]
        input_visual_blur = request.form["visual_blur"]
        input_itching = request.form["itching"]
        input_irritability = request.form["irritability"]
        input_healing = request.form["healing"]
        input_paresis = request.form["paresis"]
        input_muscle_stiff = request.form["muscle_stiff"]
        input_alopecia = request.form["alopecia"]
        input_obesity = request.form["obesity"]
        input_gender = request.form["gender"]
        input_Note = request.form["notes"]

        sugar_diag = diagnose.log_reg(input_Age, input_Polyuria, input_polydipsia, input_weight_loss, 
input_weakness, input_Polyphagia, input_genital_thrush, input_visual_blur, 
input_itching, input_irritability, input_healing, input_paresis, 
input_muscle_stiff, input_alopecia, input_obesity, input_gender)
       
        
        if sugar_diag == 1:
            print('HIGH chance of diabetes')
        else:
            print('LOW chance of diabetes')

        return render_template("index.html", sugar_result = sugar_diag, userNote = input_Note)

    return render_template("index.html")
