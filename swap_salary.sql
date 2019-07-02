UPDATE salary
SET sex = Case
When sex = 'm' Then 'f'
When sex = 'f' then 'm'
End
Where sex ='f' or sex ='m'
