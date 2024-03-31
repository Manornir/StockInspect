# StockInspect - Final project in algorithmic trading using Machine Learning

## Description
In this project, I developed a website that presents data regarding the [S&P500](https://en.wikipedia.org/wiki/S%26P_500) stock price index.  
Every time the user logs into the website, a stocks prices table will be shown. Its columns are:  

  * Stock Ticker - A unique combination of letters and numbers that represents a particular stock.  
  * Today Price - Stock closing price.  
  * Predicted Tomorrow Price - A forecasted tomorrow’s closing price.  

The user has to provide a `csv file` containing today’s S&P500 stocks prices.  
Another csv file containing past data will be updated with the new data delivered by the user, who will get a new csv file consisting of tomorrow’s predicted prices.  
Using a machine learning model, trained on reliable raw S&P 500 stock price index data from the past 10 years, today’s new price data and tomorrow’s predicted price data will be displayed in the mentioned above website.

## User Instructions
1.	Clone the repository and open it in Pycharm.

2.	Create a virtual environment directory for the project:  

    a.	Press `ctrl+alt+s`  
    b.	"Project: XXX"  
    c.	"Python Interpreter"  
    d.	"Add Interpreter" => "Add Local Interpreter"  
    e.	Select "Virtual Environment" => "New"  
    f.	In Location, name it "venv" and save  

3.	Then, run in pycharm's terminal: `pip install -r requirements.txt`

4.	Modify the paths in the relevant fields within the Python project “algotrading_webserver” directory on your computer:  
  a.	In “FilesManager.py” modify the following paths under:  
    i.	“__init__(self)” ⇒ “self.new_full_data”, “self.stocks_by_id”, “self.all_stocks_best_parameters” (in `pd.read_csv()` function).  
    ii.	“Read_input_data” ⇒ “self.new_day_prices” (in `pd.read_csv()` function).  
    iii.	“update_stocks_data” ⇒ “self.new_full_data” (in `pd.to_csv()` function).  
    iv.	“get_paths_by_ids” ⇒ “paths_list”.  
  b.	In “Predictor.py” modify the following paths under:  
    i.	“save_predictions” ⇒ “new_day_preds_df” (in `pd.to_csv()` function).  

5.	In the algotrading_webserver directory, open the terminal and run the command “python .\Webserver.py” (write and press enter). Estimated runtime is 5-10 minutes (depending on the number of stocks provided for prediction).  

6.	In the algotrading_client directory, open the terminal and navigate to stocks_prediction directory (using cd stocks_prediction command) and run the command “python manage.py runserver” (write and press enter).  
Click on the link that appears in the terminal. The website will appear in the browser.  

7.	On the next day, the user is expected to get a csv file containing the data about the closing prices of S&P 500 stocks. In order to get the next day’s predictions, the user needs to change the file’s name to “latest dates of stocks.csv” and put it in “read_input_data” ⇒ “model_input”.
