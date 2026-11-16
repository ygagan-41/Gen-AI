from langchain_text_splitters import CharacterTextSplitter

text = """Breaking the fourth wall, Suzanne says she prefers her professional
 surname Stone over her Italian American husband's, and describes her passionate romance with
 Larry Maretto. For the camera, Larry's sister Janice, who trains for the Ice
 Follies, voices her low opinion of Suzanne, and how she tried, unsuccessfully, 
 to dissuade her brother from getting involved with "The Ice Maiden".

"""

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)

result = splitter.split_text(text)

print(result)