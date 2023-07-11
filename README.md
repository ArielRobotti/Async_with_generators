# Async_with_generators
##Concurrencia basada en generadores de Python
Un generador es una función especial que puede pausar su ejecución y luego reanudarla desde donde se detuvo. Esto se logra mediante el uso de la palabra clave "yield". Cuando un generador encuentra una cláusula "yield", devuelve un valor y pausa su ejecución hasta que se le solicite continuar. Esto permite que otras partes del código tengan la oportunidad de ejecutarse antes de que el generador se reanude.

En el código proporcionado, la función asyncCount se define como un generador. Recibe dos parámetros: start, que indica el valor inicial para la cuenta regresiva, y _t, que representa el tiempo de espera entre cada cuenta. Antes de comenzar la cuenta regresiva, se realizan algunas validaciones para garantizar que los parámetros sean válidos.

Dentro del generador, se utiliza un bucle for para iterar en orden descendente desde el valor inicial hasta 1. En cada iteración, se imprime el valor actual del contador. A continuación, se establece un tiempo de referencia t0 utilizando la función time.time(). Luego, se entra en un bucle while que compara continuamente el tiempo actual con t0 + _t para determinar si ha transcurrido el tiempo de espera.

Aquí es donde entra en juego la característica clave de los generadores. En lugar de bloquear la ejecución en el bucle while, el generador utiliza la cláusula yield para ceder el control de ejecución. Al llegar al yield, la ejecución se pausa y se devuelve el control al código que llamó al generador. Esto permite que otras tareas se ejecuten mientras se espera que pase el tiempo de espera.

Después de la pausa, el generador se reanuda desde donde se detuvo en la iteración anterior y continúa con la siguiente iteración del bucle for. Este proceso se repite hasta que se completa la cuenta regresiva y se alcanza el valor 0.

El código principal crea dos generadores utilizando la función asyncCount con diferentes parámetros. Estos generadores se almacenan en una lista llamada tareas (tareas en español). Luego, se inicia un bucle while que se ejecuta mientras haya tareas pendientes en la lista.

En cada iteración del bucle, se extrae la última tarea de la lista utilizando tareas.pop() y se intenta ejecutarla utilizando la función next(current). Si la tarea tiene un yield pendiente, se pausa y se pasa el control a otras tareas. Luego, se vuelve a colocar la tarea al inicio de la lista para que tenga la oportunidad de ejecutarse en la próxima iteración.

Si una tarea ha completado su cuenta regresiva y no tiene más yield pendientes, se captura la excepción StopIteration y se pasa a la siguiente tarea sin volver a incluirla en la lista.

En resumen, este enfoque de implementar la cuenta regresiva como generadores pausables y utilizando el control de ejecución con yield tiene varias ventajas. Permite que el programa se ejecute de manera asíncrona y concurrente, ya que otras tareas pueden ejecutarse mientras se espera que pase el tiempo de espera. Esto mejora la eficiencia y el rendimiento general del programa, ya que no se bloquea en esperas innecesarias.

Además, al utilizar generadores, el código es más legible y modular. Cada generador representa una tarea específica y se puede reutilizar en otros contextos si es necesario. También es más fácil de mantener y depurar, ya que el flujo de ejecución es más claro y controlable.
