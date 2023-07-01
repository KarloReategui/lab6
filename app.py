from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)
@app.route("/signup/", methods=["GET", "POST"])
def index():
    #Consumir la API y obtener los usuarios
    if request.method == 'POST':
        name = request.form['name']
        next = request.args.get('next', None)
    url = 'https://pokeapi.co/api/v2/pokemon'
    nombre = name
    new_url = "{}/{}".format(url, nombre)
    args={nombre:nombre} if nombre else {}
    response = requests.get(new_url,params=args)
    tipis=[]
    movimi=[]
    if response.status_code == 200:
            lista=response.json()
            results = lista.get('types',[])
            result2 = lista.get('sprites',[])
            results3 = lista.get('moves',[])
            print('TIPOS: ')
            if results:
                for i in results:
                    name = i['type']
                    nombree=name.get('name')
                    tipis.append(nombree)
                    print(nombree)
            print('MOVIMIENTOS: ')
            if results:
                for i in results3:
                    name = i['move']
                    movis=name.get('name')
                    movimi.append(movis)
                    print(movis)

            sprite1 = result2.get('back_default')
            sprite2 = result2.get('front_default')
            sprite3 = result2.get('front_shiny')
            sprite4 = result2.get('back_shiny')

            response = requests.get(sprite1)

            file = open("images/sample1.png", "wb")
            file.write(response.content)
            file.close()

            response2 = requests.get(sprite2)

            file = open("images/sample2.png", "wb")
            file.write(response2.content)
            file.close()

            response3 = requests.get(sprite3)

            file = open("images/sample3.png", "wb")
            file.write(response3.content)
            file.close()

            response4 = requests.get(sprite4)

            file = open("images/sample4.png", "wb")
            file.write(response4.content)
            file.close()

            print('SPRITES DESCARGADOS CORRECTAMENTE')


    return render_template('codepokehtml.html',nombre=nombre, movimi = movimi, tipis = tipis, response = sprite1,response2 = sprite2,response3 = sprite3,response4 = sprite4)
########################################################
@app.route("/", methods=["GET", "POST"])
def show_signup_form():
    return render_template("index.html")
    


########################################################
if __name__ == '__main__':
    app.run(debug=True)