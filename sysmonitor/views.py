from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import psutil
import platform
import cpuinfo
import datetime

# Create your views here.
def index(request):
    try:
        drivePath = "C:\\" if psutil.WINDOWS else "/"
        osName = platform.system()
        osVersion = platform.version()
        osRelease = platform.release()
        arch = platform.architecture()
        physCores = psutil.cpu_count(logical=False)
        logicalCores = psutil.cpu_count(logical=True)
        memory = psutil.virtual_memory()
        cpuUsage = psutil.cpu_percent()
        driveUsage = psutil.disk_usage(drivePath)
    except Exception as e:
        return HttpResponse("An error has occured: {e}")

    
    return render(request, 'sysmonitor/index.html', {
        'osName' : osName + " " + osRelease,
        'osVersion' : osVersion,
        'arch' : arch,
        'cpuUsage' : cpuUsage,
        'physCores' : physCores,
        'logicalCores' : logicalCores,
        'memory' : round(memory.total/1073741824, 2),
        'freeMem' : round(memory.free/1073741824, 2),
        'memUsage' : memory.percent,
        'totalStorage' : round(driveUsage.total/1073741824, 2),
        'freeStorage' : round(driveUsage.free/1073741824, 2),
        'driveUsage' : driveUsage.percent
    })

def updated_values(request):
    try:
        drivePath = "C:\\" if psutil.WINDOWS else "/"
        physCores = psutil.cpu_count(logical=False)
        logicalCores = psutil.cpu_count(logical=True)
        memory = psutil.virtual_memory()
        cpuUsage = psutil.cpu_percent()
        driveUsage = psutil.disk_usage(drivePath)
    except Exception as e:
        return HttpResponse("An error has occured: {e}")
    
    return JsonResponse({
        'cpuUsage' : cpuUsage,
        'physCores' : physCores,
        'logicalCores' : logicalCores,
        'memory' : round(memory.total/1024**3, 2),
        'usedMem' : round(memory.used/1024**3, 2),
        'freeMem' : round(memory.free/1024**3, 2),
        'memUsage' : memory.percent,
        'totalStorage' : round(driveUsage.total/1024**3, 2),
        'usedStorage' : round(driveUsage.used/1024**3, 2),
        'freeStorage' : round(driveUsage.free/1024**3, 2),
        'driveUsage' : driveUsage.percent
    })

def cpu_view(request):
    try:
        cpu_vendor = platform.processor()
        cpu_info = cpuinfo.get_cpu_info()
        phys_cores = psutil.cpu_count(logical=False)
        logical_cores = psutil.cpu_count(logical=True)
        frequency = psutil.cpu_freq()
        cpu_usage = psutil.cpu_percent()
        img_url = ""

        if "AMD" in cpu_info or "AMD" in cpu_vendor:
            img_url = "https://www.svgrepo.com/show/329916/amd.svg"
        elif "Intel" in cpu_info or 'Intel' in cpu_vendor:
            img_url = "https://www.svgrepo.com/show/473665/intel.svg"
        
    except Exception as e:
        return HttpResponse("An error has occured: {e}")
    
    return render(request, "sysmonitor/cpu.html", {
        'cpu_name' : cpu_info["brand_raw"],
        'cpu_vendor' : cpu_vendor,
        'phys_cores' : phys_cores,
        'logical_cores' : logical_cores,
        'frequency' : round(frequency.max/1000, 2),
        'current_usage' : cpu_usage,
        'img_url' : img_url
    })

def ram_view(request):
    try:
        memory = psutil.virtual_memory()
    except Exception as e:
        return HttpResponse("An error has occured: {e}")
    
    return render(request, "sysmonitor/ram.html", {
        'memory' : round(memory.total/1024**3, 2),
        'used_memory' : round(memory.used/1024**3, 2),
        'free_memory' : round(memory.free/1024**3, 2),
        'memory_usage' : memory.percent
    })

def drives_view(request):
    try:
        drive_path = "C:\\" if psutil.WINDOWS else "/"
        drive_usage = psutil.disk_usage(drive_path)
        drives = psutil.disk_partitions()
        drive = None

        for d in drives:
            if d.mountpoint == drive_path:
                drive = d

    except Exception as e:
        return HttpResponse("An error has occured: {e}")
    
    return render(request, "sysmonitor/drives.html", {
        'name' : drive.device,
        'mountpoint' : drive.mountpoint,
        'filesystem' : drive.fstype,
        'total_storage' : round(drive_usage.total/1024**3, 2),
        'used_storage' : round(drive_usage.used/1024**3, 2),
        'free_storage' : round(drive_usage.free/1024**3, 2),
        'drive_usage' : drive_usage.percent
    })

def sys_view(request):
    try:
        os_name = platform.system()
        os_version = platform.version()
        os_release = platform.release()
        arch = platform.architecture()
        img_url = ""
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())

        if os_name == 'Windows':
            if os_release == '11':
                img_url = "https://www.svgrepo.com/show/444174/os-windows-7.svg"
            elif os_release == '10' or os_release == '8' or os_release == '8.1':
                img_url = "https://www.svgrepo.com/show/508879/os-win-04.svg"
            else:
                img_url = "https://www.svgrepo.com/show/508880/os-win-03.svg"
        elif os_name == 'Linux':
            img_url = "https://www.svgrepo.com/show/444160/os-linux.svg"
        elif os_name == 'Darwin':
            img_url = "https://www.svgrepo.com/show/444156/os-apple.svg"

    except Exception as e:
        return HttpResponse("An error has occured: {e}")
    
    return render(request, "sysmonitor/sys.html", {
        'img_url' : img_url,
        'os_name' : os_name + " " + os_release,
        'os_version' : os_version,
        'arch' : arch,
        'boot_time' : boot_time
    })