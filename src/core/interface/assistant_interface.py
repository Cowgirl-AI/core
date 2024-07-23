from src.core.assistant.core_assistant import CoreAssistant

class AssistantInterface(CoreAssistant):
    """
    Assistant Interface
    """
    def __init__(self, assistant_name=None):
        super().__init__(assistant_name=None)

    def stream_data(self):
        """
        Usage::
            >>> interface = AssistantInterface(assistant_name='Data Generation Assistant v2')
            >>> interface.stream_data()

        """

        self.set_prompt()
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": self.content}
            ],

            # Potentially make the following conditional
            stream=True, 
            response_format=self.response_format
        )
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                # Add clause to write to file or database
                print(chunk.choices[0].delta.content, end="")


if __name__=="__main__":
    AssistantInterface()
    # interface = AssistantInterface(assistant_name='Data Generation Assistant v2')
    # interface.stream_data()