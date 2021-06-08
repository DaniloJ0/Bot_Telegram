from matplotlib.figure import Figure
import networkx as nx
import matplotlib.pyplot as plt
from math import sqrt
import random as rd
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, update

def ImprimirStepsPolinomio(query):
    query.message.reply_text("1. Escriba el comando //poli y a lado coloque los parametros de la siguiente forma a,b,c todos separados con coma (,).\n"
    +"2. Ejemplo: //poli 1,-6,9\n"
    +"3. Para este ejercicio tomamos en cuenta que los coeficientes hacen parte de un polinomio de grado 2, por lo que solo perimitirá 3 valores.")

def ImprimirStepsGraph(query):
    query.message.reply_text("1. Escriba el comando //grafo y a lado coloque los parametros de la siguiente forma V(vértices), E(aristas), K(grado) separados por coma. \n"
    +"2. Ejemplo: //grafo 6,10,4 \n"
    +"3. El algoritmo valida que con los parametros dados se pueda crear el grafo,"
    +" de igual forma trate de colocar parametros validos")

def StepsFibonacci(query):
    query.message.reply_text("1. Escriba el comando //fibo y a lado la secuencia de números separados con espacio.\n"
    +"2. Coloque un punto y coma para digitar el comienzo del patron.\n"
    +"3. Ejemplo: //fibo 2 3 4 5 7 11 13 18 22 29; 1 \n"
    +"- En este caso el algoritmo empezará a buscar desde el número 2")

def ImprimirAyuda(query):
    query.message.reply_text("                 Bienvenido al centro de ayuda            \n"
    +"Para iniciar el bot existen dos maneras, mediente el comando /start o /menu en ambos se le desplegará las opciones de los items pedidos en el proyecto, al darle clic a alguno se le mostrarán automanticamente las instrucciones para el buen funcionamiento del Bot. \n\n"
    +"Los comando disponibles son: \n\n"
    +"1. /start \n"
    +"2. /menu \n"
    +"3. /fibo \n"
    +"4. /grafo \n"
    +"5. /poli \n"
    +"6. /grupo \n"
    +"7. /ayuda \n\n")

def ImprimirAyuda2(update,context):
    update.message.reply_text("                 Bienvenido al centro de ayuda            \n"
    +"Para iniciar el bot existen dos maneras, mediente el comando /start o /menu en ambos se le desplegará las opciones de los items pedidos en el proyecto, al darle clic a alguno se le mostrarán automanticamente las instrucciones para el buen funcionamiento del Bot. \n\n"
    +"Los comando disponibles son: \n\n"
    +"1. /start \n"
    +"2. /menu \n"
    +"3. /fibo \n"
    +"4. /grafo \n"
    +"5. /poli \n"
    +"6. /grupo \n"
    +"7. /ayuda \n\n")

def PatronFibonacci (secuencia,vertice):
    secuencia = [int(x) for x in secuencia]
    secuencia.sort()
    i = vertice
    lista = [secuencia[vertice], secuencia[vertice+1]]
    while i < len(secuencia):
        suma = lista[-2]+lista[-1]
        if suma in secuencia:
            lista.append(suma)
        i += 1
    return lista

def ImprimirIntegrantes(update,context):
    update.message.reply_text("Los integrantes del grupos son: \n"+"1. Danilo Jiménez (Lider) \U0001F9D1\n"+"2. Yassary Garcia \U0001F469 \n"
    +"3. Sergio Muñoz\U0001F9D1")
    
def Polinomio(update,context):
    text = update.message.text
    text = text.replace("/poli", "").strip()
    try:
        polin=eval(text)
        if len(polin)==3:
            a=int(polin[0])
            b=int(polin[1])
            c=int(polin[2])
            cap=HallarPolinomio(a,b,c)
            update.message.reply_text("La solución es:\n")
            try:
                if len(cap)==2:
                    update.message.reply_text(f"f(n)=  c_0*{cap}^n +c_1*n* {cap[0]}^2 + c_1* {cap[1]}^n")
            except:
                    update.message.reply_text(f"f(n)=  c_0*n* {cap}^n + c_1* {cap}^n")
        else:
            update.message.reply_text("Debe ingresar únicamente tres parámetros.")
    except Exception as e:
        print(e)
        update.message.reply_text("Por favor, digite los parámetros nuevamente.")

