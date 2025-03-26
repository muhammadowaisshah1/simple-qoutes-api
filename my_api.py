from fastapi import FastAPI
import random

app=FastAPI()

quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Act as if what you do makes a difference. It does. – William James",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
    "The secret of getting ahead is getting started. – Mark Twain"
]

@app.get("/quotes")
def get_jokes():
    return {"quotes":random.choice(quotes)}












