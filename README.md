# ScrambledEggs
For people too lazy to mix their files

# But why?
I don't know either.

# Usage
File to be mixed:
```
Text
to
mix
--BREAK--
Another
text
to
mix
--BREAK--
```
Every line ending with newline will be mixed inside of a 'shell'.
Shells end with `--BREAK--`. This allows you to have multiple text to be mixed inside of one file.
Output file is saved as `output.txt` and stored in the same directory as `main.py`.

# Example
Input file:
```
Lorem
ipsum
dolor
sit
amet,
--BREAK--
consectetur
adipiscing
elit.
--BREAK--
```
`output.txt`:
```
dolor
ipsum
sit
amet,
Lorem
--BREAK--
consectetur
adipiscing
elit.
--BREAK--
```

# Dependencies
* Tkinter

I assume you have random in-built.