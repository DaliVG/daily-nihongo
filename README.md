Daily Nihongo - Práctica Diaria de Kanji
===========================================

Este proyecto envía un mensaje de texto diario con un kanji aleatorio y una práctica de escritura en japonés. Utiliza Twilio para enviar los mensajes y la API de Kanji para obtener información sobre los kanjis.

Características
--------------
- Obtiene un kanji aleatorio de la API `KanjiAPI <https://kanjiapi.dev/>`_.
- Genera una fecha y hora aleatoria.
- Envía un mensaje SMS usando Twilio con los detalles del kanji en un sandbox.
- Motiva al usuario a practicar la escritura en hiragana.

Requisitos
----------
Antes de ejecutar este proyecto, asegúrate de tener lo siguiente:

- Python 3.x instalado.
- Una cuenta de Twilio con un número de teléfono habilitado para SMS.
- Un archivo ``.env`` con las siguientes variables de entorno:

.. code-block:: ini

   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_FROM_NUMBER=your_twilio_number
   TWILIO_TO_NUMBER=your_recipient_number

Instalación
------------
1. Clona este repositorio::

   git clone https://github.com/tuusuario/daily-nihongo.git
   cd daily-nihongo

2. Crea un entorno virtual y actívalo::

   python -m venv env
   source env/bin/activate  # En Mac/Linux
   env\Scripts\activate     # En Windows

3. Instala las dependencias::

   pip install -r requirements.txt

4. Crea un archivo ``.env`` y agrega tus credenciales de Twilio y OpenAI.

Uso
---
Ejecuta el script para enviar un mensaje::

   python daily_nihongo.py

Explicación del Código
------------------------

- ``get_random_time()``: Genera una hora aleatoria en formato HH:MM:SS.
- ``get_random_date()``: Genera una fecha aleatoria entre 1990 y 2023.
- ``get_random_kanji()``: Obtiene un kanji aleatorio de la API de Kanji.
- ``send_message()``: Construye y envía un mensaje SMS con la práctica diaria.

Dependencias
------------

- ``twilio``: Para el envío de mensajes SMS.
- ``requests``: Para obtener información de la API de Kanji.
- ``python-dotenv``: Para manejar variables de entorno.
- ``random`` y ``datetime``: Para generar valores aleatorios de fecha y hora.

Instala estas dependencias con::

   pip install twilio requests python-dotenv

Notas
-----
- Asegúrate de que tu cuenta de Twilio tiene saldo suficiente para enviar mensajes.
- Puedes modificar la API de kanji para obtener un grado de kanji diferente.

