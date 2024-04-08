import json
from pprint import pprint
from typing import TypedDict



class Movies(TypedDict):
  title: str
  original_title: str
  is_movie: bool
  imdb_rating: float
  year: int
  characters: list[str]
  budget: None | float


string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

movie: Movies = json.loads(string_json)
pprint(movie, indent=2)
print(movie['year'] + 50)

print(json.dumps(movie, indent=2))