from saram import saram_get_job as sa_job
from so import get_jobs as get_so_jobs
from save import save_to_file,save_to_files
sa=sa_job()
so_jobs=get_so_jobs()
jobs=sa+so_jobs
save_to_file(jobs)
save_to_files(so_jobs)

