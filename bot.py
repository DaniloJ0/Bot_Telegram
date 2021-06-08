#recursivefunction_bot  --- Rfunction_bot
#Token: 1858178635:AAECvUvncL5F5J0GMip2kYtua2mC5cv6OB0
from typing import Text
from telegram import update
from telegram.ext import Updater,CommandHandler,CallbackQueryHandler
import funciones as fn

def start(update,context):
    update.message.reply_text(fn.Menu(update,context))
    
def FindPattern(update,context):
    text=update.message.text.replace("/fibo","")
    try:
        index=text.index(";")
    except:
        update.message.reply_text("¡Ingrese el vertice separado por un ';' ! Intentelo de nuevo.")    
    vertice=int(text[index+1:].strip())-1
    text=text[0:index].split()
    update.message.reply_text("El patron que coincide con la seria de Fibonacci es: \n")
    update.message.reply_text(fn.PatronFibonacci(text,vertice))

if __name__== '__main__':
    updater=Updater(token="YOUR_TOKEN",use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('menu', start)) 
    dp.add_handler(CommandHandler("fibo", FindPattern))         
    dp.add_handler(CommandHandler("grafo", fn.grafo))    
    dp.add_handler(CommandHandler("ayuda", fn.ImprimirAyuda2))
    dp.add_handler(CommandHandler("grupo",fn.ImprimirIntegrantes))
    dp.add_handler(CommandHandler("poli", fn.Polinomio))    
    dp.add_handler(CallbackQueryHandler(fn.menu, pattern="op1"))
    dp.add_handler(CallbackQueryHandler(fn.menu, pattern="op2"))
    dp.add_handler(CallbackQueryHandler(fn.menu, pattern="op3"))
    dp.add_handler(CallbackQueryHandler(fn.menu, pattern="op4"))
    updater.start_polling()
    updater.idle()
