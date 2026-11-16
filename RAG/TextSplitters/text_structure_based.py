from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Breaking the fourth wall, Suzanne says she prefers her professional
 surname Stone over her Italian American husband's, and describes her passionate romance with
 Larry Maretto. For the camera, Larry's sister Janice, who trains for the Ice
 Follies, voices her low opinion of Suzanne, and how she tried, unsuccessfully, 
 to dissuade her brother from getting involved with "The Ice Maiden".
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(chunks)
print(len(chunks))