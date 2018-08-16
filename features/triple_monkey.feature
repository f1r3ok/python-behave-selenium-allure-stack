Feature: Triple Monkey spin test
  In order to play Triple Monkey slot game,
  As a registered user
  I want to be able to make a spin

  Scenario: Make a spin
    Given the user opens Triple Monkey
     When user press Play button
     Then user get start balance
     Then user get total bet
     Then user send cheat
     Then user press Spin button
     Then user send cheat
     Then user press Spin button
     Then user get end balance
     Then user compares start and end balance
