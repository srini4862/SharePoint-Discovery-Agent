"""Main entry point for SharePoint Discovery Agent."""

import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add project root and src to system path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "src"))
sys.path.insert(0, str(project_root))

from config.settings import settings
from agents.main_agent import create_sharepoint_discovery_agent


def main():
    """Main entry point for the SharePoint Discovery Agent."""
    WELCOME_MESSAGE = """
    Welcome to SharePoint Discovery Agent.

    Capabilities:
    - SharePoint tenant discovery
    - Site inventory assessment
    - Permission analysis
    - Storage analysis
    - Migration readiness assessment
    - Reporting and export generation

    How can I help you today?
    """
    # Create the deep agent
    try:
        agent = create_sharepoint_discovery_agent()
        print(WELCOME_MESSAGE)
    except Exception as e:
        print(f"Error initializing Deep Agent: {e}")
        sys.exit(1)

    # # Start conversational loop
    # print("Starting conversational session...")
    # print("Type 'exit', 'quit', or 'bye' to end the session.")
    # print()

    config = {"configurable": {"thread_id": "chat-session"}}

    while True:
        try:
            user_input = input("Human: ")
            if not user_input.strip():
                continue

            # Check for exit intent with various phrases
            exit_phrases = [
                "exit", "quit", "bye", "goodbye",
                "i'm done", "im done", "that's all", "thats all",
                "stop", "finish", "end", "no more", "nothing", 
                "nothing else", "done", "ok thanks", "thanks bye"
            ]
            user_text = user_input.lower().strip()
            
            # Exit if exact match or if user input starts with exit phrase (like "no i am done")
            if user_text in exit_phrases or any(user_text.startswith(p) for p in exit_phrases) or "good by" in user_text:
                print("Agent: Goodbye!")
                break

            # Send message as a list of dictionaries to satisfy the State requirements
            response = agent.invoke(
                {"messages": [{"role": "user", "content": user_input}]},
                config=config
            )

            # The response is the content of the last message in the state
            agent_reply = response['messages'][-1].content
            print(f"Agent: {agent_reply}")
            
            # Intelligently stop if the agent acknowledges the end of the conversation
            lower_reply = agent_reply.lower()
            if "goodbye" in lower_reply or "have a good day" in lower_reply or "farewell" in lower_reply:
                break

        except KeyboardInterrupt:
            print("\nAgent: Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
