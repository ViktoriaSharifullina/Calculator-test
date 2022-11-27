Feature: Calculator
 	As an author of this article
 	I want to demonstrate
 	How to write a simple test using behave
 		with a calculator as an example

	Scenario Outline: Arithmetic operations with integers

        Given I have entered <number1> into the calculator
        And I have also entered <number2> into the calculator
        When I press <action>
        Then the <result> should be on the screen

        Examples:

            |  number1|  number2|   result|  action|
            |        5|        2|        7|    plus|
            |       -4|        8|        4|    plus|
            |      100|      200|      300|    plus|
            |      100|      -70|      170|   minus|
            |        8|        2|        6|   minus|
            |        4|       -1|        5|   minus|
            |        4|       -2|       -8|multiply|
            |        4|        2|        8|multiply|
            |        4|        2|        2|division|
            |        5|        5|        1|division|


    Scenario Outline: Arithmetic operations with floats

        Given I have entered <number1> into the calculator
        And I have also entered <number2> into the calculator
        When I press <action>
        Then the <result> should be on the screen

        Examples:

            |  number1|  number2|   result|  action|
            |      5.1|      2.4|      7.5|    plus|
            |     10.1|      4.0|      6.1|   minus|
            |      4.5|      2.0|      9.0|multiply|
            |      4.5|      0.5|      9.0|division|