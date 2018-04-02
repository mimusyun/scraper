# scraper

## Assumption
    * I've made the following assumption to parse uid & job title
    - uid is always in <a> tag
    - uid always follows the format href="/en/jobs/...uid..."
    - title is always in <div> tag
    - title comes with the class 'job-card-title'
    
## Consideration 
    - Keep it simple & Maintain the agility 
    (simple structure / configurable)
    - TDD using docker
    - Less Assumptions as much as possible when scraping data

## How to Run
    ```
    docker-compose run --rm start_dependencies
    docker-compose up scraper
    ```
    
## Expected Result
    ```
     id |                 uid                  |                                    
                               title                                                           
    ----+--------------------------------------+------------------------------------
    --------------------------------------------------------------------------------
    ------------------------

    1 | b8e936de-f06c-41aa-ad38-d394f58d56b8 | Kundenbetreuer / Kundenberater / Mi
    tarbeiter Backoffice (m/w) im Kundenservice in Vollzeit/ Teilzeit (auch Quereins
    teiger)
    2 | a9a49d9f-10ce-4be0-a44c-20d3d9d8271b | Teamleiter Kundenberatung / Projekt
    leiter / Key Account Manager (m/w/d) in Vollzeit/ Teilzeit
    3 | 94a068e2-5460-4ef1-afca-90a3cf583a1a | Customer Care Agent/ Kundenbetreuer
    / Kundenservice (w/m/d) in Vollzeit (auch Quereinsteiger)
    ...
    ...
    ```
    
    ```
     count 
    -------
        20
    (1 row)

    ```
        

    
    