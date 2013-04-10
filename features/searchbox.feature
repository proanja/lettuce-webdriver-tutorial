Feature: Websites should have correct layout
  	In order to make my site look professionally
  	As a site owner
  	I want to have the website that has correct layout

	Scenario: Each site should have correct CSS in search box
	Given I have the following data for css selector "div.widget_search":
	  | name     							| attribute_name 	| attribute_value 	|
	  | http://www.alexssa.com/    			| width       		| 166px     		|
	  | http://www.mis-solutions.com/   	| margin-top       	| 0px     			|
	  | http://www.allaccessinfotech.com/  	| position      	| absolute    		|
	  | http://www.castema.com/  			| width      		| 166px    		 	|
	  | http://www.ceigroup.com/  			| width      		| 166px    		 	|
	  | http://www.workwithcss.com/ 		| margin-top      	| 0px    		 	|
	  | http://www.drivencomputers.com/ 	| padding-right     | 8px    		 	|
	  | http://www.esudo.com/ 				| height	     	| 30px    		 	|
	  | http://www.gosilverpoint.com/		| width		      	| 175px    		 	|
	  | http://www.hireanitexpert.com/ 		| width		      	| 580px    		 	|