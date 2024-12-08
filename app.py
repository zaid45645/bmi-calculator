from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    bmi = None  
    if request.method == "POST":
        try:
            weight = float(request.form.get("weight"))
            height = float(request.form.get("height"))
            if height > 0:
                new_height = height * height
                bmi_val = weight / new_height
                if bmi_val <= 18.5:
                    bmi = "You are considered underweight and possibly malnourished"
                elif bmi_val > 18.5 and bmi_val <= 24.9:
                    bmi = "You are within a healthy weight range for young and middle-aged adults"
                elif bmi_val >= 25.0 and bmi_val <= 29.9:
                    bmi = "You are considered overweight"
                elif bmi_val >= 30:
                    bmi = "You are considered obese."
            else:
                bmi = "Height must be greater than zero."
        except ValueError:
            bmi = "Please enter valid numeric values for weight and height."

    return render_template("index.html", bmi=bmi)

if __name__ == "__main__":
    app.run(debug=True)
