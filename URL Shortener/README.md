
# URL Shortener (Flask API)

This is a simple Flask-based URL Shortener API that allows users to shorten long URLs, redirect shortened URLs to their original destinations, and track the number of times each shortened link has been accessed.

All data is stored locally in a JSON file (urldata.json), making it easy to test and run without a database.

## Features

- ✅ Shorten any valid HTTP/HTTPS URL
- 🔁 Redirect short links to their original URLs
- 📊 Tracks the number of times each short link is accessed
- 🧩 Prevents duplicate URLs
- 🧠 Ensures unique short codes using SHA-256 hashing
- 🧾 Stores data in a local JSON file (urldata.json)


## Tech Stack

- Python 3.x

- Flask (Web framework)

- hashlib & random (For generating unique short codes)

- JSON (For local storage)

- urllib.parse (For URL validation) 
## Installation & Usage

#### Clone the repository:

```bash
- git clone https://github.com/yourusername/url-shortener.git
- cd url-shortener
```
#### The app will run locally on:
```bash
- http://localhost:5000
```
#### All available app routes:
```bash
- /table            #Displays all urls with shortened urls and number of times accessed
- /table/shorten    #shortens the input long url
- /<short_url>      #Use the shortened url to access long url
```

#### The POST method should be entered in the following syntax:

```bash
{
    "url" : "https://www.example123.com/"
}
```

## How It Works
- When a URL is submitted, it’s validated using Python’s urlparse() to ensure it has a valid HTTP/HTTPS scheme.

- A unique short code is generated using a SHA-256 hash of the original URL.

- The short link and original URL are stored in urldata.json.

- When someone visits the short link, the server redirects them to the original URL and increments the access counter.

## Author

Aditya Kumar Sharma (Spark)

- email: shradi0612@gmail.com
- Github: https://github.com/Sparky-06
