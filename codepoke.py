from flask import Flask, render_template
import requests
url = 'https://pokeapi.co/api/v2/pokemon'
nombre=input('Nombre del pokemon: ').lower()
new_url = "{}/{}".format(url, nombre)
def get_pokemons(url=new_url,name=nombre):
        args={name:nombre} if name else {}
        

        response = requests.get(url,params=args)
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
                    print(nombree)
            print('MOVIMIENTOS: ')
            if results:
                for i in results3:
                    name = i['move']
                    movis=name.get('name')
                    print(movis)

            sprite1 = result2.get('back_default')
            sprite2 = result2.get('front_default')
            sprite3 = result2.get('front_shiny')
            sprite4 = result2.get('back_shiny')

            response = requests.get(sprite1)

            file = open("templates/sample_image1.png", "wb")
            file.write(response.content)
            file.close()

            response2 = requests.get(sprite2)

            file = open("templates/sample_image2.png", "wb")
            file.write(response2.content)
            file.close()

            response3 = requests.get(sprite3)

            file = open("templates/sample_image3.png", "wb")
            file.write(response3.content)
            file.close()

            response4 = requests.get(sprite4)

            file = open("templates/sample_image4.png", "wb")
            file.write(response4.content)
            file.close()

            print('SPRITES DESCARGADOS CORRECTAMENTE')

            otra=input('Quieres buscar otra vez?: S/N ')
            if otra == 's':
                url = 'https://pokeapi.co/api/v2/pokemon'
                nombre2=input('Nombre del pokemon: ').lower()
                new_url2 = "{}/{}".format(url, nombre2)
                get_pokemons(new_url2)
                    
url='https://pokeapi.co/api/v2/pokemon'
get_pokemons()