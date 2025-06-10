
from agentuniverse.agent.input_object import InputObject

from agentuniverse.agent.template.openai_protocol_template import OpenAIProtocolTemplate


class DemoOpenAIProtocolAgent(OpenAIProtocolTemplate):

    def input_keys(self) -> list[str]:
        return ['input']

    def output_keys(self) -> list[str]:
        return ['output']

    def parse_input(self, input_object: InputObject, agent_input: dict) -> dict:
        agent_input['input'] = input_object.get_data('input')
        return agent_input

    def parse_result(self, agent_result: dict) -> dict:
        return {**agent_result, 'output': agent_result['output']}