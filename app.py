import platform 
import psutil 

print("Hello, World!")
print('The CPU usage is: ', psutil.cpu_percent(4))
print('RAM memory % used:', psutil.virtual_memory()[2])
