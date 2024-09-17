import fandom

fandom.set_wiki("jojo")

search_results = fandom.search("Hol Horse")
print(search_results)

if search_results:
    text = []
    for result in search_results:
        try:
            page_title = result[0]
            page = fandom.page(title=page_title)
            content = page.content

            print(content.keys())
            text.append(content['content'])
        except:
            continue
        
    with open('fanwiki.txt', 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(text))
    print("Content successfully written to fanwiki.txt")
else:
    print("No search results found for 'Hol Horse'")
