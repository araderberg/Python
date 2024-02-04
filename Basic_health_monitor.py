###Program Name: Basic_health_monitor.py
###Programmer: Aaliyah Raderberg
###Description: System Health Monitor

import psutil
import time
import logging

def monitor_system_health():
    """Monitors system health metrics and logs them periodically."""

    logging.basicConfig(filename='system_health.log', level=logging.INFO)

    while True:
        try:
            # Get system metrics
            cpu_usage = psutil.cpu_percent()
            memory_usage = psutil.virtual_memory().percent
            disk_usage = psutil.disk_usage("/").percent
            network_io = psutil.net_io_counters()

            # Format metrics into a clear message
            message = f"CPU Usage: {cpu_usage:.2f}%\n" \
                      f"Memory Usage: {memory_usage:.2f}%\n" \
                      f"Disk Usage: {disk_usage:.2f}%\n" \
                      f"Network Sent: {network_io.bytes_sent} bytes\n" \
                      f"Network Received: {network_io.bytes_recv} bytes"

            # Log the message
            logging.info(message)

            # Check for potential issues and trigger alerts
            if cpu_usage > 90:
                logging.warning("High CPU usage detected!")
            if memory_usage > 90:
                logging.warning("High memory usage detected!")
            if disk_usage > 90:
                logging.warning("Low disk space remaining!")

            # Adjust the monitoring interval as needed
            time.sleep(60)  # Check every minute

        except Exception as e:
            logging.error(f"Error during system health check: {e}")

if __name__ == "__main__":
    monitor_system_health()
