from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir()


result = nr.run(
        task=netmiko_send_command,
        command_string="show version"
)

print_result(result)