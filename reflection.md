# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game produced a decent looking webpage and appeared correctly setup to begin a new game.

- List at least two concrete bugs you noticed at the start  
  1- When a guess was made that was lower than the secret value, the hint said to "Go lower" and when a guess was higher than the secret value, the hint was to "Go higher.
  2- When a guess matches the secret, the game correctly indicates a win. Then when the "new game" button is clicked:
    * the banner indicating the game was won does not go away.
    * a new secret value is generated, but:
       * subsequent guesses do not produce any hints
       * the guess value is not added to the history list
       * the attempts count is not incremented.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  * Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  * Claude correctly suggested a correction to the "guess higher/lower" hints and logic.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  * Claude did not make any incorrect or misleading suggestions on this project. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran multiple tests of guesses that were too low, too high, and correct, to make sure the game logic was correct.
- Did AI help you design or understand any tests? How?
  AI assisted with correcting the tests in test_game_logic that had errors. It correctly identified the issues, one of which was that the "comparison" tests were using text that did not match what the game actually output after a guess. After these corrections all tests passed.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The original code converted the secret number into text whenever the number of guesses was even. This could cause errors during the comparison of guesses because sometimes the logic was comparing a string to an integer.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
If a variable is not created with session state (st.session_state.variable_name), it gets reset every time the script is run. 
- What change did you make that finally gave the game a stable secret number?
I removed the logic that changed the secret number to a string.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Frequent commits with clear messages so it is easy to see what was changed and when if code needs to be rolled back.
- What is one thing you would do differently next time you work with AI on a coding task?
Work on small chunks at a time and making sure to tell AI to suggest changes that I must confirm before they are implemented.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It is really remarkable how these LLM's create the illusion of understanding and reasoning when fundamentally they are probability machines predicting string tokens. It has really increased my desire to more thoroughly understand the underlying mathematics of these models.
