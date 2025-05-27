import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_repo_files():
    file_list = []
    for root, _, files in os.walk("."):
        if root.startswith("./.git") or "node_modules" in root:
            continue
        for file in files:
            if file.endswith((".py", ".tf", ".yaml", ".yml", ".sh")):
                path = os.path.join(root, file)
                try:
                    with open(path, "r") as f:
                        content = f.read()
                        file_list.append({"path": path, "content": content})
                except Exception:
                    continue
    return file_list

def call_openai_model(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're an assistant that summarizes codebase structure into Mermaid architecture diagrams."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response['choices'][0]['message']['content']

def build_prompt(files):
    combined = ""
    for f in files[:10]:  # Limit for prompt size
        combined += f"## File: {f['path']}\n```\n{f['content'][:1000]}\n```\n\n"
    return f"""
You are given code from a GitHub repository. Generate a high-level architecture diagram using Mermaid syntax in markdown. Focus on application logic, databases, infra (like Kubernetes/Terraform), and CI/CD pipelines.

Output only valid markdown containing Mermaid code block.

{combined}
"""

def main():
    files = get_repo_files()
    prompt = build_prompt(files)
    diagram_md = call_openai_model(prompt)

    os.makedirs("docs", exist_ok=True)
    with open("docs/architecture.md", "w") as f:
        f.write(diagram_md)
    print("Generated docs/architecture.md")

if __name__ == "__main__":
    main()