def HallarPolinomio(a,b,c):
    determinante = (b**2)- (4*a*c)
    if determinante > 0:
        x_1 = (-b + sqrt((b**2)- (4*a*c))) / (2*a)
        x_2 = (-b - sqrt((b ** 2) - (4 * a * c))) / (2*a)
        return x_1,x_2
    elif determinante == 0:
        x_1= -b / (2*a)
        return x_1
    else:
        return "No tiene raices"

def Menu(update, context):
    opciones = [[InlineKeyboardButton("1. Polinomio caracteristico", callback_data="op1")],
                [InlineKeyboardButton("2. Patron con Fibonacci \U0001F522", callback_data="op2")],
                [InlineKeyboardButton("3.      Grafo      \U0001F578", callback_data="op3")],
                [InlineKeyboardButton("4.      Ayuda      \U00002753", callback_data="op4")]]
    reply_markup = InlineKeyboardMarkup(opciones)
    name = update.message.chat["first_name"]
    text = f"¡Hola, {name} \U0001F44B! Aquí tienes un menú de las opciones"
    update.message.reply_text(text, reply_markup=reply_markup)

def menu(update, context):
    query = update.callback_query
    query.answer()
    answer = query.data
    if answer == "op1":
        ImprimirStepsPolinomio(query)
    elif answer == "op2":
        StepsFibonacci(query)
    elif answer == "op3":
        ImprimirStepsGraph(query)
    elif answer == "op4":
        ImprimirAyuda(query)

def grafo(update, context):
    text = update.message.text
    text = text.replace("/grafo", "").strip()
    update.message.reply_text("loading...")
    try:
        graph = eval(text)
        if len(graph) == 3:
            vertices = int(graph[0])
            aristas = int(graph[1])
            grado = int(graph[2])
            if 2*aristas>vertices*grado:
                try:
                    s="t"-5
                except:
                    update.message.reply_text("El grafo no se puede completar debido a que los valores de V o K no lo permiten")
            else:            
                DibujarGrafo(vertices,aristas,grado)
                img = open("src/images/grafo.png", "rb")
                chat_id = update.message.chat_id
                update.message.bot.sendPhoto(chat_id=chat_id, photo=img)
                update.message.reply_text("\U0001F511 Tener en cuenta \U0000203C : La librería Networkx con la cual nos facilita trabajar con grafos, "
                +"tiene cierto incoveniente al dibujar el grafo; al parecer solo sucede cuando intenta colocar una arista entre"
                +" dos nodos que están muy alejados y hay uno entre ellos, lo que hace es agregarle una arista demás a x vértice o también sobrescribe una arista."+" Cabe recalcar que solo pasa en algunos casos.\n"
                +" El algoritmo que realizamos si realiza todo correctamente \U0001f680")
        else:
            update.message.reply_text("Debe ingresar únicamente tres parámetros.")
    except Exception as e:
        update.message.reply_text("Por favor, digite los parámetros nuevamente.")

def GenerarGrafo(v, m, k):
    y=0
    i=1
    lista3=[0]*v  #Inicializo la lista con 0 para así ir contando las ocurrencias
    lista=[]
    while y<m:
        j=1
        s=k
        lista2=[]
        while(j<=k and y<m and j<=s):
            s=k-lista3[i-1] # este me dice los vertices que ya han sido vinculado previamente
            while(True):
                x=rd.randint(1,v)
                if x!=i and x not in lista2 and x not in [y for y in range(1,i)]: #En este compruebo que no haya aristas ciclicas y que el número que salga no este vinculado a una arista ya tiniendo su grado mayor
                    break
            lista.append((i,x))
            lista2.append(x)
            lista3[x-1]=lista3[x-1]+1 #lista que contiene las ocurrecias de los vertices
            j+=1
            y+=1
        i+=1
    return lista

def DibujarGrafo(v, m, k):
    G = nx.Graph()
    G.add_edges_from(GenerarGrafo(v, m, k))
    nx.draw_networkx(G)
    plt.savefig("src/images/grafo.png")
    plt.figure()
