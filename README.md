# application_review_sys
A system to review job applications having api endpoints to create, retrieve, update, delete and list the information of an applicant.
It also have a feature to mark applicants Selected or rejected.

it has functionality to upload resumes of the applicant along with rest of the info.
it allows filtering and pagination in the applicant listing api.

## API end-points

### http://127.0.0.1:8000/core/applicant/?search={something}&ordering={some field eg name}&{some field}={some value}
GET to get a list of applicants also support filtering,ordering,searching
### http://127.0.0.1:8000/core/applicant/
POST to create a new profile of new applicant

### http://127.0.0.1:8000/core/applicant/{int:id}
GET to Retrieve only aplication with given id
PUT to Update the aplication with given id
DELETE to Delete the application of applicant with the given id
