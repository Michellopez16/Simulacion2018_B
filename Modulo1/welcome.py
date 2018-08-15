# programa de bienvenida.
# Created by Lázaro Alonso.
from time import sleep
def print_words(sentence):
    for word in sentence.split():
        for l in word:
            sleep(.05)
            print(l, end = '')
        print(end = ' ')
sentence1 = 'Hola, bienvenida o bienvenido a simulación matemática.'
print_words(sentence1)
sentence2 = 'Me puedes llamar Alice y me gustaría saber un poco acerca de ti, por ejemplo'
print_words(sentence2)
sentence3 = '¿Cuál es tu nombre?'
print_words(sentence3)
prompt = ' >> '
nombre_usuario = input(prompt)
sentence4 = 'Gusto en conocerte ' + nombre_usuario + ', espero que te guste el curso.'
print_words(sentence4)
sentence5 = 'Ahora, me gustaría saber donde vives %s, ¿cuál es tu ciudad?' % nombre_usuario
print_words(sentence5)
lugar = input(prompt)
sentence6 = 'Mmm... ¿eso es una ciudad real? %s.' % lugar
print_words(sentence6)
sentence7 = 'Bueno, después lo investigo. ¿Qué edad tienes?'
print_words(sentence7)
edad = input(prompt)
sentence8 = '¿Te ha gustado esta bienvenida?'
print_words(sentence8)
gustar = input(prompt)
sfinal = ' Muy bien %s, dices que %s te gustó la bienvenida.' % (nombre_usuario, gustar)
sfinal2 = ' Tú vives en %s, ya dije que voy a investigar donde es eso.'% lugar
sfinal3 = 'Y además estas por cumplir %s años. Fue un gusto conocerte, hasta pronto!' %  (int(edad)+ 1 )
print_words(sfinal)
print_words(sfinal2)
print_words(sfinal3)
sentence9 = 'Enunciado de prueba. '
