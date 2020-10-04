# coding-challenge-python
A coding challenge used to assess developers knowledge and skills.
Completed by Roland Kajatin.

## Scenario
A developer has tried to do a task that you must now take over and complete.
The task has been extended with additional requirements after the developer left.
You should use best practices in order to make the code easy to understand, maintain and extend.

The API mock must not be changed and must be used.

### Requirements
- It must be possible to run the program and get back the colors green, blue and red in HEX format.
- It must be possible to define the colors using their names like red, blue and green.
- It must be possible to define the order the colors are returned.
##### Additional requirements
- The program must also support the colors white and black.
- The program must also return the RGB values.

## Solution
The solution to the requirements is given in an elegant way, using only one positional argument.
For example, to get information about the colors red, blue, and white (in this order) you can type:

```
python colors.py red blue white
```

The solution ignores colors that are not supported by the API.
Currently supported colors by the API are: red, green, blue, black, and white.
If the API is extended with a new color, the solution supports it out-of-the-box, without requiring any changes to the code.