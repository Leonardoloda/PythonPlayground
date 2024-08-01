MENU_TEMPLATE = """
    <h1>Welcome to higher or lower!</h1>
    
    <p>Please choose a number</p>
    
    <ol>
        {options}
    </ol>
"""

GUESSING_OPTION = """
        <li> <a href="/guess/1">One</a> </li>
        <li> <a href="/guess/2">Two</a> </li>
        <li> <a href="/guess/3">Three</a> </li>
        <li> <a href="/guess/4">Four</a> </li>
        <li> <a href="/guess/5">Five</a> </li>
        <li> <a href="/guess/6">Six</a> </li>
        <li> <a href="/guess/7">Seven</a> </li>
        <li> <a href="/guess/8">Eight</a> </li>
        <li> <a href="/guess/9">Nine</a> </li>
"""

HIGHER_GUESS_MESSAGE = "<p>You guessed higher than the number!</p>"

LOWER_GUESS_MESSAGE = "<p>You guessed lower than the number!</p>"

RIGHT_GUESS_MESSAGE = "<p>You guessed the right number!</p>"

RESULTS_SCREEN = """
    {message}
    
    <p>Thanks for playing!</p>
    
    <a href="/">Start a new game</a>
"""
