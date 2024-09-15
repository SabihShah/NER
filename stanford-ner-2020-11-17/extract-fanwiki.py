import fandom

# Set the wiki to "jojo" (JoJo's Bizarre Adventure)
fandom.set_wiki("jojo")

# Search for "Hol Horse" to get the precise page title
search_results = fandom.search("Hol Horse")
print(search_results)

if search_results:
    text = []
    for result in search_results:
        try:
            # Get the first search result's title
            page_title = result[0]
            # Load the page using the page title
            page = fandom.page(title=page_title)
            # Get the content of the page
            content = page.content

            print(content.keys())
            # Save the content to fanwiki.txt
            text.append(content['content'])
        except:
            continue
        
    with open('fanwiki.txt', 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(text))
    print("Content successfully written to fanwiki.txt")
else:
    print("No search results found for 'Hol Horse'")
