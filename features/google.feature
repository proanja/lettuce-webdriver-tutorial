Feature: Go to google

Scenario: Visit Google
	Given I go to "http://www.google.com/"
	When I fill in field with class "gbqfif" with "agile thailand 2013"
	Then I should see "agile66.com" within 2 second
