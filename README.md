# scraper

## Assumption
    * I've made the following assumption to parse uid & job title
    - uid is always in <a> tag
    - uid always follows the format href="/en/jobs/...uid..."
    - title is always in <div> tag
    - title comes with the class 'job-card-title'
    
## Consideration 
    - Keep it simple & Maintain the agility (simple structure + config)
    - TDD using docker

## How to Run
    ```
    docker-compose run --rm start_dependencies
    docker-compose up scraper
    ```