from pathlib import Path

def define_env(env):
    @env.macro
    def read_file(relative_path):
        full_path = Path("docs") / relative_path
        return full_path.read_text(encoding="utf-8")
