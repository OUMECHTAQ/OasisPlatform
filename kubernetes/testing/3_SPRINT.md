Sprint 3 - Keycloak
===================

Testing for https://github.com/OasisLMF/OasisPlatform/pull/553

# Test cases

## Backwards compatibility

Using the original `SIMPLE_JWT` authentication model when running the platform via docker-compose. This is for testing compatibility with older usecases


| Test No  | Inputs | Expected result | Description  |
|---|:---|:---|:---|
| 1        | <ul><li> User `A` credentials </li><li> auth request </li></ul> | Successful user auth | Test token authentication |
| 2        | <ul><li> User `A` credentials </li><li> auth request </li><li> Wait for token timeout </li><li> auth request  </li></ul> | Token timeout error | test token timeout  |
| 3        | <ul><li> Admin Account </li><li> Create user request </li></ul> | New user `B` is created | Test that users can be created via the Django Admin Panel |
| 4        |  <ul><li> User `A` </li><li> Execute piwind workflow </li></ul>  | Basic piwind run is Successful | Check that a standard model execution works |
| 5        |  <ul><li> User `B` </li><li> request results from piwind run </li></ul> | User B is able to access results from User A's run | Test that results are accessible between accounts |


## Keycloak integration

Run the platform using the default kubernetes helm charts (via minikube), this should support keycloak authentication by default.

| Test No  | Inputs | Expected result | Description  |
|---|:---|:---|:---|
| 6       | <ul><li> User `A` credentials </li><li> auth request (OasisAPI) </li></ul> | Successful user auth | Test token authentication |
| 8       | <ul><li> User `A` credentials </li><li> auth request </li><li> Wait for token timeout </li><li> auth request  </li></ul> | Token timeout error | test token timeout  |
| 7       | <ul><li> User `A`  </li><li> Clear user session `A` (keycloak)  </li><li> auth request </li></ul> | User `A` access rejected | Check token is revoked |
| 8       | <ul><li> User `A`  </li><li> New Token request </li></ul> | New token returned | Check New token is issued |
| 9       | <ul><li> User `A` </li><li> Create/Upload portfolio </li></ul> | Successful portfolio upload | Test portfolio creation |
| 10      | <ul><li> User `A`  </li><li> revoking access (keycloak) </li><li> auth request  </li></ul> | User `A` access rejected | Check that users can be disabled |
| 11      | <ul><li> User `A`  </li><li> enable access (keycloak) </li><li> auth request  </li></ul> | User `A` access successful and `username_<keycloak-id>` is retained | Check that users can be enabled |
| 12      | <ul><li> User `B` </li><li> Create an analysis </li></ul>  | Successful analysis creation | Using the portfolio from step `9` create a new analysis |
| 13      | <ul><li> User `B`  </li><li> Delete user `B` (keycloak)  </li><li> auth request </li></ul> | User `B` access rejected | Check account access revoked |
| 14      | <ul><li> Create User `B` (keycloak)</li><li> New credentials </li><li> auth request (OasisAPI) </li></ul>  |  Successful user auth with new credentials |Check that updating credentials works on inactive user |
| 15      | <ul><li> Update User `B` (keycloak)</li><li> New credentials </li><li> auth request (OasisAPI) </li></ul>  |  Successful user auth | Check that updating credentials works on active user |

