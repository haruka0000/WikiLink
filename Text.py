import sqlite3

def get_wiki(title):
  conn = sqlite3.connect("wikipedia.db")
  c = conn.cursor()
  wiki_data = list(c.execute('''SELECT * FROM wiki where title="%s";''' % title))[0]
  conn.commit()
  return wiki_data

#print(get_wiki("ジオン公国"))
