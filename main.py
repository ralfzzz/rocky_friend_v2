from config import AI_NAME

from ui.cli import user, ai

from llm.ollama_client import ask
from llm.prompt_builder import PromptBuilder

from personality.personality_manager import PersonalityManager

from memory.memory_manager import MemoryManager
from memory.profile_manager import ProfileManager

from learning.profile_extractor import extract_name
from learning.fact_extractor import extract_fact


def main():

    personality = PersonalityManager()

    memory = MemoryManager()

    profile = ProfileManager()

    print("=" * 50)
    print(AI_NAME)
    print("=" * 50)
    print("Ketik /exit untuk keluar.\n")

    while True:

        question = user().strip()

        if not question:
            continue

        # ----------------------------
        # COMMAND
        # ----------------------------

        if question.lower() == "/exit":
            break

        if question.lower() == "/profile":

            print(profile.build_profile())

            continue

        if question.lower() == "/clear":

            memory.short.messages.clear()

            print("Short memory dibersihkan.")

            continue

        # ----------------------------
        # PROFILE
        # ----------------------------

        name = extract_name(question)

        if name:

            profile.set("name", name)

        facts = extract_fact(question)

        for key, value in facts.items():

            profile.set(key, value)

        # ----------------------------
        # SHORT MEMORY
        # ----------------------------

        memory.add_chat(

            "user",

            question

        )

        # ----------------------------
        # BUILD PROMPT
        # ----------------------------

        builder = PromptBuilder(

            personality=personality.build_prompt(),

            profile=profile.build_profile(),

            history=memory.history()

        )

        messages = builder.build()

        # ----------------------------
        # OLLAMA
        # ----------------------------

        answer = ask(messages)

        # ----------------------------
        # SAVE CHAT
        # ----------------------------

        memory.add_chat(

            "assistant",

            answer

        )

        ai(answer)


if __name__ == "__main__":

    main()