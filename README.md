# Bitacora de progreso

Naturalmente me surgió empezar el desarrollo desde el dominio, la capa más profunda. Decidí arrancar por acá porque en el contexto de hacer muchas cosas sobre las cuales no se tanto o no tengo el contexto necesario, lo más conocido resultaba pensar los aspectos funcionales del programa como objetitos separados.
Después los puedo relacionar, pero de esa manera empiezo a familiarizarme con el negocio en cuestión sobre el que estoy trabajando y lo que tiene más "jugo" explorar.

Una vez desarollado el dominio me encontre con dificultades en la interfaz, lo que conectaría el frontend y el backend. Siguiendo lo que vi en clase sobre pensar en una capa interna y otra externa, empece desarollando lo que espera recibir y devolver la interfaz acorde a los requerimientos del sistema.
Algo curioso que me sucedió es que desarollando la interfaz me sentí obligada a hacer cambios en el dominio, porque había resultado muy trivial y la implementación no me había servido mucho (aunque esto ya lo sabía de antemano).

La capa interna nunca podría devolver un objeto de dominio, porque no existe tal con confianza con la interfaz ni tampoco quiero tenerla. Quiero devolver cosas que representen que tengo esos objetos ó si los tengo bien o no, pero no el objeto per sé.

¿Como diferencio la cara interna de la cara externa? (En términos de responsabilidades)

Yo entiendo la interna como lo que entra hacia mi sistema (dominio) y la externa como lo que sale de mi sistema. Si esto fuera correcto, yo estando parada desde la capa interna, como le digo a la capa externa que la operación o lo que se haya querido hacer fue exitoso o no? ¿Qué se supone que tengo que devolver? Porque al prinicpio yo creía que la especificación de los requerimientos en el READ.ME de la consigna me decían lo que tenía que devolver esos endpoints, pero ahora no me queda claro si esos valores los tendría que devolver la capa interna o externa. Por ejemplo, en el caso de /createCart no me queda claro si en caso de exito tendríamos que devolver un id desde la capa interna o desde la externa. Si el id tiene que ser devuelto en la capa externa, como devuelvo desde la interna que todo salió bien? ¿Cuál sería la responsabilidad de la capa externa?

¿Esta bien que el carrito decida que libros se ofrecen (_books_in_stock)?  Quien deberia tener esa responsabilidad?
  RTA: Nop, creo que está mal eso que hice, pero tuve que hacerlo para poder preguntar si el libro que se quiere agregar al carrito está en el catalogo o no. Quizás hay otra forma de relacionar esas entidades y no lo estoy viendo.
 No esta necesariamente mal que el carrito conozca un catalogo. Depende bien lo que estas representando con ese carrito? Es solo un contenedor de libros? o es algo mas represeenta algo que podes poner dentro solo libros de la editorial? Si es solo un contenedor de libros, ¿vale la pena modelarlo con una clase propia? ¿qué diferencia tiene con  una coleccion en ese caso?
  RTA: El carrito es una entidad que me permite guardar libros para poder comprarlos luego, según el negocio, solo puedo guardar libros que tiene la editorial, proque esta es la editorial FIUBA. Asi que yo creería que tiene sentido que sea un objeto y no un diccionario.
El concepto de catalogo esta muy bien!  ¿Qué opinas de los mensajes y las responsabilidades que te quedaron en los objetos catalogo?
  RTA: Me gusta! Por ahora hace poquito pero porque siento que me falta descubrir algunas cosas más sobre el dominio, pero el catalogo sabe que libros tiene, sabe responder si un libro esta o no en su listado, y me puede dar libros, no sé si hará algo más a futuro. Creí necesario tener que crear este objeto porque no la editorial quien tendría que saber hacer estas cosas.
Lo del EditorialSystem pinta que es una buena intuicion, tiene sentido. Por ahora en la captura no le veo muchas responsabilidades, asi que quizas te falte asignarle alguna responsabilidad o quizas no tenga sentido que creemos una nueva clase para ello, ¿no?
  RTA: Por ahora el sistema de editorial conoce un carrito asociado y un catalogo de libros (con sus respectivo stock). Quizás más adelante maneje el pago, este sistema es más como un contenedor de todo lo que hace funcional a la editorial, lo pensé como un objeto que se compone de distintos objetitos y te da el sistema mayor.

Esta bien que el carrito conozca a un catalogo, pero no esta bien que él lo cree.  ¿Cómo resolvemos eso?

Y con respecto al resto de tus respuestas te diria que recuerdes la heuristica de "que solo vale la pena crear una nueva si es que tiene responsabilidades asociadas". Si solo responde colaboradores (editorial), o tiene un protocolo similar al de una coleccion (catalogo)   te quedan clases anemicas. Y en muchos casos es mejor representar esas entidades con otros objetos.

  RTA: En primer lugar, me ordena el conocimiento que tengo sobre el negocio. El carrito y el catalogo no existen por fuera de la editorial de fiuba. Si yo creo un objeto que los agrupe le estoy dando un marco a la existencia de ese carrito y ese catalogo.
Por otro lado, creo que aunque es verdad que no tiene mucho comportamiento la clase, es un punto de partida. Es un por ahora, va ir ganando más contexto a medida que yo sepa más.
No creo que valga la pena tener un diccionario o alguna estructura de datos primitiva porque estoy refiriendome al sistema de la editorial escondiendo el nombre, para eso mejor que tenga nombre.
Además, siento que sigue con el modelo 1:1 de la realidad. Una editorial que me da cosas, no hago diccionario["catalogo"]

Un poco de contexto y lo que sabemos sobre HTTP:

Surge la necesidad de usar requests y responses de HTTP. A priori uno pensaría que necesitamos usar algo que nos provea una biblioteca. No vamos a usarlo porque por ahora nuestros objetos son simples y no queremos acoplarnos a eso de inmediato. Me parece interesante charlarlo después para ver si hubiera que escalar el programa tuvieramos la necesidad de usar algo algún paquete. En caso de necesitarlo, como podemos resolver el problema sin acoplarnos a una dependencia externa.

La request y la response HTTP tiene normalmente un header y un body.
El body tendría un diccionario clave-valor como lo dice el enunciado. Siempre vamos a manejar strings. Los requests son de distinto tipo (metodo HTTP). Depende la acción que hago tendría que usar un método HTTP u otro.
La response además de estas mismas cosas, tiene un status code para indicar como terminó esa petición.

El server lo corro como: python3 web_server.py


Un Web Server consta de un cliente y un servidor que se pueden mandar mensajes entre sí. Estos mensajes se conocen como peticiones y respuestas (request/response) y pueden ocurrir a través de cualquier protocolo (HTTP, HTTPS, SOAP). Los protocolos definen cómo se envíaran esos mensajes entre cliente y servidor (sintaxis, formato, etc).

REST API es un API específico para Web Servers que usa un estilo de arquitectura REST basado en el protocolo HTTP. 
Esto inlcuye:

- Metodos HTTP (GET, POST, DELETE, PUT)
- URLs especificas (/surveys, /surveys/123)
- Respuesta del servidor en formato JSON ({survey_id: "123", "score": 9, ...})





