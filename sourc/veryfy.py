import os,platform,subprocess,psutil
def is_virtual_machine():
    try:
        model = ""
        if hasattr(psutil.users()[0], "host"):
            model = psutil.users()[0].host.lower()
        if os.path.exists("/proc/cpuinfo"):
            with open("/proc/cpuinfo") as f:
                cpuinfo = f.read().lower()
            if "hypervisor" in cpuinfo:
                return True
        if platform.system() == "Linux":
            try:
                output = subprocess.check_output(["systemd-detect-virt"]).strip().decode().lower()
                if output and output != "none":
                    return True
            except Exception:
                pass
            try:
                output = subprocess.check_output(["sudo", "dmidecode", "-s", "system-product-name"]).strip().decode().lower()
                if any(vm in output for vm in ["virtual", "vmware", "kvm", "qemu", "hyper-v", "xen"]):
                    return True
            except Exception:
                pass
        if platform.system() == "Windows":
            try:
                output = subprocess.check_output("wmic computersystem get model", shell=True).decode().lower()
                if any(vm in output for vm in ["virtual", "vmware", "kvm", "qemu", "hyper-v", "xen"]):
                    return True
            except Exception:
                pass
        if any(vm in model for vm in ["virtual", "vmware", "qemu", "hyper-v", "xen"]):
            return True
    except Exception:
        pass
    return False
