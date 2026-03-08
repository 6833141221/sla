create table applicant(
	ssn text primary key,
	full_name text not null,
	email text not null
);

create table department(
	d_id int primary key,
	d_name text not null
);

create table hr(
	hr_id text primary key,
	hr_name text not null
);

create table job(
	job_id int primary key,
	job_title text not null,
	job_type text not null,
	d_id int not null,

	constraint fk_job foreign key(d_id) references department(d_id)
);

create table application(
	app_id text primary key,
	ssn text not null,
	job_id int not null,
	apply_date date not null,

	constraint fk_application_ssn foreign key(ssn) references applicant(ssn) on delete cascade,
	constraint fk_application_job foreign key(job_id) references job(job_id) on delete cascade
);

create table status(
	log_id text primary key,
	app_id text not null,
	status_type text not null,
	status_time timestamp,

	constraint fk_status foreign key(app_id) references application(app_id) on delete cascade
);

create table interviews(
	itv_id text primary key,
	itv_date date not null,
	app_id text not null,

	constraint fk_interviews foreign key(app_id) references application(app_id) on delete cascade
);

create table performs(
	itv_id text not null,
	hr_id text not null,
	primary key(itv_id,hr_id)
);




//สร้างตารางส่วนนี้เพื่อให้ง่ายต่อการ SLA

WITH RawDates AS (
	select
        a.app_id,
        p.full_name AS candidate_name,
        d.d_name AS department,
        j.job_title,
        a.apply_date,
        MAX(CASE WHEN s.status_type = 'Screening' THEN s.status_time END) AS screening_date,
        MAX(CASE WHEN s.status_type = 'Interview' THEN s.status_time END) AS interview_date,
        MAX(CASE WHEN s.status_type = 'Hired' THEN s.status_time END) AS hired_date
    FROM application a
    JOIN applicant p ON a.ssn = p.ssn
    JOIN job j ON a.job_id = j.job_id
    JOIN department d ON j.d_id = d.d_id
    LEFT JOIN status s ON a.app_id = s.app_id
    GROUP BY a.app_id, p.full_name, d.d_name, j.job_title, a.apply_date
)
SELECT 
    *,
    DATE_PART('day', screening_date - apply_date) AS sla_apply_to_screen,
    DATE_PART('day', interview_date - screening_date) AS sla_screen_to_interview,
    DATE_PART('day', hired_date - apply_date) AS total_time_to_hire
FROM RawDates;