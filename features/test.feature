Feature: The dealer for the game of 21
  Scenario: Deal initial cards
    When the round starts

  Scenario Outline: Get hand total
  Given a <hand>
  Then the <total> is correct

  Examples: Hands
  | hand | total |
  | 5,7  | 12    |
  | 6    | 15    |