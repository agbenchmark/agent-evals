import subprocess

def call_agent_protocol():
    command = "agent-protocol test --url=http://127.0.0.1:8000 -k test_create_agent_task"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    call_agent_protocol()
