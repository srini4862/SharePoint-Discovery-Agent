"""Runtime entry point for the SharePoint Discovery Agent."""

from dotenv import load_dotenv

from agents.main_agent import create_sharepoint_discovery_agent


# --------------------------------------------------
# Environment Initialization
# --------------------------------------------------

load_dotenv()


# --------------------------------------------------
# Static UX Content
# --------------------------------------------------

WELCOME_MESSAGE = """
Welcome to the SharePoint Discovery Agent.

I coordinate SharePoint discovery operations across
environment assessment, dependency validation,
discovery execution, and reporting workflows.

Provide your discovery objective or relevant
environment details to begin.
"""


# --------------------------------------------------
# Runtime
# --------------------------------------------------

def run():
    """Start the SharePoint Discovery Agent runtime."""

    print(WELCOME_MESSAGE)

    try:
        agent = create_sharepoint_discovery_agent()

    except Exception as exc:
        print(
            "\nFailed to initialize "
            f"SharePoint Discovery Agent: {exc}"
        )
        return

    config = {
        "configurable": {
            "thread_id": "sharepoint-discovery-session"
        }
    }

    while True:

        try:
            user_input = input("\nHuman: ").strip()

            if not user_input:
                continue

            response = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": user_input
                        }
                    ]
                },
                config=config
            )

            messages = response.get("messages", [])

            if not messages:
                continue

            latest_message = messages[-1]

            agent_reply = getattr(
                latest_message,
                "content",
                str(latest_message)
            )

            print(f"\nAgent: {agent_reply}")

        except KeyboardInterrupt:
            print("\n\nSession interrupted by user.")
            break

        except Exception as exc:
            print(f"\nOperational error: {exc}")


# --------------------------------------------------
# Application Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    run()
