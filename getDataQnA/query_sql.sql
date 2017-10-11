-- SELECT dataTrain.QnA.cat_ID , dataTrain.Category.catName 
-- FROM dataTrain.QnA , dataTrain.Category 
-- where dataTrain.QnA.cat_ID = dataTrain.Category.catId 

SELECT dataTrain.QnA.title ,dataTrain.QnA.cat_ID , dataTrain.Category.catName 
FROM dataTrain.QnA , dataTrain.Category 
where dataTrain.QnA.cat_ID = dataTrain.Category.catId ;

select dataTrain.QnA.cat_ID, dataTrain.QnA.qnaId,dataTrain.QnA.title ,dataTrain.Category.catName
from  dataTrain.QnA , dataTrain.Category 
where dataTrain.QnA.cat_ID = dataTrain.Category.catId ;

-- select dataTrain.QnA.cat_ID,dataTrain.QnA.qnaId,dataTrain.QnA.title
-- from dataTrain.QnA
select   COUNT(dataTrain.QnA.qnaId) ,dataTrain.QnA.qnaId
from dataTrain.QnA
where dataTrain.QnA.qnaId 
group by  dataTrain.QnA.qnaId 
HAVING COUNT(dataTrain.QnA.qnaId) > 1;


select dataTrain.QnA.cat_ID,dataTrain.QnA.qnaId,dataTrain.QnA.title,dataTrain.QnA.shortAnswer,dataTrain.QnA.answer
from dataTrain.QnA
where dataTrain.QnA.qnaId = 101699;

select dataTrain.QnA.answer
from dataTrain.QnA;

select  dataTrain.QnA.qnaId, dataTrain.QnA.title, dataTrain.QnA.shortAnswer  , dataTrain.QnA.cat_ID 
from dataTrain.QnA ;


select count(dataTrain.QnA.title) from dataTrain.QnA;

select  dataTrain.QnA.cat_ID ,dataTrain.Category.catName
from dataTrain.QnA , dataTrain.Category;

select  dataTrain.QnA.cat_ID, dataTrain.QnA.title ,dataTrain.Diseases.cat_Name
from dataTrain.QnA , dataTrain.Diseases
where dataTrain.QnA.cat_ID = dataTrain.Diseases.cat_ID;

select dataTrain.QnA.id dataTrain.QnA.qnaId, dataTrain.QnA.title , dataTrain.QnA.shortAnswer from dataTrain.QnA;

