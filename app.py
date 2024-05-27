from flask import Flask,render_template, request

app = Flask(__name__)


#Flask'taki URl yapıları

@app.route("/")             #response
def index():
    message = "Bu bir mesajdır..."
    numbers = [1,2,3,4,5,6,7,8,9]
    
    return render_template("index.html", number  = 10 ,number2 = 20, message = message, numbers = numbers)

@app.route("/search")
def search():
    return "Search page"

@app.route("/delete/item")
def delete():
    return "Delete itemm"

@app.route("/delete/<string:id>")  #dinamik url  
def deleteId(id):
    return "Id: " + id

@app.route("/toplam", methods = ["GET", "POST"])
def toplam():
    if request.method == "POST":
        number1= request.form.get("number1")
        number2 = request.form.get("number2")
        return render_template("number.html", total = int(number1) + int(number2))
    else:
        return render_template("number.html")

if __name__ == "__main__":  # bu dosya direk terminalden mi çalıştırılmış diye kontrol ediyoruz
    app.run(debug = True)   #local host taki web sunucumuzu çalıştırma, Debug = true yaptığımız için otomatik yeniliyor