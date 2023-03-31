# comma-code
This is my solution to the Comma Code project assignment from Chapter 4: Lists of "Automate the Boring Stuff with Python."

<p>The program allows a user to enter as many words as they would like. Each word is added to a list.<br>
The user can stop entering words by entering a blank space. This will then call the function.<br>
The function takes the list of words and creates a string with comma separation and the word 'and' before the last word.</p>

### Example
<p><b>Input:</b><br>
  cat<br>
  bat<br>
  frog<br>
  dog<br>
  
<b>Generated List:</b> ['cat', 'bat', 'frog', 'dog']<br>
<b>Output String:</b> 'Your list: cat, bat, frog and dog'</p>

### Input Validation
Prevents the following situations:
 <ul> <li>an empty list [ ]</li>
  <li>a one item list ['cat']</li>
  <li>more than one word with spaces entered at once</li>
  <li>numbers or symbols being entered instead of a word</li>
</ul>
