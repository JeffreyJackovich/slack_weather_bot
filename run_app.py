from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent 
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput 

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')

agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)



input_channel = SlackInput('<Insert OAuth Access Token>',
							'<Insert Bot User OAuth Access Token>',
							'<Insert Verification Token>',
							True)


agent.handle_channel(HttpInputChannel(5004, '/', input_channel))