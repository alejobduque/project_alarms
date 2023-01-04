
CREATE TABLE public."alarm"
(
    id serial NOT NULL,
    alarm_name varchar(30) UNIQUE NOT NULL,
	comment varchar(40) NULL,
	start_date date NOT NULL,
	end_date date NULL,
	start_date_utc timestamptz,
	end_date_utc timestamptz,
	is_delete bool DEFAULT False,
    CONSTRAINT "pk_id" PRIMARY KEY (id)
);

CREATE OR REPLACE FUNCTION UPDATE_UTC() RETURNS TRIGGER AS $$
BEGIN
UPDATE public."alarm"
set start_date_utc = NEW.start_date_utc at time zone 'utc',
end_date_utc = NEW.end_date_utc at time zone 'utc'
where id = NEW.id;
RETURN NULL;
END;
$$ LANGUAGE PLPGSQL;

CREATE TRIGGER trigger_update_utc
AFTER INSERT ON public."alarm"
FOR EACH ROW EXECUTE FUNCTION public."update_utc"();

INSERT INTO public."alarm" (alarm_name, comment, start_date, end_date) VALUES
('Alarm1', 'Old', '15/01/2022', '15/02/2022'),
('Alarm2', NULL, '15/02/2022', '15/03/2022'),
('Alarm3', 'inside', '15/03/2022', '15/04/2022'),
('Alarm4', 'used', '15/04/2022', '15/05/2022'),
('Alarm5', 'New', '15/05/2022', '15/06/2022');


