CREATE TABLE SQLUser.usa_housing_train (
	id BIGINT NOT NULL,
	AvgAreaIncome DOUBLE,
	AvgAreaHouseAge DOUBLE,
	AvgAreaRooms DOUBLE,
	AvgAreaBedRooms DOUBLE,
	AreaPopulation DOUBLE,
	Price DOUBLE,
	CONSTRAINT USA_HOUSING_TRAIN_PKEY1 PRIMARY KEY (id)
)
GO
CREATE TABLE SQLUser.usa_housing_validate (
	id BIGINT NOT NULL,
	AvgAreaIncome DOUBLE,
	AvgAreaHouseAge DOUBLE,
	AvgAreaRooms DOUBLE,
	AvgAreaBedRooms DOUBLE,
	AreaPopulation DOUBLE,
	Price DOUBLE,
	CONSTRAINT USA_HOUSING_TRAIN_PKEY1 PRIMARY KEY (id)
)
GO