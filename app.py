
import os
import streamlit as st

from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
# Load environment variables
load_dotenv(find_dotenv())


# Pydantic schema
class Movie(BaseModel):
    title: str = Field(description="The title of the movie")
    year: int = Field(description="The release year")
    genre: list[str] = Field(description="The movie genres")
    director: str = Field(description="The director")
    plot: str = Field(description="A short plot summary")


# Create LangChain pipeline
@st.cache_resource
def create_chain():
    model = init_chat_model("google_genai:gemini-3.6-flash")

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
You are a movie information extraction assistant.

Extract movie information from the user's paragraph.

Do not invent information that isn't present.
Return the information according to the provided schema.
"""
        ),
        ("human", "{movie_paragraph}")
    ])

    structured_model = model.with_structured_output(Movie)

    return prompt | structured_model


chain = create_chain()


# Streamlit UI
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬"
)

st.title("🎬 Movie Information Extractor")

st.write(
    "Paste a movie paragraph and the AI will extract structured movie information."
)


movie_paragraph = st.text_area(
    "Movie Paragraph",
    placeholder="Paste your movie paragraph here...",
    height=250
)


if st.button("Extract Movie Information", type="primary"):

    if not movie_paragraph.strip():
        st.warning("Please enter a movie paragraph.")

    else:
        with st.spinner("Analyzing movie..."):
            try:
                response = chain.invoke({
                    "movie_paragraph": movie_paragraph
                })

                st.success("Movie information extracted successfully!")

                st.subheader("Structured Output")

                st.json(response.model_dump())

            except Exception as e:
                st.error(f"Error: {e}")