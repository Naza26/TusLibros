# Bitacora de progreso

Naturalmente me surgió empezar el desarrollo desde el dominio, la capa más profunda. Decidí arrancar por acá porque en el contexto de hacer muchas cosas sobre las cuales no se tanto o no tengo el contexto necesario, lo más conocido resultaba pensar los aspectos funcionales del programa como objetitos separados.
Después los puedo relacionar, pero de esa manera empiezo a familiarizarme con el negocio en cuestión sobre el que estoy trabajando y lo que tiene más "jugo" explorar.

Una vez desarollado el dominio me encontre con dificultades en la interfaz, lo que conectaría el frontend y el backend. Siguiendo lo que vi en clase sobre pensar en una capa interna y otra externa, empece desarollando lo que espera recibir y devolver la interfaz acorde a los requerimientos del sistema.
Algo curioso que me sucedió es que desarollando la interfaz me sentí obligada a hacer cambios en el dominio, porque había resultado muy trivial y la implementación no me había servido mucho (aunque esto ya lo sabía de antemano).

La capa interna nunca podría devolver un objeto de dominio, porque no existe tal con confianza con la interfaz ni tampoco quiero tenerla. Quiero devolver cosas que representen que tengo esos objetos ó si los tengo bien o no, pero no el objeto per sé.

¿Como diferencio la cara interna de la cara externa? (En términos de responsabilidades)

Yo entiendo la interna como lo que entra hacia mi sistema (dominio) y la externa como lo que sale de mi sistema. Si esto fuera correcto, yo estando parada desde la capa interna, como le digo a la capa externa que la operación o lo que se haya querido hacer fue exitoso o no? ¿Qué se supone que tengo que devolver? Porque al prinicpio yo creía que la especificación de los requerimientos en el READ.ME de la consigna me decían lo que tenía que devolver esos endpoints, pero ahora no me queda claro si esos valores los tendría que devolver la capa interna o externa. Por ejemplo, en el caso de /createCart no me queda claro si en caso de exito tendríamos que devolver un id desde la capa interna o desde la externa. Si el id tiene que ser devuelto en la capa externa, como devuelvo desde la interna que todo salió bien? ¿Cuál sería la responsabilidad de la capa externa?
