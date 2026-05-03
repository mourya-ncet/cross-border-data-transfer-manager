def load_prompt(file_name, user_input):
    try:
        with open(f"prompts/{file_name}", "r") as file:
            prompt = file.read()

        # Replace placeholder with actual input
        prompt = prompt.replace("{input}", user_input)

        return prompt

    except Exception as e:
        print("Error loading prompt:", e)
        return None