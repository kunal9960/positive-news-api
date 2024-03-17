# News Email Digest 🗞️

This Python script fetches the latest news articles from TechCrunch using the News API and sends them via email.


## Requirements

- Python 3.10
- Requests
- Gmail


## Usage

This project requires Requests library.

1. Install required packages:

   ```
   pip install requests
   ```
   
2. Set up environment variables:

- **API**: Set this variable to your News API key at [NewsAPI](https://newsapi.org/)
- **EMAIL**: Set this variable to your email address.
- **PASSWORD**: Set this variable to your email app password (*How to generate your [email app password](https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237)*)

3. Don't forget to restart your windows

4. Run the script (Donot run `send_email.py`)
```
python main.py
```


## Customization

You can customize various parameters to tailor the news digest to your preferences:

- **Language:** Modify the language parameter in the main.py script to specify the language of the news articles (e.g. en for English, es for Spanish etc.)
- **Source:** Change the source parameter to specify the news source (e.g. techcrunch, bbc-news, cnn etc.)
- **Domains:** Specify one or more domains to filter news articles by domain. This parameter allows you to receive news articles only from specific domains (e.g. bbc.co.uk, techcrunch.com, engadget.com etc.)


## Screenshots

### Example

![Example](https://github.com/kunal9960/positive-news-api/blob/master/Example.png)

### Upcoming Web App version of the program
This will enable the user to use the program hassel free in just one click.
![Future](https://github.com/kunal9960/positive-news-api/blob/master/Future%20version.png)


## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to fork the repository and submit a pull request. You can also open an issue to report bugs or suggest enhancements.


## Acknowledgments

Feel free to contact me if you need help with any of the projects :)
