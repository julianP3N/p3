""" 

H:\djangoProyectos\p2>python manage.py runserver
jango-admin startproject Proyecto1

python manage.py migrate

 python manage.py runserver """


#from pipes import Template
from django.template import Template, Context
from django.http import HttpResponse
import datetime

def metodo1 (request):  
    return HttpResponse("Alumnos OK 1")



def metodo2 (request):  #Vista 1  (V1.html)    
   #  plantilla_juan=open("H:/djangoProyectos/p2/p2/plantillas/plantillas1.html")
    juanPLT=open("H:\djangoProyectos\p2\p2\plantillas\plantillas1.html", encoding="utf-8")
    juan=Template(juanPLT.read())
    juanPLT.close()
    ctx=Context()
    juan1=juan.render(ctx)

    return HttpResponse(juan1)




def metodo3 (request):
    from datetime import datetime

# current date and time
    now1 = datetime.now()
    f= datetime.timestamp(now1)
    a2= "punto 2 con"
    a3= "punto 2 con"

    a1="""<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title> Blockchain  </title>
  </head>
  <body style="background-color:#F2F3F4;">
    <p>&nbsp;</p>
<h3 style="text-align: center; color: #3f7320;"><span style="border-bottom: 4px solid #c82828;"></span> <h1 style="text-align:center;">Blockchain</h1> <img src="https://s03.s3c.es/imag/_v0/770x420/b/a/7/Blockchain.jpg" ">
<p><strong>  ¿Qué es y para qué sirve la tecnología blockchain? </strong></p>

<table class="demoTable" style="height: 54px;">
<thead>
<tr>
<td><span style="color: #c82828;"><b>¿qué es y para qué sirve? <b></span></td>
<td><span style="color: #c82828;"><b>Sector financiero está aprovechando tecnología blockchain? <b></span></td>
</tr>
</thead>
<tbody>
<tr>
<h1>%s  Se traduce como cadena de bloques.
</h1>


>es de un conjunto de tecnologías que permiten llevar un registro seguro, descentralizado, sincronizado y distribuido de las operaciones digitales, sin necesidad de la intermediación de terceros.
En ese sentido, la definición más completa es la dada por Don & Alex Tapscott en su libro Blockchain Revolution: “un libro de contabilidad digital incorruptible de transacciones económicas que se puede programar para registrar no solo transacciones financieras, sino prácticamente todo lo que tiene valor».
<h1>%s Básicamente,
</h1>
Cada uno de los bloques de datos se encuentra protegido y vinculado entre sí, permitiendo la participación de determinados usuarios (cada uno, asociado a un bloque). Así, la transacción no la verifica un tercero, sino la red de nodos (computadores conectados a la red), que también es la que autoriza en consenso cualquier actualización en la Blockchain.
Para ejemplificar, se puede pensar que la empresa A quiere enviar dinero a la empresa B. Al hacerlo con blockchain, la transacción se representa como un bloque de datos, que se transmite a cada una de las partes que componen la red.
 <h1>
 %s blockchain

 </h1
Esos últimos deben aprobar la validez de la operación. El dinero se mueve y el bloque quedará añadido a la cadena, generando así el registro inmutable y transparente.
Por ende, la tecnología blockchain cumple la función de registrar, conservar y proteger la información de cualquier tipo de operación digital, sin intervención de terceros. En otras palabras, opera como una base de datos compartida y continuamente actualizada, lo que facilita el intercambio de activos y la gestión de contratos inteligentes, entre otras opciones.
En la práctica, puede usarse en un sin número de industrias en tareas que van más allá del intercambio de dinero, como el registro contable, la trazabilidad de productos en la cadena de suministro, la gestión de historias clínicas y de identidad, planes de fidelización, contratos y resolución de controversia.</td>
<td>El sector financiero ha mostrado gran interés en la exploración del mundo del blockchain, no solo por la irrupción de criptomonedas, sino por las ventajas que supone la posibilidad de llevar un sistema de registros (incluidos los contables) sin la intervención de terceros.
De hecho, este sector (finanzas) representa más del 60 del mercado global de blockchain, lo que se explica -en gran medida- por la enorme transformación digital de la industria, siempre innovando para incrementar la seguridad de las operaciones y mejorar la experiencia de los clientes.
En cuanto a usos específicos del blockchain en el sector financiero, algunos ejemplos son:
• Ofertas Iniciales de Monedas (ICO, por sus siglas en inglés), una forma de financiamiento en la que las empresas ofrecen tokens virtuales en lugar de acciones.
• Contratos inteligentes (smart contracts), programas que permiten a dos partes celebrar un contrato sin la mediación de terceros.
• Pagos internacionales. Gracias a la criptomoneda XRP -conocida como Rippe, o la criptomoneda de los bancos- es posible realizar pagos entre diversos países, evitando que las transacciones deban pasar por un intermediario.
Tanto el blockchain como el seguro de Crédito son herramientas clave para que las empresas reduzcan riesgos y agilicen sus operaciones. Puedes conocer más sobre el seguro de crédito en Solunion.</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Revisa <a target="_blank" rel="nofollow noopener" href="http://localhost:8000/inicio/">Django</a> Pagina creada desde cero.</p>
</body>
</html>""" %(f, a2, a3)
    return HttpResponse(a1)




def metodo4 (request):
    from datetime import datetime

# current date and time
    nombre="julian en metodo4"
    now1 = datetime.now()
    f= datetime.now()
    j= "holas J pasaste por aca"
    a1="Medellin"
    d1 = "Antioquia"

    estudiante=("Juan" , "cadavid")
   # nombre="juan"
    apellido="cadavid"

    #ya=datetime.datetime.now()
    p1=Per("Nombre","apelli")

   
    docExterno=open("H:\djangoProyectos\p2\p2\plantillas\V1.html", encoding="utf8")
   # docExterno=open("H:\djangoProyectos\p2\p2\plantillas\plantillas1.html", encoding="utf8")
    a2=Template(docExterno.read())
    docExterno.close()
    con=Context({"nombre_variable":apellido, "Ciudad":d1, "TiempoLinux": f, "SelfClaseMetodo": p1.nombre})
    a3=a2.render(con)
    return HttpResponse(a3)

class Per(object):
    
    def _init_(self, nombre, apellido):
        
        self.nombre=nombre
        
        self.apellido=apellido
    

    

    
