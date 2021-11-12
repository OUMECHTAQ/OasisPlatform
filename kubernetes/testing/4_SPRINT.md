

## Compatibility checks
* executure a basic piwind model run in docker-compose mode without using keyclock


## Access control checks

Create the following groups:
* `1_inclusive`,
* `2_inclusive`,
* `3_shared`,
* `4_revoked`
* `5_exclusive`,

Create the following users connected to the groups
* Admin
* open_user  ( n/a )
* 1_user  (`1_inclusive`)
* 2_user  (`2_inclusive`, `3_shared`)
* 3_user  (`3_shared`)
* 4_user  (`4_revoked`)


Create the following models connected to groups
* open_piwind ( n/a )
* 1_piwind (`1_inclusive`)
* 2_piwind (`2_inclusive`)
* 3_piwind (`3_shared`)
* 4_piwind (`5_exclusive`, `4_revoked`)


Create 1 portfolio per user
* open_portfolio  (`open_user`)
* 1_portfolio  (`1_user`)
* 2_portfolio  (`2_user`)
* 3_portfolio  (`3_user`)
* 4_portfolio  (`4_user`)
* 5_portfolio  (`admin`)

## Test each perfective

### (Admin)
- The admin account can view and access everything
- Add admin to `5_exclusive` group so it exisits In the Django DB
- for each portfolio, check that the groups have defaulted to the correct group values per user


### (open_user)
- Can see models (`open_piwind`)
- Can see portfolios (`open_portfolio`)
- Can create/exec an analysis  `open_analysis` = (`open_piwind` + `open_portfolio`)

### (1_user)
- Can see models (`open_piwind`, `1_piwind`)
- Can see portfolios (`open_portfolio`, `1_portfolio`)
- Can see and exec `open_analysis`
- Create/exec `1_analysis` = (`1_piwind` + `1_portfolio`)

### (2_user)
- Can see models (`open_piwind`, `2_piwind`, `3_piwind`)
- Can see portfolios (`open_portfolio`, `2_portfolio`, `3_portfolio`)
- Can see and exec `open_analysis`
- Cannot see, exec or access files from `1_analysis`
- Is able to create `3_analysis` = (`3_piwind` + `3_portfolio`)
- Is able to create `4_analysis` = (`2_piwind` + `3_portfolio`)
- User can edit `2_portfolio` to remove/add the `2_inclusive` group

### (3_user)
- Can see models (`open_piwind`, `3_piwind`)
- Can see portfolios (`open_portfolio` `2_portfolio`, `3_portfolio`,
- Can see but not exec `4_analysis`
- Can see and exec `3_analysis`

### (4_user)
- Can see models (`open_piwind`, `4_piwind`)
- Can see portfolios (`open_portfolio`, `4_portfolio`)
- Can create `5_analysis` = (`4_piwind` + `4_portfolio`)
- Can exec `5_analysis`
- Use admin account to remove `4_revoked` from this user
- Use admin account to delete the open objects
- User cannot access any models, portfolios or analysis


### to do 
- Test data file adding / Access 
- Test file linking between portfilios / analysis copy
