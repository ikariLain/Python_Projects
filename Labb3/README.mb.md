# Lab 3 - Guess the Number
I based on the following assignments I hade in C# but did it in python
# About the Assignment

Now it's time to build your first real program that can actually be fun to use - a simple game!

You will create a fairly simple game where the user gets to guess a number. The user will get some hints and has a limited number of attempts to guess.

# What You Need to Do

- [ ]  Create a new project in Visual Studio (Console Application → C# → .Net Core)
- [ ]  Name the project "NumbersGame"
- [ ]  When the program starts, the following should be printed in the console: "Welcome! I'm thinking of a number. Can you guess which one? You get five attempts."
- [ ]  The program should randomly generate a number that the user needs to guess but of course not print what number it is. Preferably, the program generates a number between 1 and 20, but you can choose.
- [ ]  The user should then input a number they want to guess.
- [ ]  If the number is wrong, the program should respond with either "Sorry, you guessed too low!" or "Sorry, you guessed too high!" depending on whether the number the user guessed was lower or higher than the correct one.
- [ ]  If the user guesses correctly, the program should print "Wohoo! You made it!"
- [ ]  If the user has guessed five (5) times and hasn't got the right number, the program should print "Sorry, you didn't manage to guess the number in five attempts!" and the user cannot guess anymore.
- [ ]  Some part of your code should be in its own function/method. For example, you can have a function to check if the guess is right or wrong called `CheckGuess()`

### Tips

To let the program randomly generate a number, you can use the code below. It will generate a random number between 1 and 20, which is stored in the variable `number`.

```csharp
Random random = new Random();
int number = random.Next(1,20);
```

### Examples

Below you'll find some examples of game rounds as they appeared in the console.

- Example 1
    
    ```
    Welcome! I'm thinking of a number. Can you guess which one? You get five attempts.
    2
    Sorry, you guessed too low!
    9
    Sorry, you guessed too high!
    7
    Sorry, you guessed too high!
    4
    Sorry, you guessed too high!
    5
    Sorry, you guessed too high!
    Sorry, you didn't manage to guess the number in five attempts!
    ```
    
- Example 2
    
    ```
    Welcome! I'm thinking of a number. Can you guess which one? You get five attempts.
    4
    Sorry, you guessed too high!
    2
    Wohoo! You made it!
    ```
    
- Example 3
    
    ```
    Welcome! I'm thinking of a number. Can you guess which one? You get five attempts.
    4
    Wohoo! You made it!
    ```
    

### Extra Challenge

Does the assignment feel too simple? Did you finish quickly?

Here are some ideas on how you can make the assignment a bit more advanced. Test as much as you want with these! Click on the arrows to read more.

- Choose difficulty level
    
    <aside>
    🤔 Let the game start by having the program ask about difficulty level. Either you can make it so that the user gets to choose different levels, for example by entering a number between 1 and 5, and then based on the answer, the game becomes differently difficult. Or maybe the user gets to enter how many numbers there should be to guess from.
    
    You can modify both how many numbers the program randomizes between and how many attempts the user should get. Easy level might be 10 numbers and 6 attempts. Medium level might be 25 numbers and 5 attempts. Hard level might be 50 numbers and 3 attempts.
    
    </aside>
    
- Variation in responses
    
    <aside>
    🤔 Isn't it boring that the program responds like a robot and says the same thing every time? Make it more fun!
    
    Come up with maybe four or five different variants of answers for example "Sorry, you guessed too high!". Maybe the program can answer "Haha! That was too high!" or "Good guess, but it was too high".
    
    Then let the program vary its responses. It should still tell if it's too high or low but with some variation in the language.
    
    </aside>
    
- It's getting hot!
    
    <aside>
    🤔 Make the responses to guesses a bit more adapted based on how close to the right number the user guesses!
    
    If the program is thinking of e.g. the number 7 and the user guesses 6, it can instead say "It's getting hot!" or "That was close!". But if the user guesses 2, the program can answer for example "Oh, that was far off".
    
    Here you can be creative and come up with several different types of responses based on how close or far from the number the user guesses.
    
    </aside>
    
- Restart the game
    
    <aside>
    🤔 As you notice, it's a bit boring that the game ends when you've guessed correctly or used all your attempts. Make it so you can restart the game without rerunning the program!
    
    A nice way could be that the game at the end asks something like "Do you want to play again?" and if the user writes "yes" the game restarts.
    
    </aside>
    

If you've done these challenges, you can submit this lab with these features included of course!

# Your Submission

- You submit the assignment in Canvas
- Submit a text file containing the link to a Github repo with your code

# Grading

This assignment is graded and is grade-foundational but upcoming assignments will test the same course objectives so you will be able to demonstrate greater understanding later in the course.

The assignment is graded with F or P and if you get F you need to complement the assignment by working further on it and completing it.

You cannot get VG on this assignment even though one of the objectives being tested has a VG level. This is because there is no VG component in the assignment and it will instead be tested in later assignments.

Below you can see the course objectives in the syllabus that are tested in this assignment.

[Untitled](https://www.notion.so/796be14d851247aa8f54d3f79cd86dc9?pvs=21)
