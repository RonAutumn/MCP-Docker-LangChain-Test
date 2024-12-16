from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms.fake import FakeListLLM

def create_mock_chain():
    responses = ["Prompt received: {}".format]
    fake_llm = FakeListLLM(responses=responses)
    prompt = PromptTemplate(
        input_variables=["user_input"],
        template="Process this input: {user_input}"
    )
    return LLMChain(llm=fake_llm, prompt=prompt)

def process_input(user_input: str) -> str:
    chain = create_mock_chain()
    return chain.run(user_input=user_input)

def main():
    test_input = "Hello, LangChain!"
    print(f"Testing with input: {test_input}")
    result = process_input(test_input)
    print(f"Response: {result}")

if __name__ == "__main__":
    main()