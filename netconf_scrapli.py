# https://gitlab.com/networklessons-content/network-automation-orchestration/-/blob/master/netconf/netconf-delete-config-loopback.py

from scrapli_netconf.driver import NetconfScrape
import logging
import xmltodict
import xml.dom.minidom

logging.basicConfig(filename="scrapli.log", level=logging.INFO)
logger = logging.getLogger("scrapli")

my_device = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "auth_username": "developer",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
    "port": 830,
    # "port": 22,
    "transport": "system"
}

descr = "Network Interface"
ip_addr='192.168.1.1'
netmask_addr='255.255.255.0'
name='GigabitEthernet3'
# template = f"""
#   <config>
#     <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
#       <interface>
#         <name>{name}</name>
#         <description>{descr}</description>
#         <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
#         <enabled>true</enabled>
#         <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
#           <address operation="delete">
#             <ip>{ip_addr}</ip>
#             <netmask>{netmask_addr}</netmask>
#           </address>
#         </ipv4>
#         <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
#       </interface>
#     </interfaces>
#   </config>
# """

template = f"""
  <config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
        <name>{name}</name>
        <description>{descr}</description>
        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
        <enabled>true</enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
          <address>
            <ip>{ip_addr}</ip>
            <netmask>{netmask_addr}</netmask>
          </address>
        </ipv4>
        <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
      </interface>
    </interfaces>
  </config>
"""

# conn = NetconfScrape(**my_device)
# conn.open()
# result = conn.edit_config(config=template, target="running")
# print(result.result)

filter_ = """
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
        <name>GigabitEthernet3</name>
    </interface>
  </interfaces>
"""

conn = NetconfScrape(**my_device)
conn.open()
response = conn.get(filter_=filter_, filter_type="subtree")
print(response.result)

# template = f"""
#   <config>
#     <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
#       <interface>
#         <name>{name}</name>
#         <description>{descr}</description>
#         <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
#         <enabled>true</enabled>
#         <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
#           <address operation="delete">
#             <ip>{ip_addr}</ip>
#             <netmask>{netmask_addr}</netmask>
#           </address>
#         </ipv4>
#         <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
#       </interface>
#     </interfaces>
#   </config>
# """
#
# conn = NetconfScrape(**my_device)
# conn.open()
# result = conn.edit_config(config=template, target="running")
# print(result.result)


# conn = NetconfScrape(**my_device)
# conn.open()
# result = conn.rpc(filter_=commit_filter)
# print(result.result)

#
# filter_ = """
# <components xmlns="http://openconfig.net/yang/platform">
#     <component>
#         <state>
#         </state>
#     </component>
# </components>"""
#
# conn = NetconfScrape(**my_device)
# conn.open()
# response = conn.get(filter_=filter_, filter_type="subtree").result
# interface_python = xmltodict.parse(response)['rpc-reply']['data']["interfaces-state"]["interface"]
# # print(interface_python)
# # print(json.dumps(interface_python, indent=2, sort_keys=True))
# # x = interface_python.json()
# for i in interface_python:
#     print(f"{i['name']}")
#     print(f"         in-unicast-pkts: {i['statistics']['in-unicast-pkts']}")
#     print(f"         out-unicast-pkts:{i['statistics']['out-unicast-pkts']}")
# print(response.result)

# conn = NetconfScrape(**my_device)
# conn.open()
# result = conn.rpc(filter_=commit_filter)
# print(result.result)

# filter_ = """
# <components xmlns="http://openconfig.net/yang/platform">
#     <component>
#         <state>
#         </state>
#     </component>
# </components>"""
#
# conn = NetconfScrape(**my_device)
# conn.open()
# response = conn.get(filter_=filter_, filter_type="subtree")
# print(response.result)