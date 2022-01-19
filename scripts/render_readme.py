from pathlib import Path


def main():
    project_name = Path.cwd().name

    readme_path = Path.cwd() / "README.md"

    readme_text = readme_path.read_text()

    title_name = project_name.replace("_", " ").title()
    dash_name = project_name.replace("_", "-")

    readme_text = readme_text.replace("{{TITLE|title}}", title_name)
    readme_text = readme_text.replace("{{TITLE|dash}}", dash_name)

    readme_path.write_text(readme_text)


if __name__ == "__main__":
    main()
