# Models
## Profile
- `OneToOneField` with `User`
- score    
- level  
## Questions
- image_link
- question_text
- cert_text
- id
- no_count
- yes_count
- not_sure_count
- count
- final_answer
### tips of Question class: 	
- not sure is not considered
- priority with the most viewed question
# QuestionUser:
- user  
- question  
- answer: No:0  Yes:1   Not Sure: 2 
	
# URLs
## Base URL:    `/api`

### `/<app_name>`  
1.`/app1`   
2.`/app2`   
3.`/app3`   
4.`/app4`   
5.`/app5`   
6.`/app6`  

---
### `/user`    
1.`/login`      
2.`/logout`         
3.`/register`    
4.`/status` 

