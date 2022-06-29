# 0x07. Networking basics #0

### OSI Model
#### What is it?
Open System Interconnection (OSI) is a layered newtwork and conceptual model that describes the universal standard of communication functions of telecommunication system or cumputing system.
#### How many layers it has
To help understand (and design) networks, the International Standars Organization (ISO) has developed a **seven-layer model** for newtworks known as Open System Interconnection (OSI).
#### How it is organized
7 layers of the OSI model
- Layer 7. The application layer
Enable the user to interact with the application or network whenever the user elects to read messages, transfer files or perform other network-related task.

- Layer 6. The presentation layer
Translates or formats data for the application layer based on the semantisc or syntax the application accepts. This layer also handles the encryption and decryption that the application layer requies.

- Layer 5. The session layer
Sets up, coordinates and terminates conversation between applications. Its services include authentication and reconnection after an interruption. 

- Layer 4. The transport layer
Is responsable for transferring data across a network and provides error-checking mechanisms and data flow controls. It determines how much data to send, where it gets sent and at what rate.

- Layer 3. The network layer
The primary function is to move data into and though other networks. Its protocols accomplish this by packaging data with correct network address information.

- Layer 2. The data-link layer
Also known as "protocol layer", handles moving data into and out of a physical link in a network, also handle problems that occur as a result of bit transmission errors.  

- Layer 1. The physical layer
Transports data using electrical, mechanical or procedural interfaces. is responsible for sendig computer bits from one device to another along the network.

### What is a LAN
It means Local Area Network (LAN)
#### Typical usage
connects nwtwork devices over a relatively short distance. In TCP/IP networking a LAN is often implemented as a single IP subnet.
#### Typical geogrdaphical size

### What is the internet
Is the global system of interconnected computer networks that uses the Internet protocol suice (TCP/IP) to communicate between networks and devices. It is a network of networks that consists of private, public, academic, business and government networks of local to global scope.
#### What is an IP address
Is a **unique** address that identifies a device on the internet or local network. IP stands for *Internet Protocol*. IP addresses indentify computers and devices and lets them communicate with each other.

#### What are the 2 types of IP address
- Static IP address:
Is an address that doesn't change. Once your device is assigned a static IP address, that number typically stats the same until the device is decommissioned or your network architecture change.

Static IP addresses are assigned by Internet Service Providers (ISPs).

A static IP address may be IPv4 or IPv6.

- Dynamic IP address
Dynamic IP addresses are subject to change, sometimes at a moment's notice. Are assigned as needed, by Dynamic Host Configuration Protocol (DHCP) servers.
We use Dynamic addresses because IPv4 doesn't provide enought static IP addresses to go around.
#### What is `localhost`
Is a hostname that refers to the current device used to access it. It is used to access the network services that are running on the host via the loopback network interface.
#### What is subnet
#### why IPv6 was created

### TCP/UDP
Both TCP and UDP are protocols used for sending bits of data over the Internet. Both protocols build on top of the IP protocol. 
#### What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
TCP and UDP
#### What is the main difference between TCP and UDP

#### What is a port
#### Memorize SSH, HTTP and HTTPS port numbers
#### What tool/protocol is often used to check if a device is connected to a network