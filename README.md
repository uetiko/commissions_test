Modulo de creacción de comisiones.
==================================

El modulo de comision consta de de mantener la reservación (orden de compra) unificado, con ello 
podremos tener con este objecto, la referencia directa del evento, el usuario del evento, el 
metodo de pago, los boletos, etc.

Para las comisiones se deberan tener tres tablas de comision, donde se podran ligar los metodos de
pago, los usuarios y los eventos en especifico a una determinada comisión.

![comisiones db](https://raw.githubusercontent.com/uetiko/commissions_test/master/comisiones.png)

Gracias a que order ahora podra tener esta información, podra hacer el calculo basado a que el evento
tenga una comision de cualquier de los siguientes tipos, dado a que dara prioridad a el evento, después
al usuario y si no, al metodo de pago.

Aunque el diagrama lo puede explicar mejor

![diagrama de clases](https://raw.githubusercontent.com/uetiko/commissions_test/dd9f70a11288aea452746136799410fe8622a80e/diagrama_clases.svg)


Este consepto de paquete, supone que uno debe crear las tablas, y configurar previamente, así que cuando se 
crea el objecto de roder, este podrá ir en busqueda de las tablas de comisiones que ayudaran a saber cual objecto de
comision generar y en base a eso, calcular la comision y el gran total.

Las clases que contendran esta información son CommissionUser, CommissionEven y CommissionPayment, que se usaran para
el metodo de commission_calculation de la case Order. Sin mencionar que la mayoria sin Beans o entities diseñados para el apoyo
a este modelo, como la Clase Ticket, que es solo la representación abstracta de los tickets, o Address, un entitie generico para apoyo
a las direcciones de compra o pago, o de direccion de usuarios, eventos u otros apoyos. O Payment que debería o debera ser el entitie del metodo de
pago elegido para el pago del evento, suponiendo que un evento tenga mas de un metodo de pago disponible.

Al final, el uso de esto se limita a Order y su correcto llenado para poder pasar esta orden al proceso de pago y creación de la factura.
