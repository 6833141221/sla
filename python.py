import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)

departments = ['  Tech', 'Data Science  ', ' Marketing ', 'HR', 'Operations']
df_department = pd.DataFrame({
    'd_id': range(1, len(departments) + 1),
    'd_name': departments
})

job_titles = ['Data Analyst', 'Software Engineer', 'Recruiter', 'Accountant']
job_data = []
for i in range(1, 11):
    job_data.append({
        'job_id': 100 + i,
        'job_title': random.choice(job_titles),
        'job_type': random.choice(['Full-time', 'Intern  ']),
        'd_id': random.randint(1, len(departments)) 
    })
df_job = pd.DataFrame(job_data)

applicant_data = []
for i in range(1, 21):
    f_name, l_name = fake.first_name(), fake.last_name()
    applicant_data.append({
        'ssn': f'S-{1000+i}',
        'full_name': f"  {f_name}   {l_name}  ",
        'email': f"{f_name.lower()}@shopee.com "
    })
df_applicant = pd.DataFrame(applicant_data)

hr_data = []
for i in range(1, 6):
    hr_data.append({
        'hr_id': f'HR-{i:03}',
        'hr_name': fake.name(),
    })
df_hr = pd.DataFrame(hr_data)

application_data = []
status_data = []
for i in range(1, 16):
    app_id = f'APP-{500+i}'
    start_date = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 30))
    
    application_data.append({
        'app_id': app_id,
        'ssn': f'S-{1000 + random.randint(1, 20)}', # เชื่อมกับ Person
        'job_id': 100 + random.randint(1, 10),     # เชื่อมกับ Job
        'apply_date': start_date
    })
    
    stages = [('Applied', 0), ('Screening', 2), ('Interview', 5), ('Hired', 7)]
    stop_at = random.choices([1, 2, 3, 4], weights=[0.1, 0.2, 0.3, 0.4])[0]
    
    for j in range(stop_at):
        st_type, days = stages[j]
        random_hour = random.randint(8, 18)
        random_minute = random.randint(0, 59)
        random_second = random.randint(0, 59)
        
        status_time = start_date + timedelta(days=days, hours=random_hour, minutes=random_minute, seconds=random_second)
        
        status_data.append({
            'log_id': f'LOG-{random.randint(10000, 99999)}',
            'app_id': app_id,
            'status_type': st_type,
            'status_time': status_time
        })

df_application = pd.DataFrame(application_data)
df_status = pd.DataFrame(status_data)


itv_data = []
performs_data = []

for i, app in df_application.iterrows():
    itv_id = f'ITV-{900+i}'
    itv_data.append({
        'itv_id': itv_id,
        'itv_date': datetime(2024, 2, 1) + timedelta(days=random.randint(1, 20)),
        'app_id': app['app_id'] 
    })
    
    assigned_hr = random.sample(list(df_hr['hr_id']), k=random.randint(1, 2))
    
    for hr_id in assigned_hr:
        performs_data.append({
            'itv_id': itv_id,
            'hr_id': hr_id
        })

df_itv = pd.DataFrame(itv_data)
df_performs = pd.DataFrame(performs_data)

print("create all entity")

df_department.to_csv('dept.csv', index=False)
df_job.to_csv('job.csv', index=False)
df_applicant.to_csv('applicant.csv', index=False)
df_hr.to_csv('hr.csv', index=False)
df_application.to_csv('application.csv', index=False)
df_status.to_csv('status.csv', index=False)
df_itv.to_csv('interviews.csv', index=False)
df_performs.to_csv('performs.csv', index=False)

print("create file")
