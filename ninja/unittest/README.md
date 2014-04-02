# Formal unit testing

Python has a built-in `unittest` module and many developers who practice TDD (test-driven development) use them.

## Test-driven Development

[TDD](en.wikipedia.org/wiki/Test_driven_development) refers to the process of writing automated test cases, writing code that passes these tests, and refactoring the code to industry standard.

One of its core components is "test cases", which inherently points to unit tests (or end-to-end tests and behavioral tests, based on your development context).

## Why use unit tests?

There are many reasons why people use unit tests, and while I don't claim to know all of it, I'll list what I do know and have experienced first hand:

#### Edge cases

Remember that one problem on the mid-term that threw you off - `in_language()`? It involved `a`s followed by the same number of `b`s, and many of us forgot to check for cases like `abab`, which should have failed under our function. 

These are what many people call edge cases: cases that are outside the "meets-the-eye" scope of the problem. 

<dl>
    <dt>A more formal definition:</dt>
    <dd>"A problem or situation that occurs only at an extreme (maximum or minimum) operating parameter".</dd>
</dl>
Another edge case for the same `in_language` problem is empty string (`''`). Some common edge cases are:

- case of empty lists (`[]`) in sorting algorithms
- other edge cases that I can't think of right now...

#### Easy Integration

While this isn't the main use case for unit tests, I've seen it used where multiple developers for one project use test cases as references for what the inputs and the outputs of their functions and methods should be. 

Each test (when implemented correctly) shows a reader what the inputs and expected outputs are, which in turn makes it easy for one programmer to know exactly what the behavior of someone else's code should be. If you know how your code should interact with someone else's, it makes things a lot easier when you have to put it all together.

#### Refactoring

Having a system of unit tests can make refactoring codes extremely simple.

<dl>
    <dt>code refactoring</dt>
    <dd>the process of restructuring existing computer code - changing the factoring - without changing its external behavior</dd>
</dl>

As its definition says, we want to make the code more efficient and more up-to-standard without changing its outwardly behavior - its inputs and outputs should still be the same as before, and its interaction with other pieces of code should be consistent. This tends to be one of the hardest parts of refactoring code. Refactoring can very easily lead to unexpected changes in its output; having a unit test that keeps its functionality in line can be extremely handy.
