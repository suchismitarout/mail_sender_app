Feature: Functional test cases of mail_sender application

  Scenario: Database has no username and password
    Given the server is running
      And the username and password are not in database
    When the user fills the username with username
       And the user fills the passwd with passwd
       And the user clicks login
    Then the user will get error


   Scenario: Database has username and password
     Given the server is running
      And the username and password are in database
    When the user fills the username with username
       And the user fills the passwd with passwd
       And the user clicks login
     Then the user will be logged in


    Scenario: User enters wrong username
      Given the server is running
        And the username and password are in database
      When the user fills the username with wrong username
       And the user fills the passwd with passwd
       And the user clicks login
      Then the user will get error


     Scenario: User enters wrong password
       Given the server is running
        And the username and password are in database
      When the user fills the username with username
       And the user fills the passwd with wrong passwd
       And the user clicks login
      Then the user will get error

      Scenario: User will redirect to mail_send page
        Given the server is running
      And the username and password are in database
    When the user fills the username with username
       And the user fills the passwd with passwd
       And the user clicks login
     Then the user will be logged in
       And the user redirects to mail_send page

      Scenario: User tries to send mail without recepient
        Given the server is running
      And the username and password are in database
     When the user fills the username with username
       And the user fills the passwd with passwd
       And the user clicks login
     Then the user will be logged in
       And the user redirects to mail_send page
     When the user clicks send
       And the user will get error

      Scenario: User tries to send mail with recepient
        Given the server is running
      And the username and password are in database
     When the user fills the username with username
       And the user fills the passwd with passwd
       And the user clicks login
     Then the user will be logged in
       And the user redirects to mail_send page
     When the user fills recepient
        And the user clicks send
      Then the user should redirect to success page

