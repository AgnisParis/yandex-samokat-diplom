SELECT track,
	CASE
		WHEN finished = true THEN 2
		WHEN cancelled = true THEN -1
		WHEN "inDelivery" = true THEN 1
		ELSE 0 
	END
FROM "Orders"
ORDER BY track;