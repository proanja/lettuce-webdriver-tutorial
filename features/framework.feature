Feature: Go to framework

Scenario: Check Phoenix Header
	Given I go to "http://framework.prontomarketing.com"
	Then The element with id of "header" contains "Home"
	And I should see class "navbar" of element "header" id "header"
	And I should see the selector "div.navbar" has css attribute "overflow" value "visible"