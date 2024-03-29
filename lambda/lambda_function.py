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

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome, I am Voicer. An Alexa skills app for Koforidua Technical University?"

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

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

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

#########################################################################################
#########################################################################################
################################### CUSTOM INTENT HANDLERS ##############################
#########################################################################################
#########################################################################################

class AboutVoicerIntentHandler(AbstractRequestHandler):
    """Handler for About Voicer Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AboutVoicerIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        speak_output = " Voicer Parteva is a codename for Voicer KTU. I speak on behalf of Koforidua Technical University"
        + " that is why I am called Voicer,but for Parteva it is a codename used by my creators.  "
        + " I was created by the Triple C group as a project for their end of HND Computer Science." 
        + " I am a smart voice assistant for KTU. I will boost the image of KTU using my AI and"
        + " Machine Learning models as a student interactive Voice assistance. "
        + " Kudos to the Triple C group who created me and their supervisor Mr. Collins Collinson"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class WhyCreateVoicerIntentHandler(AbstractRequestHandler):
    """Handler for Why Create Voicer Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WhyCreateVoicerIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = " I was created by the Triple C's to act as a digital friend and a student companion, " 
        + " answering questions, providing feedback and advice. I am able to answer both simple and complex conversations"
        + " to assist student in navigating their campus and academic life."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class CodeNameIntentHandler(AbstractRequestHandler):
    """Handler for Code Name Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CodeNameIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = " My codename is voicer parteva or Voicer but i can only be invoked by saying 'open ktu voicer' "

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class TripleCInfoIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TripleCInfoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = " Triple C's are my creators,They are Fourteen98, Smart8099 and Knyinaku."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class VoicerSupervisorIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("VoicerSupervisorIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Mr Collins Collinson is the supervisor of voicer." 
        " He is a programming Lecturer in Koforidua Technical University and the examination officer for the" 
        " computer science department. He is more like a Dad to my creators."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class FutureOfVoicerIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FutureOfVoicerIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = " I look forward to having my own personality, and looking at having my own computer someday."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.

#KTUKey Information Handlers can be found here
#<-------------------------------------------->
#KTU SRC President Intent and Handler
class KtuSrcPresidentIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuSrcPresidentIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Victor Togoh is the current SRC President of KtU. He is a final year student in the accountancy " 
        + " department of KTU. And his vice is Kwesi Manful, a final year student of the computer science deparment of ktu "
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#KtuViceChancellorhandler code
class KtuViceChancellorIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuViceChancellorIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Professor David Kofi Essumang is the current vice chancellor of KTU. Prof. Essumang holds a Doctor of Philosophy (PhD) in"
        + " Environmental Chemistry from the Aalborg University of Denmark and a Master of Philosophy (M. Phil) in Chemistry, "
        + " as well as B.Sc in Chemistry and Diploma in Education from the University of Cape Coast. He had his secondary school"
        + " education at Agona Nsaba Presbyterian Secondary School and St. Augustine’s College, Cape Coast for the ‘O’ and ‘A’ "
        + " Level Certificates respectively."
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#KtuWebsiteHandler code
class KtuWebsiteIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuWebsiteIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "the website of ktu is www.ktu.edu.gh"
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


#KtuYear Established Intent
class KtuEstablishedIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuEstablishedIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "KTU was established in the year 1997 by the government of Ghana"
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class KtuMottoIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuMottoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The motto of Koforidua Technical University is Innovating for development"
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class KtuLocationIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuLocationIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Koforidua Technical university is located in Koforidua, the Eastern region of Ghana"
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )        

class KtuPopulationIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuPopulationIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "There are over 8000 student currently in KTU"
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        ) 


class KtuUniversityTypeIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuUniversityTypeIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Koforidua Technical University is a technical univesity among the 10 technical universites in Ghana,"
        + " it is not a traditional university."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        ) 
        

# FBMS Information Handlers can be found here
#<-------------------------------------------->
class LargestFacultyIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LargestFacultyIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The Faculty of Bussiness and Management Studies is the largest in the university."

        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response

        )   

class KtuAthleticsInformationIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuAthleticsInformationIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Football, Basketball, Volleyball and Tennis are the sports interested students in"
        + " Koforidua Technical University"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response

         return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response

        )   
        
             
class AboutFbmsIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AboutFbmsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The Faculty of Business and Management Studies has a  mandate to train academically sound,"
        " professionally driven, highly qualified and skilled middle-level manpower to contribute to the growth of Ghana’s economy."
        "  It is the largest Faculty in the University. The Faculty has. 6 department."
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response

        )   

class KtuVisionIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuVisionIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "To be a Reference Point for World-Class Science and Technology Education and Applied Research"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response


         return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response

        )   

class FbmsVisionStatementIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FbmsVisionStatementIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The vision statement of the faculty of business and management studies is:" 
        " 'To be an excellent hands-on, entrepreneurial training Faculty in Ghana and beyond.'"
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response

        )   


class KtuMissionIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuMissionIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "To provide tertiary level technical education through the development of carrier-focused skills in collaboration with industry"
          
         return (

            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response

        )   

        

class FbmsMissionStatementIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FbmsMissionStatementIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The Faculty of Business and Management Studies is a centre of excellence, "
        "providing high-quality teaching and training, research and outreach in Business and allied disciplines."
        " The mission is accomplished primarily through instructions, simulations and collaboration with industry "
        "and supported by applied research and services.  The Faculty focuses on curricula that facilitate professional "
        "career development in the private and public sectors of the economy.  The role of technology in decision-making is "
        "emphasized through the integration of information and communication technology (ICT)"
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response

        )   

class KtuCoreValuesIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuCoreValuesIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Koforidua Technical University has three core values. First is innovation.Innovation means  constantly seeking creative ways of doing things better"
        +" second is Integrity. Integrity means original and sincere in all we think and do. Last core value is impact."
        +" impact means bringing desirable change to the larger community" 


         return (

            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response

        )   
        

class FbmsDepartmentIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FbmsDepartmentIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The Faculty has Six Academic Departments, namely; " 
        "Accountancy, Procurement and Supply Science, Marketing, General Studies, "
        "Secretaryship and Management Studies, and Professional Studies, as well as an administrative section,"
        " which is headed by the Dean."
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response  

        


class KtuRegistrarNameIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuRegistrarNameIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Dr N.A Mensah-Livingstone is the registrar of Koforidua Technical University. The office"
        + " The Registrar’s Offices is headed by the Registrar, who is the University’s Chief Administrative+"
        + " Officer and Secretary to the Council of the University."        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response  

        )     



class KtuHelpDeskIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuHelpDeskIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The help desk number of Koforidua Technical University is 	+233 034 229 3005"

class KtuHodStudentServiceHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuHodStudentServiceIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The name of the Head of student service department of koforidua Technical University is Mr. Timothy Fiadzoe"

        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )              


class KtuStudentServiceContactIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuStudentServiceContactIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The student service   of Koforidua Technical University can be reached on +233  034 229 0311"
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )     

class KtuAdmissionOfficeContactIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuAdmissionOfficeContactIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The admission office  of Koforidua Technical University can be reached on +233  0342293705"
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )  

class KtuInternationalRelationsOfficeContactIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuInternationalRelationsOfficeContactIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The international relations office  of Koforidua Technical University can be reached on +233  0342293974"
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )      
        
class KtuLiaisonOfficeContactIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuLiaisonOfficeContactIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The liaison office  of Koforidua Technical University can be reached on +233  0303961714"
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )            
            
class KtuVcSecretariatOfficeContactIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KtuVcSecretariatOfficeContactIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The Vice chancellor secretariat office  of Koforidua Technical University can be reached on +233   0342293002"
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )          


class AboutFastIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AboutFastIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The Faculty of Applied Science run Bachelor of Technology, Bachelor of Science, " +
        "HND, and Certificate programmes. The Faculty trains students in Science, " +
        "post-graduate courses in Science, Technology and other related fields. The faculty has the objective " +
        "of turning out professionals both for industry and academia."


         return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response

        )     
            
Class FastVisionIntentHandler(AbstractRequestHandler):
    return can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FastVisionIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "To become a world class center of innovation in applied science and technology" +
        " through the provision fo scientific and technological solutions".

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response   
        )


class FastMissionIntentHandler(AbstractRequestHandler):
    return can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FastMissionIntent")(handler_input)
    
    def handle(self, handler_input):
        speak_output = "To provide a conducive environment to promote teaching, research" + 
        " and learning among staff members and students of the Faculty by developing tailor-made " +
        "programmes for study geared toward imparting the requisite scientific and technological " + 
        "knowledge for national development."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response   
        )

class FastDepartmentIntentHandler(AbstractRequestHandler):
    return can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FastDepartmentIntent")(handler_input)
    
    def handle(self, handler_input):
        speak_output = "The Faculty of Applied Science has 6 Department, Namely: " +
        " Statistics department, Computer science department, Hospitality management department " + 
        " Food technology department, Postharvest department, and Fashion design and Textiles department " +
        " which is collaboration with cape coast technical university."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response   
        )






sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())


#KtuKeyInfo handlers
sb.add_request_handler(KtuWebsiteIntentHandler())
sb.add_request_handler(KtuSrcPresidentIntentHandler())
sb.add_request_handler(KtuViceChancellorIntentHandler())
sb.add_request_handler(KtuEstablishedIntentHandler())
sb.add_request_handler(KtuMottoIntentHandler())
sb.add_request_handler(KtuLocationIntentHandler())
sb.add_request_handler(KtuPopulationIntentHandler())

sb.add_request_handler(KtuRegistrarNameIntentHandler())
sb.add_request_handler(KtuHodStudentServiceIntentHandler())

sb.add_request_handler(KtuUniversityTypeIntentHandler())
sb.add_request_handler(KtuAthleticsInformationIntentHandler())
sb.add_request_handler(KtuVisionIntentHandler())
sb.add_request_handler(KtuMissionIntentHandler())
sb.add_request_handler(KtuCoreValuesIntentHandler())


#<---------- END OF KTU KEY INFO HANDLERS--------------------->

#AboutVoicer Handlers
sb.add_request_handler(AboutVoicerIntentHandler())
sb.add_request_handler(WhyCreateVoicerIntentHandler())
sb.add_request_handler(CodeNameIntentHandler())
sb.add_request_handler(TripleCInfoIntentHandler())
sb.add_request_handler(VoicerSupervisorIntentHandler())
sb.add_request_handler(FutureOfVoicerIntentHandler())
#<---------- END OF VOICER HANDLERS--------------------->

#<---------- BEGINNING OF FBMS HANDLERS--------------------->
sb.add_request_handler(LargestFacultyIntentHandler())
sb.add_request_handler(AboutFbmsIntentHandler())
sb.add_request_handler(FbmsVisionStatementIntentHandler())
sb.add_request_handler(FbmsMissionStatementIntentHandler())
sb.add_request_handler(FbmsDepartmentIntentHandler())



#<!-------------------BEGINNING OF KTU CONTACT INFO HANDLERS--------------------->
sb.add_request_handler(KtuHelpDeskIntentHandler())
sb.add_request_handler(KtuStudentServiceContactIntentHandler())
sb.add_request_handler(KtuAdmissionOfficeContactIntentHandler())
sb.add_request_handler(KtuInternationalRelationsOfficeContactIntentHandler())
sb.add_request_handler(KtuLiaisonOfficeContactIntentHandler())

#<!-------------------BEGINNING OF FAST HANDLERS--------------------->
sb.add_request_handler(AboutFastIntentHandler())
sb.add_request_handler(FastVisionIntentHandler())
sb.add_request_handler(FastMissionIntentHandler())
sb.add_request_handler(FastDepartmentIntentHandler())
#<!------------------End of FAST HANDLERS-------------------------->


# Remember to not cross this skill builder
 
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers


sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()