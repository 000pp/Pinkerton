from random import choice

def get_user_agent() -> str:
    " Return a random User-Agent from user-agents.txt file to be used in the request "

    file_path: str = 'src/pinkerton/data/user-agents.txt'
    with open(file_path) as content:
        user_agents: str = content.readlines()
        user_agent: str = choice(user_agents).strip()

        return user_agent