import os
import typer
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_KEY"),  # This is the default and can be omitted
)
#openai.api_key = os.getenv("OPENAI_KEY")

app = typer.Typer()

@app.command() 

def interactive_chat(
		temperature: float = typer.Option(0.7, help="Control Randomness. Defaults to 0.7"),
	    max_tokens: int = typer.Option(
	        150, help="Control length of response. Defaults to 150"
	    ),
	    model: str = typer.Option(
	        "gpt-3.5-turbo", help="Control the model to use. Defaults to gpt-3.5-turbo"
	    ),
    ):
    """Interactive CLI tool to chat with ChatGPT."""
    typer.echo(
        "Starting interactive chat with ChatGPT. Type 'exit' to end the session."
    )

    messages = []
    model= "gpt-3.5-turbo"

    while True:
        prompt = input("You: ")
        messages.append({"role":"user", "content":prompt})

        if prompt == "exit":
            typer.echo("ChatGPT: Goodbye!")
            break

        response = client.chat.completions.create(
        	model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )

        typer.echo(f'ChatGPT: { response.choices[0].message.content }')
        messages.append(response.choices[0].message)


if __name__ == "__main__":
    app()