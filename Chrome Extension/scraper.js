/**
*   This will be the heart of the scraper, where we will implement the code similar to the scraper.py script
**/

let url = "https://coinmarketcap.com/"

let scraper = (url) => {
  $.get(url, function(response) {
    let cryptoName = response.match(/<td class="no-wrap currency-name">\<\/td>/)[0];
    let cryptoPrice = response.match(/<a class="price">\<\/a>/)[0];
    console.log(cryptoName + " " + cryptoPrice);
    let returnVal = [];
    
  }
};
