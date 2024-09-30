Feature: Leave Application Process
    Background: some requirement of this test
        Given I am on the login page
    
    @employeeleaverequest
    Scenario: Employee can apply for leave and HR can approve it
        Given I am logged in as an Employee
        When I navigate to "Leave Application"
        And I fill out the leave application form
        And I submit the application
        Then I should see a confirmation message
    
    @hrapproveleave
    Scenario: HR can approve leave
        Given I am logged in as HR
        When I navigate to "Leave Requests"
        And I search for leave request by employee name
        Then I approve the leave request
        Then I should see a confirmation message of leave status "Approved"
