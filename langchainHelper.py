
from langchain_core.prompts import PromptTemplate
from langchain.chains import SequentialChain, LLMChain
from langchain_groq import ChatGroq
import os

os.environ["GROQ_API_KEY"] = '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'

llm = ChatGroq(
    # model="mixtral-8x7b-32768",
    model="llama3-8b-8192",
    temperature=0.0,
    max_retries=2,
)


def generate_restaurant_name_and_menu(cuisine):
    prompt_template_name = PromptTemplate(

        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest only a single name for my restaurant",

    )

    chain_name = LLMChain(prompt=prompt_template_name,
                          llm=llm, output_key="restaurant_name")
    # chain_name = prompt_template_name | llm

    prompt_template_menu = PromptTemplate(

        input_variables=["restaurant_name"],
        template="Suggestions for menu items for {restaurant_name} restaurant. Give only item names nothing else.",

    )

    chain_menu = LLMChain(prompt=prompt_template_menu,
                          llm=llm, output_key="menu_items")
    # chain_menu = prompt_template_menu | llm

    sequential_chain = SequentialChain(
        chains=[chain_name, chain_menu],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"],
        verbose=True
    )

    return sequential_chain({"cuisine": cuisine})


if __name__ == "__main__":
    print(generate_restaurant_name_and_menu("Italian"))
