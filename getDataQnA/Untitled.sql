SELECT * FROM dataTrain.Diseases;
SELECT dataTrain.QnA.cat_ID , dataTrain.QnA.title
 FROM dataTrain.QnA 
 where dataTrain.QnA.cat_ID = 215;

select  dataTrain.QnA.title , dataTrain.Diseases.cat_Name,dataTrain.Diseases.cat_ID,dataTrain.QnA.cat_ID
from dataTrain.QnA, dataTrain.Diseases
where dataTrain.QnA.cat_ID != dataTrain.Diseases.cat_ID;
