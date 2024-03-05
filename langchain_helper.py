from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables= ['animal_type', 'pet_color'],
        template = "I have a {animal_type} and I want it's name. It is {pet_color} and I want it to be cool. Tell me what color, and what animal i inform you"
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

    response= name_chain({
        'animal_type': animal_type
        , 'pet_color': pet_color
    })
    return response


if __name__ == "__main__":
    print(generate_pet_name("cow", "red"))