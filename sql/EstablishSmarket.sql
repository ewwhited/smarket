create table smarket (
	Yr varchar(4),
	Lag1 numeric(4,3),
	Lag2 numeric(4,3),
	Lag3 numeric(4,3),
	Lag4 numeric(4,3),
	Lag5 numeric(4,3),
	Volume numeric(5,4),
	Today numeric(4,3),
	Direction varchar(4),
	Probability numeric(1,0)
	)


bulk insert smarket
    from 'C:\Users\Evan\Desktop\smarket\Smarket_new.csv'
    with
    (
    firstrow = 2,
    fieldterminator = ',',
	rowterminator = '\n'
    )

select * from smarket