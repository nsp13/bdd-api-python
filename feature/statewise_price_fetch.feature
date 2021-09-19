Feature: Price Fetch Check

Scenario: Fetch State wise Car Price
  Given Create the header & url based on appointment id
  When Perform the get call on price fetch api
  Then Validate the status code & price