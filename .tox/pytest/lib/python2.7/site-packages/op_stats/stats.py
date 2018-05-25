#stats.py  
import psutil

class Stats():
  @classmethod
  def get_cpu_percent(cls):
    cpu_percent = psutil.cpu_percent()
    return cpu_percent

  @classmethod
  def get_ram(cls):
    ram_available = psutil.virtual_memory()[2]
    return ram_available

  @classmethod
  def get_disk(cls):
    disk_available = 100-psutil.disk_usage('/')[3]
    return disk_available
