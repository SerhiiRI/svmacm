def containerNameId(container_stats:dict) -> (int, int):
    return container_stats['name'][1:], container_stats['id']

def containerStatus(container_object) -> str:
    return container_object.status

def cpuPercentUsage(container_stats:dict) -> int:
    CPU_PERCENT = 0.0
    CPUTotalUsage     = float(container_stats['cpu_stats']   ['cpu_usage']       ['total_usage'])
    PreCPUTotalUsage  = float(container_stats['precpu_stats']['cpu_usage']       ['total_usage'])
    percpu_core_usage = len(  container_stats['cpu_stats']   ['cpu_usage']       ['percpu_usage'])
    SystemUsage       = float(container_stats['cpu_stats']   ['system_cpu_usage'])
    PreSystemUsage    = float(container_stats['precpu_stats']['system_cpu_usage'])

    cpuDelta          = CPUTotalUsage  - PreCPUTotalUsage
    systemDelta       = SystemUsage    - PreSystemUsage
    if systemDelta > 0.0 and cpuDelta > 0.0:
        CPU_PERCENT = (cpuDelta / systemDelta) \
                      * percpu_core_usage \
                      * 100.0
    return int(CPU_PERCENT)

def networkUsage(container_stats:dict, format:str, interface="eth0") -> (int, int):
    """
    By default this function print out to screen only memory
    on device eth0, as standard VM configuration
    :param container_stats: container status dictionary
    :param format: format of output MB, KB, B(default)
    :return: (tuple Receive Mem, Transceiver Mem)
    """
    rx = float(container_stats['networks'][interface]['rx_bytes'])
    tx = float(container_stats['networks'][interface]['tx_bytes'])

    if (format is "MB"): (rx, tx) = (rx / (1024 * 1024), tx / (1024 * 1024))
    if (format is "KB"): (rx, tx) = (rx / (1024)       , tx / (1024))
    return (int(rx), int(tx))

def memoryRAM(container_stats:dict) -> int:
    #MEM_PERCENT = 0.0
    maximum = float(container_stats["memory_stats"]["max_usage"])
    used    = float(container_stats["memory_stats"]["usage"])
    return int(used / maximum * 100)

def imageNameTag(container_obj) -> (str, str):
    try:
        image, tag = container_obj.image.tags[0].split(":")
    except Exception:
        image, tag = container_obj.image.tags[0], "-"
    return image, tag
