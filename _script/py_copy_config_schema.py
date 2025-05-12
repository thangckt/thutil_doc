def append_schema_text(yaml_schema_file: str, text_file: str):
    """Append yaml text to .md file."""
    with open(yaml_schema_file, "r") as f:
        text = f.read()
    schema_text = "\n```yaml\n" + text + "\n```\n"
    schema_text = "\n## Schema:\n" + schema_text
    ### append yaml schema
    with open(text_file, "a") as f:
        f.write(schema_text)
    return


def append_example_config(yaml_config_file: str, text_file: str):
    """Append yaml text to .md file."""
    with open(yaml_config_file, "r") as f:
        text = f.read()
    schema_text = "\n```yaml\n" + text + "\n```\n"
    schema_text = "\n## Example configuration:\n" + schema_text
    ### append yaml schema
    with open(text_file, "a") as f:
        f.write(schema_text)
    return


##### ANCHOR: udpate the blog posts
def main():
    ### Append schema to the .md files
    append_schema_text(
        yaml_schema_file="./thutil/schema/schema_arg_remote_machine.yml",
        text_file="./_docs/schema_doc/config_remote_machine.md",
    )
    ### Append example configuration to the .md files
    append_example_config(
        yaml_config_file="./thutil/schema/example_machine_config.yml",
        text_file="./_docs/schema_doc/config_remote_machine.md",
    )
    return


if __name__ == "__main__":
    main()
