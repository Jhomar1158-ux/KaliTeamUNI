# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
import requests
from ask_sdk_model import Response
import csv
import os
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email():
    smtp_server = "smtp.gmail.com"
    my_sender_email = 'jhomarcristianelias@gmail.com' 
    password = '########'
    destino_email = "jhomar.astuyauri@ieee.org"

    Subject = "Cita - Jhomar Astuyauri - Emergencia"
    mensaje = "Hola estimado doctor, tengo los siguientes sintomas me gustaría recibir su atención."
    message = MIMEMultipart("alternative")
    message["Subject"] = Subject
    message["From"] = my_sender_email
    message["To"] = destino_email

    part1 = MIMEText(mensaje, "plain")
    message.attach(part1)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(my_sender_email, password)
        server.sendmail(
            my_sender_email, destino_email, message.as_string()
        )


def get_data_covid():
    data_covid = {}
    path_excel = '/tmp/CASOS_25012021.csv'
    url = 'https://podcast-henry.s3.amazonaws.com/CASOS_25012021.csv'
    #os.remove(path_excel)
    file = requests.get(url).content

    with open(path_excel, 'wb') as f:
        f.write(file)

    with open(path_excel, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            pais = row[0]
            if pais == 'Pais':
                continue
            depa = row[1]
            pcr = row[2]
            prueba_quick = row[3]
            prueba_antigeno = row[4]
            total_casos = row[5]
            fallecidos = row[6]
            letalidad = row[7]
            try:
                letalidad = round(float(letalidad.replace('"', '')), 2)
            except:
                letalidad = ""
            print(data_covid)
            data_covid[depa.replace('"', '')] = {
                'PCR': pcr.replace('"', ''),
                'PRUEBA RAPIDA': prueba_quick.replace('"', ''),
                'PRUEBA ANTIGENO': prueba_antigeno.replace('"', ''),
                'TOTAL CASOS': total_casos.replace('"', ''),
                'CASOS TOTALES': total_casos.replace('"', ''),
                'FALLECIDOS': fallecidos.replace('"', ''),
                'LETALIDAD': letalidad
            }

    return data_covid


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hola, soy kali vinco, para los amigos kali y para la familia vinco. ¿Cómo puedo ayudarte? ¿Qué necesitas saber?. En mi cerebro tengo información muy actualizada sobe el COVID-19."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class InfoCovidIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("InfoCovidIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = """Según la OMS, para evitar la propagación de la COVID-19:
Lávate las manos con frecuencia. Usa agua y jabón o un desinfectante de manos a base de alcohol.
Mantén una distancia de seguridad con personas que tosan o estornuden.
No te toques los ojos, la nariz ni la boca.
Si no te encuentras bien, quédate en casa.
En caso de que tengas fiebre, tos o dificultad para respirar, no dudes en pedirme que me contacte con tu doctor."""

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("¿Hay algo más en lo que pueda ayudarte?")
                .response
        )

class EstadisticasdIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("EstadisticasIntent")(handler_input)

    def handle(self, handler_input):
        data_covid = get_data_covid()
        # type: (HandlerInput) -> Response
        param_detect = ask_utils.request_util.get_slot(handler_input, "param_detect")
        param_detect = param_detect.value.upper()
        departamento = ask_utils.request_util.get_slot(handler_input, "departamento")
        departamento = departamento.value.upper()

        filter2 = data_covid.get(departamento, {}).get(param_detect, '')
        speak_output = "En " + departamento + " hay " + str(filter2) +" "+ str(param_detect) 

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class NotificarEmailIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NotificarEmailIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speak_output = "Le envie una notificación a tu doctor"
        send_email()
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(EstadisticasdIntentHandler())
sb.add_request_handler(NotificarEmailIntentHandler())
sb.add_request_handler(InfoCovidIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
