import os
import subprocess
import signal
import sys

from Bot.core.config import bot

def stop_script():
    try:
        os.kill(os.getpid(), signal.SIGTERM)
    except Exception as e:
        print(f"Exception stopping script: {e}")

async def update_project(chat_id):
    print("Updating project with Git...")
    try:
        project_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.join(project_dir, "..")

        os.chdir(project_dir)

        repo_url = "https://github.com/1nkret/tele-guard.git"
        branch_name = "main"

        if not os.path.exists(project_dir):
            print(f"Cloning repo {repo_url}...")
            subprocess.run(["git", "clone", repo_url, project_dir], check=True)
        else:
            print(f"Dir {project_dir} is exists. Execute git pull...")
            os.chdir(project_dir)
            subprocess.run(["git", "pull", "origin", branch_name], check=True)

        await bot.send_message(chat_id, "Bot successful updated.")
        print("Project updated.")
    except subprocess.CalledProcessError as e:
        print(f"Error during update: {e}")
        sys.exit(1)

def restart_script():
    print("Restart script...")
    try:
        local_path = os.path.abspath(os.getcwd())
        python_path = os.path.join(local_path, '..', '..', '.venv', 'Scripts', 'python.exe')
        script_path = os.path.join(local_path, '..', '..', "main.py")
        subprocess.Popen([python_path, script_path])
        print("Script started.")
    except Exception as e:
        print(f"Error during restart: {e}")

if __name__ == "__main__":
    update_project()
    restart_script()
