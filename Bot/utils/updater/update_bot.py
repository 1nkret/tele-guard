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
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

        os.chdir(project_root)

        repo_url = "https://github.com/1nkret/tele-guard.git"
        branch_name = "main"

        if not os.path.exists(project_root):
            print(f"Cloning repo {repo_url}...")
            subprocess.run(["git", "clone", repo_url, project_root], check=True)
        else:
            print(f"Dir {project_root} exists. Executing git pull...")
            subprocess.run(["git", "pull", "origin", branch_name], check=True)

        await bot.send_message(chat_id, "Bot successfully updated.")
        print("Project updated.")
    except subprocess.CalledProcessError as e:
        print(f"Error during update: {e}")
        sys.exit(1)


def restart_script():
    print("Restarting script...")
    try:
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
        python_path = os.path.join(project_root, '.venv', 'Scripts', 'pythonw.exe')
        script_path = os.path.join(project_root, "main.py")

        os.chdir(project_root)

        subprocess.Popen([python_path, script_path], cwd=project_root)
        print("Script started.")
    except Exception as e:
        print(f"Error during restart: {e}")
