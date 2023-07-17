# Steam Market Bot

## Requirements

* Discord Bot (chat & answer)
* Collect data from Steam Market -> Frequency: run as needed (create an endpoint to programmatically update prices)
* Steam Endpoint: <https://steamcommunity.com/market/search/render/?query=&start=0&count=100&search_descriptions=0&sort_column=popular&sort_dir=desc&norender=1>
* Allow user to search for items by query (broad match)
* Notify price changes (?)
* Hosting on <https://replit.com/>

## To-do

1. Write a function to get all marketplace items from the Steam endpoint (1)
2. Set up local database for marketplace items
3. Write a function to use the result of (1) and save to database
4. Set up FastAPI app
5. Write `@app.get` route to return all item listings
6. Write `@app.post` route to trigger the update of marketplace items to local database
7. Integrate with Discord as bot user
