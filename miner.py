import random
import datetime
import time


init_msg="ETH: 1 pool is specified\nMain Ethereum pool is eth.coinmine.pl:4000\n\nFPGA initializing...\n\nFPGA Cards available: 1\n"
init2_msg="POOL/SOLO version\nFPGA #0: algorithm ASM\nTotal cards: 1\nETH: Stratum - connecting to 'eth.coinmine.pl' <5.196.90.173> port 4000\nETHEREUM-ONLY MINING MODE ENABLED (-mode 1)\nETH: eth-proxy stratum mode\n\nWatchdog enabled\nRemote management is enabled on port 3333\n\nETH: Stratum - Connected (eth.coinmine.pl:4000)\nETH: Authorized\nSetting DAG epoch #191...\nSetting DAG epoch #191 for FPGA0 done\n"
print(init_msg)
print(init2_msg)



new_job=" - New job from eth.coinmine.pl:4000\n"
speed = 1000 + random.randint(255,420)
total_speed1= "ETH - Total Speed: "
total_speed2= " Gh/s, Total Shares: 0, Rejected: 0, Time:"
speed_fpga0 = "ETH: FPGA0 " 


share_found = " - SHARE FOUND - (FPGA0)\n"
share_acc= "ETH: Share accepted ("

total_time = 0

while (1):
    now = datetime.datetime.now()
    string_st = "ETH: " + str(now.strftime("%m/%d/%Y %H:%M:%S"))
    speed = str(1000 + random.randint(255,420))
    fan = "FPGA0 t=" + str(50 + random.randint(0,9)) + "C fan=" + str(66 + random.randint(0,9)) + "%"
    timeout = random.randint(1,5)
    total_time = total_time + timeout

    print(string_st + new_job)
    print(total_speed1 + speed + total_speed2 + str(round(total_time/60,0)) + ":" + str(total_time % 60) + " \n")
    print(speed_fpga0 + speed + " Mh/s\n")

    report_share_generator = random.randint(0,10)
    
    if report_share_generator < 8:
	print(string_st + share_found)
	print(share_acc + str(30 + random.randint(3,33)) +" ms)! \n")

    time.sleep(timeout)

