###Program Name: speed_test.py
###Programmer: Aaliyah Raderberg
###Project: Python Test Speed (internet)

##This script uses the speedtest-cli library to perform download
##and upload speed tests. It then displays the results in Mbps (megabits per second).
##You can run this script in your terminal to measure your internet connection speed.

##install it via pip: speedtest-cli 
#pip install speedtest-cli


import speedtest

def measure_speed():
    # Create Speedtest object
    st = speedtest.Speedtest()

    # Perform download speed test
    print("Performing download speed test...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps

    # Perform upload speed test
    print("Performing upload speed test...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps

    return download_speed, upload_speed

def main():
    # Measure speed
    download_speed, upload_speed = measure_speed()

    # Display results
    print("\nSpeed Test Results:")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    main()
