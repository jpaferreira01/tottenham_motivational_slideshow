const puppeteer = require('puppeteer');
const express = require('express');
const app = express();
const port = 3000;

// Endpoint to get the last opponent Tottenham played
app.get('/last-opponent', async (req, res) => {
  const url = 'https://www.flashscore.com/team/tottenham-hotspur/Y8A8y5dY/';
  
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url);

  const lastOpponent = await page.evaluate(() => {
    const matchElement = document.querySelector('.event__team--home');
    const opponent = matchElement ? matchElement.textContent.trim() : 'Opponent not found';
    return opponent;
  });

  await browser.close();
  res.json({ opponent: lastOpponent });
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
