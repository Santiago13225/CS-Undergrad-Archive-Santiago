# Past Midterm Questions

#### **Question 1**

1) What are the three major components of internet if you take a "nuts and bolts" view?
   ANSWER: **Devices, Links, Packet Switches**
2) What is the definition of protocols?
   ANSWER: **Protocols define format order of messages sent and received among network entities and actions taken on message transmission receipt**
3) What is inside the network core?
   ANSWER: **Routers**
4) What are the two key functions for network core?
   ANSWER: **Routing and Forwarding**
5) For packet switching and circuit switching, which one can accommodate more users?
   ANSWER: **Packet switching**

#### **Question 2**

1) What is the major difference between a virus and a worm?
   ANSWER: **Worms do not need user interaction but viruses do (virus requires user to click it to activate it, but worm acts on its own)**
2) What is a DDoS attack? Which is easier, DDoS attack to root DNS servers, or to TLD name servers?
   ANSWER: **Distributed Denial of Service attack; TLD name servers**
3) What is packet sniffing?
   ANSWER: **Records or reads all packets passing by including passwords**
4) What is IP spoofing?
   ANSWER: **Sends packets with the fourth source addresses**
5) Please describe a DNS poisoning attack
   ANSWER: **The server caches bogus replies so the bogus replies poison the server.**

#### **Question 3**

1) Which network architecture is more scalabe, client server model or P2P model?
   ANSWER: **P2P (more users = more combined computing speed)**
2) Which two identifiers should be used to address a process in a communication?
   ANSWER: **IP address and port number**
3) Which transport layer protocol could be used for email service, TCP or UDP? Why?
   ANSWER: **TCP because we do not want to lose any data in email transfer since TCP guarantees no data will be lost during transfer.**
4) Which transport layer protocol provides flow control and congestion control, TCP or UDP?
   ANSWER: **TCP**
5) Is Secure Socket Layer (SSL) implemented at the application layer or transport layer?
   ANSWER: **Application layer**

#### **Question 4**

1. What is the major difference between persistent HTTP and non-persistent HTTP?
   ANSWER: **Persistent HTTP allows multiple objects to be sent over a single connection, whereas non-persistent allows only one object through.**
2. When using cookies, what is the header line used used by the server to send the client the cookie ID?
   ANSWER: **Set-Cookie**
3. When the client wants to attach this cookie ID again in the request message, what is the header line used?
   ANSWER: **Cookie**
4. Where is the cookie ID stored on server side?
   ANSWER: **Database or backend**
5. Where is the cookie ID stored on client side?
   ANSWER: **Cookie file, managed by web browser**

#### **Question 5**

1. What are the four services provided by DNS?
   ANSWER: **Host to IP mapping, Host nickname, Mail server nickname, load distribution**
2. What are the two resolution methods for DNS name resolution?
   ANSWER: **iterated or recursive**
3. If you have a startup company named fruit.com, the DNS server for fruit.com is dns.fruit.com and the IP address for dns.fruit.com is 192.168.112.0. What are the two Resource Records that need to insert into the .com TLD server by the registrar.
   ANSWER: **(fruit.com, dns.networkdevices.com, NS) and (dns.fruit.com, 192.168.112.0, A)**

#### **Question 6**

1. In BitTorrent, when a new user Alice is requesting missing file chunks from the peers, if chunk A is available on 10 peers and chunk B is available on 2 peers, which chunk will Alice request first?
   ANSWER: **Chunk B, by the rarest first policy**
2. In BitTorrent, to which peers will Alice send the chunks based on the tit-for-tat mechanism?
   ANSWER: **The peers currently sending her chunks at the highest speed**

#### **Question 7**

1. In UDP, should the client/server create a socket using **SOCK_DGRAM** or **SOCK_STREAM**?
   ANSWER: **SOCK_DGRAM**
2. In UDP, should the client send a message using **send** or **sendto**?
   ANSWER: **sendto**
3. In UDP, should the client close the client socket after the communication is completed? Should the server close the server socket after the communication is completed?
   ANSWER: **For client, it needs to close; For server, it should not close since it will always be used indefinitely.**
4. In TCP, how many types of sockets will be created on the server side? What are their differences?
   ANSWER: **2 types, one is for welcoming requests, one is for handling requests**
5. In TCP, which type of server socket mentioned above can be closed after communication is completed?
   ANSWER: **The connection socket that is handling services**

#### **Question 8**

1. What are the 7 layers in the ISO/OSI model?
   ANSWER: **Application, presentation, session, transport, network, datalink, physical**
2. Which two layers are missing in the Internet Protocol Stack?
   ANSWER: **presentation, session**
3. Please list at least two major benefits of using web cache/proxy server.
   ANSWER: **same bandwidth, same traffic**
4. In web cache, which header line is attached in the request message to get the up-to-date objects from the original server?
   ANSWER: **If-Modified-Since**
5. Which status line will be provided in the response message if the object is already up to date and not modified?
   ANSWER: **304 (Not-Modified)**

#### **Question 9**

Suppose there are two packet switches between a sending host A and a receiving host D. The transmission rates are: R1 = 3 Gbits/sec; R2 = 5 Gbits/sec; R3 = 10 Gbits/sec. The total distance between A and D is 100km, and the signal propagation speed between A and D is 20km/s. The nodal processing delay spent on each router is 2 seconds, and the queueing delay spent at each router is 1 second. Assuming that the switches use store-and-forward packet switching and packet length L = 30 Gbits, please answer the following questions:

1. The transmission delay between A and D is how many seconds?
   ANSWER: L/R = (L/R1) + (L/R2) + (L/R3) = (30/3) + (30/5) + (30/10) = **19**
2. The propagation delay between A and D is how many seconds?
   ANSWER: D/S where D is distance and S is speed = (100/20) = **5**
3. The total delay between A and D is how many seconds?
   ANSWER: transmission delay + propagation delay + nodal processing delay (2 nodes @ 2 secs each = 2x2) + queueing delay (2 nodes @ 1 sec each = 2x1) = 19+5+(2x2)+(1x2) = **30**
4. If the switch has infinite buffer, but the incoming packet rate is much faster than the outgoing packet rate, what type of delay will happen from the following: Transmission, Processing, Queueing, Propagation
   ANSWER: **Queueing Delay**
5. For the entire route, what is the effective throughput between A and D? The effective throughput is how many Gbits/sec?
   ANSWER: Effective throughput is limited by the slowest router, which has a speed of **3 Gbits/sec**

#### **Question 10**

Given the following scenario for email, please answer the following questions (**USE ALL CAPITAL LETTERS FOR YOUR ANSWERS**):

1. What are/is the application layer protocol(s) that can be used between the sender's user agent and sender's mail server?
   ANSWER: **SMTP, HTTP**
2. What are/is the application layer protocol(s) that can be used between the sender's mail server and receiver's mail server?
   ANSWER: **SMTP**
3. What are/is the application layer protocol(s) that can be used between the receiver's mail server and receiver's user agent?
   ANSWER: **POP3, RMAP, HTTP**
4. What is the port number for SMTP protocol?
   ANSWER: **25**
5. What is the underlying transport layer protocol for SMTP service?
   ANSWER: **TCP**

# Textbook Practice Q/A

#### Chapter 1 Q/A

**R1. What is the difference between "host" and "end system"? List several different types of end systems. Is a web server an end system?**
Answer:
The host and end systems are not different. Common end systems such as laptops, smartphones, etc. A web server is an end system.

**R2. The term "agreement" is often used to describe diplomatic relations. How does Wikipedia describe diplomatic agreements?**
Answer:
Baidu Encyclopedia: Agreements concluded between countries or governments to determine their mutual rights and obligations, mostly used for agreements on major political, economic, military, legal and other issues. There are bilateral and multilateral. The narrow sense only refers to agreements named after treaties, such as alliance treaties, friendship treaties, peace treaties, non-aggression treaties, etc. In a broad sense, it refers to agreements concluded in whatever name or form, such as treaties, conventions, agreements, joint declarations, joint communiqués, joint declarations, protocols, minutes of talks, exchange of letters, contracts, etc. Treaties, conventions, etc. are international legal documents and are the most important diplomatic instruments. The procedures for its conclusion and entry into force are very strict, and it needs to be approved by the organs stipulated in the national constitution to complete its legal procedures. Generally, the representatives of the contracting parties will jointly formulate the articles after formal negotiation and reach an agreement in principle; after the approval of the heads of state of the contracting parties, an exchange of letters ceremony will be held at the agreed date and place to exchange the ratification. It is usually stipulated that the treaty concluded by the two parties shall enter into force from the date of the exchange of ratifications. After a treaty or convention is signed, it is binding on all contracting states during its validity period. Agreements are used to conclude less significant or short-term agreements, which are widely used, such as trade agreements, shipping agreements, etc. Protocols are usually used for agreements on certain specific issues, or to interpret, supplement, modify or extend the validity of treaties that have already been concluded. Agreements and protocols have shorter periods of validity and simpler procedures to conclude. An exchange of notes means that the two parties confirm the contents of the agreement in the form of an exchange of notes, sometimes it is an annex to a treaty, agreement, etc.

**R3. Why are standards important to protocols?**
Answer:
The standard defines what the protocol is to do and what to do.

**R4. List 6 access technologies. Classify them as residential access, corporate access, or wide area wireless access.**
Answer:
Residential Access: Fiber Access DSL Access
Corporate Access: Ethernet WiFi
Wide Area Wireless Access: 3G 4G

**R5. Is HFC broadband dedicated or shared among users? Is collision possible in downlink HFC channel? Why?**
Answer:
HFC bandwidth is shared among users.
No collision will occur in the downstream HFC channel. Because packets are sent from one source and received by different end systems, there is no conflict.

**R6. List available residential access technologies in your city. For each type of access, the declared downlink rate, uplink rate and monthly price are given.**
Answer:
Fiber to the home. Dozens of M probably.

**R7. What is the transmission rate of Ethernet LAN?**
Answer:
10M-10G range.

**R8. What are some physical media that can run Ethernet?**
Answer:
Twisted pair copper wire, coaxial cable, fiber optic, etc.

**R9. Dial-up modems, HFC, DSL, and FTTH are all used for residential access. For each of these techniques, a range of transmission rates is given. And discuss about whether broadband is shared or dedicated.**
Answer:
Dial-up Modem: Rate 56kbps Bandwidth Dedicated (haven't seen other answers)
HFC: Downstream Rate: 42.8Mbps Upstream Rate: 30.7Mbps Bandwidth Shared
DSL: Downstream Rate: 24Mbps Upstream Rate: 2.5Mbps Bandwidth Shared
FTTH: Average Downstream Rate : 20Mbps bandwidth sharing

**R10. Describe the most popular wireless Internet access technologies today. Compare and contrast them.**
Answer:
WiFi and 4G access. WiFi is fast but short distances, 4G is slow but long distances.

**R11. Assume there is only one packet switch between the sending host and the receiving host. The transmission rates between the sending host and the switch and between the switch and the receiving host are R1 and R2, respectively. Assuming the switch uses store-and-forward packet switching, what is the total end-to-end delay for sending a packet of length L? (Ignore queuing delay, propagation delay and processing delay)**
Answer:
total delay=L/R1+L/R2

**R12. What are the advantages of circuit-switched networks over packet-switched networks? What are the advantages of TDM over FDM in circuit switched networks?**
Answer:
Circuit-switched networks are suitable for real-time services. Delivered in high quality.
The advantages of TDM over FDM are as follows: (from the network)

1. When network problems such as congestion occur, the data loss in TDM may only be part of it, while in FDM it may be most or all.
2. TDM is suitable for digital signal transmission, while FDM is suitable for analog signal transmission. Because most communication networks now transmit digital signals, TDM is better than FDM.
3. After the frequency division multiplexing connection is established, when there is no data transmission in the middle, the frequency band bandwidth occupied by it cannot be used by other connections, so there may be vacancies. In the statistical time division mode of time division multiplexing, after the connection is established, when the When a connection does not need to transmit data temporarily, it can be divided into less time slices or not divided, that is, the allocation of its time slots is "assigned on demand", thus giving up the corresponding transmission time to other connections.

**R13. Assume that users share a 2Mbps link. Also assume that when each user transmits at 1Mbps continuously, each user transmits only 20% of the time.
a. How many users can be supported when using circuit switching?
b. As a legacy of this problem, assume packet switching is used. Why is there basically no queuing delay in front of the link if two or fewer users transmit at the same time? Why is there a queuing delay if 3 users transmit at the same time?
c. Find the probability that a given user is transmitting.
d. Assume there are now 3 users. Find the probability that all 3 users are transmitting at the same time at any given time. Find the rate at which the queue grows in time.**
Answers:
a. Can support 2 users when using circuit switching.
b. If two or less users are transmitting, even if they transmit at the same time, they only fully occupy the 2Mbps link and will not cause queuing. If there are 3 users transmitting at the same time, 3Mbps is required, and the link is only 2Mbps at this time, so there will be a queuing delay.
c. Specify a 20% probability that the user is transmitting.
d. At any given time, the probability that all three users transmit simultaneously is 0.2*0.2*0.2=0.008. Because the queue grows only when there are only three users, the rate at which the queue grows is 0.008.

**R14. Why are two ISPs at the same level of the hierarchy usually peering with each other? How does an IXP earn money?**
Answer:
Because all traffic between them can be directly connected instead of going through the upstream ISP.
IXPs can charge ISPs for the traffic they exchange.

**R15. Some content providers build their own networks. Describe Google's network. What are the motivations for content providers to build these networks?**
Answer:
Google's network: At the time of this writing, Google estimates that there are 30-50 data centers. Google's data centers are interconnected by a dedicated TCP/IP network that spans the globe but remains independent of the public Internet.
Content providers are motivated to build these networks: to interface directly with lower-tier ISPs, reducing the fees they pay to ISPs. Has more control over how its services are ultimately delivered to end users.

**R16. Consider sending a packet from a source host to a destination host across a fixed route. List the end-to-end delay components. Which of these delays are fixed and which are variable?**
Answer:
The components of end-to-end delay are: node processing delay, queuing delay, transmission delay, and propagation delay.
The fixed parts of the delay are: transmission delay propagation delay
The variable parts of the delay are: node processing delay queuing delay (unlike other answers, I don't think the router's processing time is fixed)

**R17. Access the Java applet on transmission delay and propagation delay on the companion web site. Find a combination of available rate, propagation delay, and available packet length such that the sender finishes transmission before the first bit of the packet reaches the receiver. Find another combination such that the first bit of the packet reaches the receiver before the sender completes the transmission.**
Answer:
skip.

**R18. How long does it take for a packet of length 1000 bytes to travel over a link of 2500km with a propagation rate of 2.5x10^8m/s and a transmission rate of 2Mbps? More generally, how long does it take for a packet of length L to propagate over a link of distance d at a transmission rate of s and a propagation rate of Rbps? Is this delay related to the transmission rate?**
Answer:
(1)
Transmission delay: 8Kb/2Mb = 4ms
Propagation delay: 2500km/2.5x10^8m/s = 10ms
takes 14ms
(2)
Transmission delay: 8*L/R
Propagation delay: d The time required for /s
is 8*L/R + d/s
The delay is related to the transmission rate.

**R19. Suppose host A wants to send a large file to host B. There are 3 links on the path from host A to host B, and their rates are R1 = 500kbps, R2 = 2Mbps, and R3 = 1Mbps.
a. What is the throughput of the file transfer, assuming there is no other traffic on the network?
b. Assume the file is 4MB. How long does it roughly take to transfer this file to host B?
c. Repeat (a) and (b), except this time R2 is reduced to 100kbps.**
Answer:
a. The throughput is 500kbps
b. It takes roughly 64s
c. The throughput is 100kbps and it takes roughly 320s

**R20. Suppose end system A wants to send a large file to end system B. At a very high level, describe how the end system generates packets from this file. When one of these packets arrives at a packet switch, what information does the switch use in the packet to decide which way to forward the packet? Why is packet switching in the Internet comparable to driving from one city to another and asking for directions along the way?**
Answer:
End systems utilize the application layer to generate packets.
The packet switch at this time should refer to the router. A router uses the IP address in a packet to decide which way to forward the packet.
Each router has a forwarding table. When a packet arrives at a router, the router checks the IP address and uses this address to search the forwarding table to find the appropriate outgoing link. This approach is similar to asking for directions along the way.

**R21. Access the queuing and packet dropping Java applet of the companion Web site. What is the maximum send rate and minimum transfer rate? What is the traffic intensity for these rates? How long does it take to run the Java applet at these rates and determine if packet loss occurs? Then repeat the experiment a second time to again determine how long it takes for packet loss to occur. How are these values different? Why does this happen?**
Answer:
skip.

**R22. List 5 tasks that a hierarchy can perform. Could one (or both) of these tasks be performed by two (or more) layers?**
Answer:
For example, at the transport layer, the tasks of TCP are divided into short packets, congestion control, flow control, reliability, and so on. Its tasks are not performed by two (or more) levels. However, many levels of tasks are repetitive.

**R23. What are the 5 layers in the Internet protocol stack? In these layers, what is the main task of each layer?**
Answer:
Application layer: Provides some network applications and application layer protocols.
Transport Layer: Transport layer messages between application endpoints. There are two main protocols, TCP and UDP.
Network layer: Responsible for moving packets from one host to another.
Link layer: The datagram is passed to the next layer of nodes along the path.
Physical Layer: Moves the entire frame from one network element to an adjacent network element.

**R24. What is an application layer packet? What is a transport layer segment? What is a network layer datagram? What is a link layer frame?**
Answer:
Application Layer Messages: Packets of information exchanged between one end system and another end system application.
Transport Layer Segment: Packets at the Transport Layer
Network Layer Datagram: Packets at the Network Layer
Link Layer Frame: Packets at the Link Layer

**R25. What layers in the Internet protocol stack do routers handle? What layers do link layer switches handle? What layers does the host handle?**
Answer:
The level of router processing: physical layer, link layer, network layer
, the level of switch processing: physical layer, link layer
, the level of host processing: physical layer, link layer, network layer, transport layer, application layer

**R26. What is the difference between a virus and a worm?**
Answer:
Virus: Requires user interaction to infect a device.
Worms: Infect devices without user interaction.

**R27. Describe how a botnet is created and how botnets are used for DDoS attacks.**
Answer:
Malware controls many network devices, collectively known as botnets.
Using malware, the network devices in the botnet send a large number of packets to the target host, or create a large number of connections, etc., so that the target host is in trouble. This is how botnets are used for DDoS attacks.

**R28. Suppose Alice and Bob send packets to each other over a computer network. Suppose Trudy places herself in the network such that she can capture all packets sent by Alice and send what she wants to Bob; she can also capture all packets sent by Bob and send what she wants to Alice. List some malicious things Trudy can do in this situation.**
Answer:
Trudy can sniff packets, get a copy of the transmitted packets, and can spoof IP to impersonate another user.

#### Chapter 2 Q/A

**R1 List five nonproprietary Internet applications and the application-layer
protocols that they use.**
Browse web pages HTTP protocol
File transfer FTP protocol
P2P download P2P protocol
Send mail SMTP protocol
DNS service DNS protocol

**R2 What is the difference between network architecture and application
architecture?**
network architecture is a layered architecture, but from the application developer's point of view, the network architecture is fixed and provides a specific set of services for the application.
Application architecture dictates how applications are organized on various end systems. There are two mainstream architectures: client-server architecture and peer-to-peer architecture.

**R3 For a communication session between a pair of processes, which process is the client and which is the server?**
to initiate a session is the client, and the first process waiting for a connection is the server.

**R4 For a P2P file-sharing application, do you agree with the statement, "There is no notion of client and server sides of a communication session?" Why or why not?**
disagrees. Because once there is a process of communication, there must be a client and a server. And in another sense, P2P also has servers to record information.

**R5 What information is used by a process running on one host to identify a process running on another host?**
identifies the peer host using the IP address, and identifies the process on the peer host using the port number.

**R6 Suppose you wanted to do a transaction from a remote client to a server as fast as possible. Would you use UDP or TCP? Why?**
uses UDP. UDP doesn't require connection establishment, congestion control, etc, so it's faster.

**R7 Referring to Figure 2.4, we see that none of the applications listed in Figure 2.4 requires both no data loss and timing. Can you conceive of an application that requires no data loss and that is also highly time-sensitive?**
Computer Controlled Machinery

**R8 List the four broad classes of services that a transport protocol can provide. For each of the service classes, indicate if either UDP or TCP (or both) provides such a service.**
Reliable Data Transmission TCP
Throughput TCP/UDP
Timing TCP/UDP
Security TCP+SSL

**R9 Recall that TCP can be enhanced with SSL to provide process-to-process security services, including encryption. Does SSL operate at the transport layer or the application layer? If the application developer wants TCP to be enhanced with SSL, what does the developer have to do?**
SSL runs at the application layer.
Need to pass SSL encrypted data to UDP. (It seems that it can't be done now, unless you implement SSL yourself)

**R10 What is meant by a handshaking protocol?**
confirms the identity, establishes the TCP connection, and prepares the client and server to accept a large number of packets.

**R11 Why do HTTP, FTP, SMTP, and POP3 run on top of TCP rather than on UDP?**
does not allow data loss because the above protocol requires reliable data transmission.

**R12 Consider an e-commerce site that wants to keep a purchase record for each of its customers. Describe how this can be done with cookies.**
For each new customer visiting the e-commerce website, set a corresponding cookie on the browser, and store the purchase record of the corresponding customer on the server. When the same customer visits later, a cookie will be attached to the HTTP request, and the server can determine that it is the same customer and continue to store the purchase record.

**R13 Describe how Web caching can reduce the delay in receiving a requested
object. Will Web caching reduce the delay for all objects requested by a user
or for only some of the objects? Why?**
A copy of the most recently requested object is stored in the web cache. Web requests are directed to the web cache first. Only the delay of some objects can be reduced. Because the web cache only stores visited copies, unvisited objects are not present in the web cache. At this point, the latency of requesting the object cannot be reduced.

**R14 Telnet into a Web server and send a multiline request message. Include in the request message theIf-modified-since:header line to force a response message with the304 Not Modifiedstatus code.**
[Answers](https://github-com.translate.goog/jzplp/Computer-Network-A-Top-Down-Approach-Answer/blob/master/Chapter-2/RQA-R14/R14.md?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp)

**R15 Why is it said that FTP sends control information "out-of-band"?**
because FTP uses two parallel TCPs to transfer files. One is the control connection and the other is the data connection. Because the transmission of data is separate from the control information, it is called out-of-band transmission of control information.

**R16 Suppose Alice, with a Web-based e-mail account (such as Hotmail or gmail), sends a message to Bob, who accesses his mail from his mail server using POP3. Discuss how the message gets from Alice’s host to Bob’s host. Be sure to list the series of application-layer protocols that are used to move the message between the two hosts**
Alice host-(HTTP protocol)-Alice's server-(SMTP protocol)-Bob's server-(POP3 protocol)-Bob's host

The header of the message received by **R17**:

> HTTP/1.1 200 OK
> Date: Sat, 19 Jan 2019 13:03:02 GMT
> Server: Apache
> Last-Modified: Sat, 31 Dec 2011 09:54:00 GMT
> ETag: "1cdb-4b56054245e00"
> Accept-Ranges: bytes
> Content- Length: 7387
> Cache-Control: max-age=86400
> Expires: Sun, 20 Jan 2019 13:03:02 GMT
> Connection: Keep-Alive
> Content-Type: text/html

   1. HTTP/1.1 200 OK
   HTTP/1.1 means HTTP version
   200 OK means the request is successful

1. Date: Sat, 19 Jan 2019 13:03:02 GMT
   indicates the date and time when the server sent the response message
2. Server: Apache
   server for Apache
3. Last-Modified: Sat, 31 Dec 2011 09:54:00 GMT
   Date and time when the request object was last modified
4. ETag: Version tag for the "1cdb-4b56054245e00"
   object
5. Accept-Ranges: bytes
   indicates that the breakpoint resuming of bytes is supported
6. Content-Length: 7387
   bytes of the object
7. Cache-Control: max-age=86400
   means that when accessing this object again within 86400 seconds, it will not go to the server to request, but use the cache
8. Expires: Sun, 20 Jan 2019 13:03:02 GMT
   The date on which this object will expire
9. Connection: Keep-Alive
   client-to-server connection continues to be valid
10. Content-Type: text/html
    object type is html text

    **R18 From a user's perspective, what is the difference between the download-and-delete mode and the download-and-keep mode in POP3?**
    the difference is that if you choose the download and retain mode, even if the mail stored locally is lost, the user can retrieve the mail again.

**R19 Is it possible for an organization''s Web server and mail server to have exactly the same alias for a hostname (for example,foo.com)? What would be the type for the RR that contains the hostname of the mail server?**
can have the exact same hostname.
RR must have a record of type MX.

**R20 Look over your received emails, and examine the header of a message sent
from a user with an .edu email address. Is it possible to determine from the
header the IP address of the host from which the message was sent? Do the
same for a message sent from a gmail account.**
[Answers](https://github-com.translate.goog/jzplp/Computer-Network-A-Top-Down-Approach-Answer/blob/master/Chapter-2/RQA-R20/R20.md?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp)

**R21 In BitTorrent, suppose Alice provides chunks to Bob throughout a 30-second interval. Will Bob necessarily return the favor and provide chunks to Alice in this same interval? Why or why not?**
is not required to make a return. As determined by BitTorrent's mechanics, there is no "must" reward operation.

**R22 Consider a new peer Alice that joins BitTorrent without possessing any chunks. Without any chunks, she cannot become a top-four uploader for any of the other peers, since she has nothing to upload. How then will Alice get her first chunk?**
Every 30 seconds, other peers will randomly select a new peer to start swapping. If Alice is selected, Alice will get the file block.

**R23 What is an overlay network? Does it include routers? What are the edges in
the overlay network?**
The overlay network is an application-layer-oriented network that includes peers and an abstract logical network composed of virtual connections between peers. The overlay network does not include routers. An "edge" in an overlay network is a logical link between peers and peers.

**R24 Consider a DHT with a mesh overlay topology (that is, every peer tracks all
peers in the system). What are the advantages and disadvantages of such a
design? What are the advantages and disadvantages of a circular DHT (with
no shortcuts)?**
mesh overlay network topology: the advantage is that the structure is simple and the implementation is convenient. Reduce the query time and the number of packets. The disadvantage is that it is too expensive for large-scale systems to be practical.
Ring DHT: Advantage Reduces the amount of overlay information that each peer has to manage. The disadvantage is that too many packets are sent, which takes a long time.

**R25 List at least four different applications that are naturally suitable for P2P
architectures. (Hint: File distribution and instant messaging are two.)**
distributed file storage, instant messaging, distributed download, blockchain

**R26 In Section 2.7, the UDP server described needed only one socket, whereas the TCP server needed two sockets. Why? If the TCP server were to supportn
simultaneous connections, each from a different client host, how many sockets
would the TCP server need?**
because a UDP port can receive packets sent by multiple hosts. And a TCP port can only establish a connection with one client. Therefore, the port needs to be freed to accept new client connections. requires n+1 sockets

**R27 For the client-server application over TCP described in Section 2.7, why must the server program be executed before the client program? For the client-
server application over UDP, why may the client program be executed before
the server program?**
Because TCP needs to establish a connection before sending, UDP does not.

#### Chapter 3 Q/A

**R1 Suppose the network layer provides the following service. The network layer
in the source host accepts a segment of maximum size 1,200 bytes and a des-
tination host address from the transport layer. The network layer then guaran-
tees to deliver the segment to the transport layer at the destination host.
Suppose many network application processes can be running at the
destination host.
a. Design the simplest possible transport-layer protocol that will get applica-
tion data to the desired process at the destination host. Assume the operat-
ing system in the destination host has assigned a 4-byte port number to
each running application process.
b. Modify this protocol so that it provides a "return address" to the destination process.
c. In your protocols, does the transport layer "have to do anything" in the
core of the computer network?**

ANSWERS (a-c):
a. The transport layer message only needs to contain the destination port number and the data part. 4 bytes for port, 1196 bytes for data.
b. The transport layer message needs to contain the source port number, destination port number and data part. The source port number is 4 bytes, the destination port number is 4 bytes, and the data is 1192 bytes.
c. The transport layer does not need to do anything in the network core.

**R2 Consider a planet where everyone belongs to a family of six, every family
lives in its own house, each house has a unique address, and each person in a
given house has a unique name. Suppose this planet has a mail service that
delivers letters from source house to destination house. The mail service
requires that (1) the letter be in an envelope, and that (2) the address of the
destination house (and nothing more) be clearly written on the envelope. Sup-
pose each family has a delegate family member who collects and distributes
letters for the other family members. The letters do not necessarily provide
any indication of the recipients of the letters.**

a. Using the solution to Problem R1 above as inspiration, describe a protocol
that the delegates can use to deliver letters from a sending family member
to a receiving family member.
b. In your protocol, does the mail service ever have to open the envelope and
examine the letter in order to provide its service?

ANSWERS (a-b):
a. The protocol of R1b can be used, the family member who writes the letter is the application layer, and the letter is handed over to the family member who collects the letter, which represents the transport layer. The shipping layer adds the sender's name and the recipient's name to the envelope, indicating the port number, and hands the letter to the postal service.
b. No need to open the envelope to check the contents of the letter.

**R3 Consider a TCP connection between Host A and Host B. Suppose that the
TCP segments traveling from Host A to Host B have source port numberx
and destination port numbery. What are the source and destination port num-
bers for the segments traveling from Host B to Host A?**
source port number y, destination port number x

**R4 Describe why an application developer might choose to run an application
over UDP rather than TCP**

1. Allow a small number of packets to be lost
2. Require a certain sending rate, do not want to be bound by TCP congestion control

**R5 Why is it that voice and video traffic is often sent over TCP rather than UDP
in today's Internet? (Hint: The answer we are looking for has nothing to do
with TCP's congestion-control mechanism.)**
may be because TCP has a perfect retransmission mechanism in case of loss/error, and does not need to deal with data loss at the user layer.

**R6 Is it possible for an application to enjoy reliable data transfer even when the
application runs over UDP? If so, how?**
can obtain reliable data transmission, and check whether the data is complete at the application layer. If it is not complete, the application layer sends a message to instruct the sender to retransmit.

**R7 Suppose a process in Host C has a UDP socket with port number 6789. Sup-
pose both Host A and Host B each send a UDP segment to Host C with desti-
nation port number 6789. Will both of these segments be directed to the same
socket at Host C? If so, how will the process at Host C know that these two
segments originated from two different hosts?**
The two segments are described as the same socket. The application layer process can parse the packet data, and can also identify two different hosts by obtaining the IP and port number of the source host.

**R8 Suppose that a Web server runs in Host C on port 80. Suppose this Web
server uses persistent connections, and is currently receiving requests from
two different Hosts, A and B. Are all of the requests being sent through the
same socket at Host C? If they are being passed through different sockets, do
both of the sockets have port 80? Discuss and explain.**
is delivered via different sockets. The sockets all have port 80. Web services use TCP, and the socket of TCP is determined by the source IP and port number, and the destination IP and port number.

**R9 In our rdt protocols, why did we need to introduce sequence numbers?**
needs to confirm whether the received message is a new message or a retransmission of the previous message.

**R10 In our rdt protocols, why did we need to introduce timers?**
needs to confirm whether the sent packet is lost.

**R11 Suppose that the roundtrip delay between sender and receiver is constant and known to the sender. Would a timer still be necessary in protocolrdt 3.0,
assuming that packets can be lost? Explain.**
still needs timers to control retransmissions.

**R12 Visit the Go-Back-N Java applet at the companion Web site.
a.Have the source send five packets, and then pause the animation before
any of the five packets reach the destination. Then kill the first packet and
resume the animation. Describe what happens.
b. Repeat the experiment, but now let the first packet reach the destination
and kill the first acknowledgment. Describe again what happens.
c.Finally, try sending six packets. What happens?**
does not have Access Code and cannot be completed

**R13 Repeat R12, but now with the Selective Repeat Java applet. How are Selec-
tive Repeat and Go-Back-N different?**
does not have Access Code and cannot be completed

**R14 True or false?
a. Host A is sending Host B a large file over a TCP connection. Assume
Host B has no data to send Host A. Host B will not send acknowledg-
ments to Host A because Host B cannot piggyback the acknowledgments
on data.
b. The size of the TCPrwndnever changes throughout the duration of the
connection.
c. Suppose Host A is sending Host B a large file over a TCP connection. The
number of unacknowledged bytes that A sends cannot exceed the size of
the receive buffer.
d. Suppose Host A is sending a large file to Host B over a TCP connection. If
the sequence number for a segment of this connection ism, then the
sequence number for the subsequent segment will necessarily bem+ 1.
e. The TCP segment has a field in its header forrwnd.
f. Suppose that the lastSampleRTTin a TCP connection is equal to 1 sec.
The current value ofTimeoutIntervalfor the connection will neces-
sarily be≥1 sec.
g. Suppose Host A sends one segment with sequence number 38 and 4 bytes
of data over a TCP connection to Host B. In this same segment the
acknowledgment number is necessarily 42.**
a. False
b. False
c. True
d. False
e. True
f. False
Assuming the old SampleRTT is 0.9, the old EstimatedRTT is 0.9 and the DevRTT is 0.
The new SampleRTT is 1, the new EstimatedRTT is 0.9125, and the new DevRTT is 0.025. Then the new TimeoutInterval is 0.9225, which is less than 1
g. False
The acknowledgment number in the same message has nothing to do with the initial sequence number and number of bytes of the message

**R15 Suppose Host A sends two TCP segments back to back to Host B over a TCP
connection. The first segment has sequence number 90; the second has
sequence number 110.
a. How much data is in the first segment?
b. Suppose that the first segment is lost but the second segment arrives at B.
In the acknowledgment that Host B sends to Host A, what will be the
acknowledgment number?**
a. 20 bytes of data
b. Confirmation number is 90

**R16 Consider the Telnet example discussed in Section 3.5. A few seconds after the user types the letter 'C,' the user types the letter 'R.' After typing the letter 'R', how many segments are sent, and what is put in the sequence number
and acknowledgment fields of the segments?**
After the user types in R, another 3 segments are
sent. A sends: Seq=43, ACK=80, data='R'
B sends: Seq=80, ACK=44, data='R'
A sends: Seq =44, ACK=81

**R17 Suppose two TCP connections are present over some bottleneck link of rateRbps. Both connections have a huge file to send (in the same direction over the bottleneck link). The transmissions of the files start at the same time. What transmission rate would TCP like to give to each of the connections?**

Both are at a rate of about R/2

**R18 True or false? Consider congestion control in TCP. When the timer expires at the sender, the value ofssthreshis set to one half of its previous value.**
False, set to half of the current congestion window value

**R19 In the discussion of TCP splitting in the sidebar in Section 7.2, it was
claimed that the response time with TCP splitting is approximately 4 x RTTFE + RTTBE + processing time. Justify this claim.**
4*RTT ~FE~ is the time it takes for the client to communicate with the front-end server connection. When the front-end server receives a request, it will communicate with the remote server. Since the TCP connection is continuous, there is no time to establish a connection, so the time spent is RTT ~BE~ . Plus events handled by intermediate servers.

#### Chapter 4 Q/A

**R1 Let's review some of the terminology used in this textbook. Recall that the
name of a transport-layer packet issegmentand that the name of a link-layer
packet isframe. What is the name of a network-layer packet? Recall that both
routers and link-layer switches are calledpacket switches. What is the
fundamental difference between a router and link-layer switch? Recall that
we use the termroutersfor both datagram networks and VC networks.**
The name of the network layer packet is datagram. Routers work at the network layer, and link layer switches work at the data link layer.

**R2 What are the two most important network-layer functions in a datagram network? What are the three most important network-layer functions in a virtual-circuit network?**
datagram network: forwarding, routing
Virtual circuit network: forwarding, routing, connection establishment

**R3 What is the difference between routing and forwarding?**
forwarding is moving from the router's input link to the output link, and routing is determining the path of the datagram from the sender to the receiver.

**R4 Do the routers in both datagram networks and virtual-circuit networks use forwarding tables? If so, describe the forwarding tables for both classes of networks.**
Both use forwarding tables.
The conversion of the interface and the VC number is recorded in the virtual circuit network forwarding table.
The destination subnet and output interface of the packet network forwarding table.

**R5 Describe some hypothetical services that the network layer can provide to a
single packet. Do the same for a flow of packets. Are any of your hypothetical services provided by the Internet's network layer? Are any provided by
ATM's CBR service model? Are any provided by ATM's ABR service
model?**
Hypothetical services that the network layer can provide for a single packet:
guaranteed delivery, upper bound on latency Hypothetical services that the
network layer can provide for packet streams:
ordered delivery, minimum bandwidth, maximum delay jitter, security services

The network layer of the Internet does not provide these services. The CBR services of ATM are: constant bandwidth, guaranteed delivery, orderly delivery, delay upper bound, and maximum delay jitter. The ABR services of ATM are: minimum bandwidth, orderly delivery.

**R6 List some applications that would benefit from ATM's CBR service model.**
VoIP, real-time video, etc.

**R7 Discuss why each input port in a high-speed router stores a shadow copy of
the forwarding table**
is very fast because of the forwarding request. So storing the shadow copy on the port's line card frees the port from calling the central selection processor, speeding it up.

**R8 Three types of switching fabrics are discussed in Section 4.3. List and briefly
describe each type. Which, if any, can send multiple packets across the fabric
in parallel?**

1. Through memory switching
Similar to a shared memory multiprocessor, a piece of memory is shared, and the lookup of the destination address and packet switching are handled by the output line card.

1. Via bus switching
   Input ports use a shared bus to transfer packets directly to output ports
2. Switching via an interconnect network
   uses a cross-bar bus fabric, with cross points opened and closed by a switch fabric controller.

   Multiple packets may be sent in parallel via an interconnected network switch.

   **R9 Describe how packet loss can occur at input ports. Describe how packet loss at input ports can be eliminated (without using infinite buffers).**
   The transmission speed of the switching fabric cannot make the packet pass through the switching fabric without delay, and the input port will be queued, and if the queue is too long, it will be lost.
   solution:

   Accelerates the transfer speed of the switch fabric. Try to solve HOL blocking by rearranging the queue in the input port so that it can reduce the situation of HOL blocking.

   **R10 Describe how packet loss can occur at output ports. Can this loss be
   prevented by increasing the switch fabric speed?** 
   The transmission speed of the switching structure to an output port is faster than the output speed of the output port, which will cause queuing. If the queue is too long, it will be lost. Increasing the rate of the switch fabric has the opposite effect on the loss phenomenon. The higher the rate, the more loss.

**R11 What is HOL blocking? Does it occur in input ports or output ports?**
If the front packet of an input port is blocking, all subsequent packets cannot be sent, even if the output port of the latter packet is free.
appears at the input port.

**R12 Do routers have IP addresses? If so, how many?**
The router has an IP address, and one port has one IP address.

**R13 What is the 32-bit binary equivalent of the IP address 223.1.3.27?**
11011111 00000001 00000011 00011011

**R14 Visit a host that uses DHCP to obtain its IP address, network mask, default
router, and IP address of its local DNS server. List these values.**
IP Address: 192.168.2.239
Subnet Mask: 255.255.255.0
Default Router: 192.168.2.1
Local DNS Server: 192.168.2.1

**R15 Suppose there are three routers between a source host and a destination host. Ignoring fragmentation, an IP datagram sent from the source host to the destination host will travel over how many interfaces? How many forwarding tables will be indexed to move the datagram from the source to the destination?**
8 ports. Retrieve 3 forwarding tables.

**R16 Suppose an application generates chunks of 40 bytes of data every 20 msec, and each chunk gets encapsulated in a TCP segment and then an IP datagram. What percentage of each datagram will be overhead, and what percentage will be application data?**
40 bytes of data + 20 bytes of TCP header + 20 bytes of IP header = 80 bytes, the
percentage of application data is 50%

There is an upper-layer protocol field in the R17 IP protocol, which indicates the upper-layer protocol that should be handed over.

**R18 Suppose you purchase a wireless router and connect it to your cable modem. Also suppose that your ISP dynamically assigns your connected device (that is, your wireless router) one IP address. Also suppose that you have five PCs at home that use 802.11 to wirelessly connect to your wireless router. How
are IP addresses assigned to the five PCs? Does the wireless router use NAT?
Why or why not?**
generally uses the DHCP protocol to automatically assign addresses, and the DHCP server is the wireless router.
General wireless routers use NAT. Because it uses a local area network address, not a public network address.

**R19 Compare and contrast the IPv4 and the IPv6 header fields. Do they have any fields in common?**
version, TOS, upper layer protocol, lifetime, source address and destination address (different bits)

**R20 It has been said that when IPv6 tunnels through IPv4 routers, IPv6 treats the IPv4 tunnels as link-layer protocols. Do you agree with this statement? Why
or why not?**
can be understood in this way. Because the IPV6 datagram is encapsulated in the IPV4 datagram, the tunnel is equivalent to passing a hop router for the IPV6 message, so it is more like a link layer protocol.

**R21 Compare and contrast link-state and distance-vector routing algorithms**
link state algorithm:
global routing algorithm, need to broadcast
Distance vector routing algorithm:
distributed routing algorithm, only need to notify connected points

**R22 Discuss how a hierarchical organization of the Internet has made it possible
to scale to millions of users.**
Different ISPs build different autonomous systems, and internal routing protocols are used in the autonomous systems. The Inter-Autonomous System Routing Protocol is used between autonomous systems.
Secondly, the OSPF protocol can also be configured as multiple areas, and the area runs its own OSPF protocol.

**R23 Is it necessary that every autonomous system use the same intra-AS routing algorithm? Why or why not?**
is unnecessary. Different ASs may have different situations, and the suitable routing algorithms are also different. As long as the same inter-AS routing protocol is selected, the external routing selection will not be affected.

**R24 Consider Figure 4.37. Starting with the original table inD,suppose that D
receives from A the following advertisement: Will the table in D change? If so how?**
will not change

**R25 Compare and contrast the advertisements used by RIP and OSPF.**
The content advertised by RIP is the forwarding table of the router, and also includes the hop count of the destination. Only advertised to connected peers.
The content advertised by OSPF is the state information of a link, which is advertised to routers in all autonomous systems.

**R26 Fill in the blank: RIP advertisements typically announce the number of hops
to various destinations. BGP updates, on the other hand, announce the
__________ to the various destinations.**
AS-PATH and NEXT-HOP

**R27 Why are different inter-AS and intra-AS protocols used in the Internet?**
The intra-AS protocol and the inter-AS protocol deal with different problems. For example, the intra-AS protocol requires performance, but does not require scale and special strategies, but the inter-AS protocol requires more scale, scalability and strategy.

**R28 Why are policy considerations as important for intra-AS protocols, such as OSPF and RIP, as they are for an inter-AS routing protocol like BGP?**
The policy issue is relatively unimportant in the AS internal protocol.

**R29 Define and contrast the following terms: subnet,prefix, and BGP route.**
The subnet is an IP in a network segment with many hosts with similar IPs and the same prefix.
The prefix is the identifier of a subnet, and IPs with the same prefix are in a subnet.
BGP routing is a routing protocol between ASs.
AS and subnet are not the same concept. The scope of AS is generally larger than that of subnet. A router port is connected to a subnet. Multiple subnets and routers in one for AS. However, after route aggregation, the AS may be represented as a subnet to the outside world.

**R30 How does BGP use the NEXT-HOP attribute? How does it use the AS-PATH
attribute?**
The NEXT-HOP attribute is used to determine the next route in the forwarding table, and to know which AS gateway router it leads to.
The AS-PATH attribute is used to detect and prevent circular advertisements, and its length can also be used to determine routing.

**R31 Describe how a network administrator of an upper-tier ISP can implement
policy when configuring BGP**
uses input strategies, such as setting certain attributes, to filter routing information that does not match the attributes.

**R32 What is an important difference between implementing the broadcast abstraction via multiple unicasts, and a single network- (router-) supported broadcast?**
unicast means that the packets are copied and then individually routed to their destination.
Broadcast is to use the router directly, and only copy the message when forwarding to multiple ports.

**R33 For each of the three general approaches we studied for broadcast communication (uncontrolled flooding, controlled flooding, and spanning-tree broadcast), are the following statements true or false? You may assume that no
packets are lost due to buffer overflow and all packets are delivered on a link
in the order in which they were sent.
a. A node may receive multiple copies of the same packet.
b. A node may forward multiple copies of a packet over the same
outgoing link.**

ANSWERS:
Uncontrolled flooding :
a. True b. True
Controlled flooding:
a. True b. False
Spanning Tree Broadcast:
a. False b. False

Not required for R34

**R35 What are the roles played by the IGMP protocol and a wide-area multicast
routing protocol?**
IGMP notifies a router that it wants to join or leave a multicast group.
The role of the multicast routing algorithm is to enable members of the multicast group to receive packets, but members of non-multicast groups to receive as few packets as possible. Because of this, the path of the multicast message is selected.

The tree shared by R36 is the path that all group members use to send/receive multicast packets.
Source-based tree means that each member has an independent routing tree, and sends multicast packets according to this tree.

#### Chapter 5 Q/A

**R1 Consider the transportation analogy in Section 5.1.1. If the passenger is
analagous to a datagram, what is analogous to the link layer frame?**
passenger+ticket is analogous to link layer frame. I think the vehicle should be the physical layer, and the vehicle + service personnel is the link layer.

**R2 If all the links in the Internet were to provide reliable delivery service, would
the TCP reliable delivery service be redundant? Why or why not?**
is basically redundant.
TCP reliable delivery is redundant, and congestion control is based on statistical packet loss, which is also ineffective. Flow control is also useful.

**R3 What are some of the possible services that a link-layer protocol can offer to
the network layer? Which of these link-layer services have corresponding
services in IP? In TCP?**
Possible services provided by are: Framing, Link Access, Reliable Delivery, Error Detection and CorrectionIP Corresponding Services: IP Datagram, Datagram Delivery TCP Corresponding Services: TCP Segment, Reliable Delivery, Error Detection

**R4 Suppose two nodes start to transmit at the same time a packet of length L
over a broadcast channel of rateR. Denote the propagation delay between the
two nodes as dprop. Will there be a collision if dprop< L/R? Why or why not?**
will detect the transmission signal of other nodes before the node has finished transmission.

**R5 In Section 5.3, we listed four desirable characteristics of a broadcast channel.
Which of these characteristics does slotted ALOHA have? Which of these
characteristics does token passing have?**

There is R throughput when only one node is sending.

1. When M nodes send at the same time, the throughput of each node is R/M
2. The protocol is decentralized and will not crash due to a node failure.
3. The protocol is simple and the implementation is inexpensive.
   Slots ALOHA have: 1, 3, 4
   Token passing has: 1, 2, 4

   **R6 n CSMA/CD, after the fifth collision, what is the probability that a node chooses K= 4? The result K= 4 corresponds to a delay of how many seconds on a 10 Mbps Ethernet?**
   1/32
   The delay is 4 * 5.12 * 10 = 204.8μs . The
   Chinese version of the textbook is written in milliseconds. It has been verified by the English version and it is wrong.

**R7 Describe polling and token-passing protocols using the analogy of cocktail
party interactions.**
polling protocol:
There is a moderator who asks each participant in turn if they want to speak, and controls the maximum speaking time of each person.
Token passing protocol:
a microphone is passed between each participant. If someone wants to speak, they will pick up the microphone to speak, and if they do not speak, it will be passed to the next participant.

**R8 Why would the token-ring protocol be inefficient if a LAN had a very large
perimeter?**
is because if there are few nodes to be sent, it also needs to be fixed for one cycle at a time. And the cycle time is very long, causing inefficiency.

**R9 How big is the MAC address space? The IPv4 address space? The IPv6
address space?**
MAC address space: 2 ^48^
IPV4 address space: 2 ^32^
IPV6 address space: 2 ^128^

**R10 Suppose nodes A, B, and C each attach to the same broadcast LAN (through
their adapters). If A sends thousands of IP datagrams to B with each encapsu-
lating frame addressed to the MAC address of B, will C's adapter process
these frames? If so, will C's adapter pass the IP datagrams in these frames to
the network layer C? How would your answers change if A sends frames with
the MAC broadcast address?**

1. will not process these frames

2. These frames are processed and passed to the network layer according to the actual protocol specification.

**R11 Why is an ARP query sent within a broadcast frame? Why is an ARP
response sent within a frame with a specific destination MAC address?**
ARP query Because the MAC address is not clear, the link layer does not know where to send it.
ARP responses do not need to be broadcast because they know the MAC address of the target host.

**R12 For the network in Figure 5.19, the router has two ARP modules, each with
its own ARP table. Is it possible that the same MAC address appears in both
tables?**
is impossible because each port of the router has its own MAC address.

**R13 Compare the frame structures for 10BASE-T, 100BASE-T, and Gigabit Eth-
ernet. How do they differ?**
The frame format is the same.

**R14 Consider Figure 5.15. How many subnetworks are there, in the addressing
sense of Section 4.4?**
1 subnet

**R15 What is the maximum number of VLANs that can be configured on a switch
supporting the 802.1Q protocol? Why?**
2 ^12^ _

**R16 Suppose that N switches supporting KVLAN groups are to be connected via a trunking protocol. How many ports are needed to connect the switches?
Justify your answer.**
are connected to each other and require a minimum of 2N-2 ports.

#### Chapter 6 Q/A

**R1 What does it mean for a wireless network to be operating in 'infrastructure
mode?' If the network is not in infrastructure mode, what mode of operation
is it in, and what is the difference between that mode of operation and infra-
structure mode?**
"Infrastructure mode" refers to the mode associated with the host and base station. If not running in infrastructure mode, run in ad hoc mode. Ad hoc mode has no base station.

**R2 What are the four types of wireless networks identified in our taxonomy in
Section 6.1? Which of these types of wireless networks have you used?**

1. Single hop, infrastructure based
2. Single hop, no infrastructure
3. Multi-hop, infrastructure based
4. Multi-hop, no infrastructure

I am using single hop, based on infrastructure

**R3 What are the differences between the following types of wireless channel
impairments: path loss, multipath propagation, interference from other
sources?**
Path Loss: Electromagnetic waves pass through objects and are weakened and diffused in space
Multipath propagation: Electromagnetic waves produce paths of different lengths due to reflection, which blurs the received signal
Interference from other sources: Electromagnetic wave interference from the transmitting source and other sources

**R4 As a mobile node gets farther and farther away from a base station, what are
two actions that a base station could take to ensure that the loss probability of
a transmitted frame does not increase?**

1. The sender increases the transmit power.
2. Use lower bit rate modulation techniques.

**R5 Describe the role of the beacon frames in 802.11.**
enables the wireless station to detect the AP, and it is convenient to apply for access to the AP.

**R6 True or false: Before an 802.11 station transmits a data frame, it must first
send an RTS frame and receive a corresponding CTS frame.**
is wrong, only the data frame whose frame length exceeds the threshold value will use the RTS/CTS sequence.

**R7 Why are acknowledgments used in 802.11 but not in wired Ethernet?**
has a high probability of not being delivered correctly due to failure, so use confirmation. Wired Ethernet has a higher probability of being received correctly, so acknowledgements are not used.

**R8 True or false: Ethernet and 802.11 use the same frame structure.**
is wrong, the frame format is not the same.

**R9 Describe how the RTS threshold works.**
uses the RTS/CTS sequence only when the frame length exceeds the threshold.

**R10 Suppose the IEEE 802.11 RTS and CTS frames were as long as the standard
DATA and ACK frames. Would there be any advantage to using the CTS and
RTS frames? Why or why not?**
is not good. At this time, it is better to use RTS/CTS directly to use data frames. If no confirmation is received, retransmit.

**R11 Section 6.3.4 discusses 802.11 mobility, in which a wireless station moves
from one BSS to another within the same subnet. When the APs are intercon-
nected with a switch, an AP may need to send a frame with a spoofed MAC
address to get the switch to forward the frame properly. Why?**
needs to change the forwarding table of the switch, so that the switch forwards the frame to the new AP.

**R12 What are the differences between a master device in a Bluetooth network and a base station in an 802.11 network?**
The master device and slave device of Bluetooth are not different in physical structure. They are both wireless sites, and other slave devices can also be used as master devices. The AP in the 802.11 network has a special physical structure. Only it is connected to the external network, and other wireless stations cannot be used as APs.

**R13 What is meant by a super frame in the 802.15.4 Zigbee standard?**
The superframe is equivalent to a reciprocating time period, in which there are contended time slots, guaranteed time slots and inactive time slots, so that various types of devices can communicate normally.

**R14 What is the role of the 'core network' in the 3G cellular data architecture?**
The 3G core network connects the radio access network to the public Internet.

**R15 What is the role of the RNC in the 3G cellular data network architecture?
What role does the RNC play in the cellular voice network?**
The RNC controls several base stations and is connected to the MSC and SGSN, sharing the same radio access network.
In a cellular voice network, channels are allocated to users using CDMA technology.

**R16 If a node has a wireless connection to the Internet, does that node have to be mobile? Explain. Suppose that a user with a laptop walks around her house
with her laptop, and always accesses the Internet through the same access
point. Is this user mobile from a network standpoint? Explain.**
Even if the has a wireless connection, it is not necessarily mobile, such as a PC with 802.11 wireless capabilities.
From the network's perspective, the user is not moving.

**R17 What is the difference between a permanent address and a care-of address? Who assigns a care-of address?**
The permanent address refers to the fixed address of the wireless station. Even if the wireless station moves, the permanent address is fixed. Other hosts want to communicate with this wireless station and need to connect using this permanent address.
The care-of address is the address temporarily allocated by the wireless station on the external network, which is transparent to the user and is only used to forward the message to the external network so that the wireless station can receive the message.

**R18 Consider a TCP connection going over Mobile IP. True or false: The TCP
connection phase between the correspondent and the mobile host goes
through the mobile's home network, but the data transfer phase is directly
between the correspondent and the mobile host, bypassing the home network.**
If is indirect routing, it is **false**, and direct routing is correct.

**R19 What are the purposes of the HLR and VLR in GSM networks? What ele-
ments of mobile IP are similar to the HLR and VLR?**
HLR: Home Location Register, which contains each user's personal information and current location information. Equivalent to the home network in Mobile IP.
VLR: Visitor Location Registration, contains entries for users currently in the network, and coordinates call setup for arriving or departing mobile users. Equivalent to the external network in Mobile IP.

**R20 What is the role of the anchor MSC in GSM networks?**
The anchor MSC is the MSC visited by the mobile user when the call is first started. The function is to transfer the user's call to the current MSC when the user moves to another MSC.

**R21 What are three approaches that can be taken to avoid having a single wireless link degrade the performance of an end-to-end transport-layer TCP connection?**

1. A retransmission protocol is used in the wireless link.
2. The sender is aware of the wireless link and uses a special congestion control strategy.
3. Wired and wireless are separated into two transport layer connections.

#### Chapter 7 Q/A

**R1 Reconstruct Table 7.1 for when Victor Video is watching a 4 Mbps video,
Facebook Frank is looking at a new 100 Kbyte image every 20 seconds, and
Martha Music is listening to 200 kbps audio stream.**

|  application  | bit rate | Bytes transferred in 67 minutes |
| :------------: | :------: | :-----------------------------: |
|  Victor Video  |  4Mbps  |               2GB               |
| Frank Facebook |  40kbps  |              20MB              |
|  Martha Music  | 200kbps |              100MB              |

**R2 There are two types of redundancy in video. Describe them, and discuss how
they can be exploited for efficient compression.**
Spatial Redundancy: The internal redundancy of an image in a video.
Temporal Redundancy: The repetition of one image and subsequent images.
Compression method: Duplicate content is stored only once.

**R3 Suppose an analog audio signal is sampled 16,000 times per second, and each sample is quantized into one of 1024 levels. What would be the resulting bit rate of the PCM digital audio signal?**
16000/s * 1024 = 16Mbps

**R4 Multimedia applications can be classified into three categories. Name and
describe each category.**

1. Streaming storage of audio and video
Pre-recorded streaming, one-to-many.

1. Conversational IP voice and video
   One-to-one or many-to-many low-latency media.
2. Streaming Live Audio and Video
   Low-latency streaming, one-to-many.

   **R5 Streaming video systems can be classified into three categories. Name and briefly describe each of these categories.**

   1. UDP Streaming
      uses UDP transport.
3. HTTP streaming
   uses HTTP transport.
4. Adaptive HTTP streaming uses HTTP transport, where the media is encoded into several versions, which the user chooses based on bandwidth.

   **R6 List three disadvantages of UDP streaming.**

   1. Constant rate UDP streaming cannot provide continuous playback due to unpredictable bandwidth.
5. A media control server is required to handle requests and track status.
6. Many firewalls block UDP traffic.

   **R7 With HTTP streaming, are the TCP receive buffer and the client's application buffer the same thing? If not, how do they interact?**
   is not the same thing.
   The client cache reads bytes from the TCP cache, puts them in the client cache, and the TCP cache deletes these bytes.

**R8 Consider the simple model for HTTP streaming. Suppose the server sends
bits at a constant rate of 2 Mbps and playback begins when 8 million bits
have been received. What is the initial buffering delay?**
8 million bits = 8000000 = 8Mb The
initial cache delay is 8Mb / 2Mbps = 4s

**R9 CDNs typically adopt one of two different server placement philosophies.
Name and briefly describe these two philosophies.**
Deep: The CDN server is deep into the ISP's access network.
Invite guests: Build large clusters in a few key locations and use high-speed networks to invite ISP connections.

**R10 everal cluster selection strategies were described in Section 7.2.4. Which of
these strategies finds a good cluster with respect to the client’s LDNS? Which
of these strategies finds a good cluster with respect to the client itself?**
versus LDNS: Geographical closest approach, real-time measurement approach
Good clustering versus client: IP anycast approach

**R11 Besides network-related considerations such as delay, loss, and bandwidth
performance, there are many additional important factors that go into design-
ing a cluster selection strategy. What are they?**
Load on cluster, ISP delivery cost, etc.

**R12 What is the difference between end-to-end delay and packet jitter? What are the causes of packet jitter?**
end-to-end delay is the sum of transmission, processing, and queuing delays in routers, propagation in links, and processing delays in end systems, while delay jitter describes the change in end-to-end delay.
The key reason for packet delay jitter is that the queuing delay in the router is variable.

**R13 Why is a packet that is received after its scheduled playout time considered
lost?**
Because the playback time has passed, it is impossible for the application to use the content in this group for playback.

**R14 Section 7.3 describes two FEC schemes. Briefly summarize them. Both
schemes increase the transmission rate of the stream by adding overhead.
Does interleaving also increase the transmission rate?**
Forward Error Correction 1: Send a block XORed by the first n blocks after the nth block.
Forward Error Correction 2: The latter block sends a low-quality version of the previous block.
The interleaving technique does not increase the transmission rate of the stream.

**R15 How are different RTP streams in different sessions identified by a receiver?
How are different streams from within the same session identified?**
different sessions are identified by IP and port number.
Different streams of the same session are identified by the synchronization source identifier.

**R16 What is the role of a SIP registrar? How is the role of an SIP registrar different from that of a home agent in Mobile IP?**
SIP registrar: When a user uses an application, a registration message is sent to the registrar to maintain the user's IP address.
When an IP address is required, the SIP proxy forwards the INVITE packet to the user.
The difference between the registrar and the home agent is that the registrar only indicates the user's IP address when connecting, and after the actual communication starts, the SIP registrar does not participate in the session.
And the home agent (depending on the method) may always act as a hand-off in the communication process.

**R17 In Section 7.5, we discussed non-preemptive priority queuing. What would
be preemptive priority queuing? Does preemptive priority queuing make
sense for computer networks?**
is in the preemptive priority queuing, and currently there are low-priority packets being transmitted, and high-priority packets can also interrupt the transmission and directly start transmitting high-priority packets.
Preemptive priority queuing makes sense for computer networks because it allows for faster transmission of very important packets.

**R18 Give an example of a scheduling discipline that isnotwork conserving.**
time division multiplexing is the scheduling rule for non-retention work. Regardless of whether there is data being transmitted in this time slot, the time slot is completely elapsed and will not be skipped.

**R19 Give an example from queues you experience in your everyday life of FIFO,
priority, RR, and WFQ**
FIFO: Normal queuing is just that.
Priority: by plane, economy class, business class, first class
RR: select the first few in each class.
WFQ: Not encountered.

#### Chapter 8 Q/A

**R1 What are the differences between message confidentiality and message
integrity? Can you have confidentiality without integrity? Can you have
integrity without confidentiality? Justify your answer.** 

The difference is that confidentiality requires that the content of the message cannot be understood by others, and integrity can understand the content of the message, but it cannot be tampered with.
  There can be confidentiality but no integrity.
  There can be integrity but no confidentiality.

**R2 Internet entities (routers, switches, DNS servers, Web servers, user end sys-
tems, and so on) often need to communicate securely. Give three specific
example pairs of Internet entities that may want secure communication.**
When the router-router exchanges link state information or distance vectors, secure communication is required and cannot be tampered with.
Host-Web server browsing the web requires secure communication that cannot be tampered with.
Host-mail server sending mail requires secure communication, which is kept secret and cannot be tampered with

**R3 From a service perspective, what is an important difference between a
symmetric-key system and a public-key system?**
The difference is whether encryption and decryption use the same key.

**R4 Suppose that an intruder has an encrypted message as well as the decrypted
version of that message. Can the intruder mount a ciphertext-only attack, a
known-plaintext attack, or a chosen-plaintext attack?**
is a known-plaintext attack.

**R5 Consider an 8-block cipher. How many possible input blocks does this cipher
have? How many possible mappings are there? If we view each mapping as a
key, then how many possible keys does this cipher have?**
2 ^8^ possible input blocks. There are ^28^ ! possible mappings.

**R6 Suppose N people want to communicate with each of N–1 other people
using symmetric key encryption. All communication between any two peo-
ple, i and j, is visible to all other people in this group of N,and no other per-
son in this group should be able to decode their communication. How many
keys are required in the system as a whole? Now suppose that public key
encryption is used. How many keys are required in this case?**
uses symmetric keys and requires N(N-1) keys.
With public key cryptography, N keys are required.

**R7 Supposen= 10,000,a= 10,023, andb= 10,004. Use an identity of modular
arithmetic to calculate in your head (a • b) modn.**
[![Image text](https://github.com/jzplp/Computer-Network-A-Top-Down-Approach-Answer/raw/master/Chapter-8/RQA-R7/pic1.gif)](https://github-com.translate.goog/jzplp/Computer-Network-A-Top-Down-Approach-Answer/blob/master/Chapter-8/RQA-R7/pic1.gif?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp)

**R8 Suppose you want to encrypt the message 10101111 by encrypting the decimal number that corresponds to the message. What is the decimal number?**
87

**R9 In what way does a hash provide a better message integrity check than a
checksum (such as the Internet checksum)?**
calculates a string through the message, so that the strings generated by different messages are different.

**R10 Can you 'decrypt' a hash of a message to get the original message? Explain
your answer.**
is not possible. Because hash functions are designed to be irreversible.

**R11 Consider a variation of the MAC algorithm (Figure 8.9) where the sender
sends (m,H(m)+ s), whereH(m) +sis the concatenation ofH(m) ands. Is
this variation flawed? Why or why not?**
is defective

1. Expose s directly in the message, so that the eavesdropper can obtain s, which is no longer a secret.
2. The ability to identify false packets is lost.

**R12 What does it mean for a signed document to be verifiable and non-forgeable?**
We can confirm that he is complete, not forged, modified, and the source is normal.

**The R13 In what way does the public-key encrypted message hash provide a better digital signature than the public-key encrypted message?**
public key directly encrypts the message with too much computation and time-consuming. And just encrypting the hash is not computationally intensive.

**R14 Suppose certifier.com creates a certificate for foo.com. Typically, the entire
certificate would be encrypted with certifier.com’s public key. True or False?**
error, should be encrypted with certifier.com private key.

**R15 Suppose Alice has a message that she is ready to send to anyone who asks.
Thousands of people want to obtain Alice’s message, but each wants to be sure of the integrity of the message. In this context, do you think a MAC-based or a digital-signature-based integrity scheme is more suitable? Why?**
based on digital signatures is more suitable, because MAC requires Alice and everyone to have independent authentication keys.

**R16 What is the purpose of a nonce in an end-point authentication protocol?**
prevents replay attacks.

**R17 What does it mean to say that a nonce is a once-in-a-lifetime value? In whose lifetime?**
is a long period of time, at least not the time of one TCP connection.
Standard answer: only once in a lifetime.

**R18 Is the message integrity scheme based on HMAC susceptible to playback
attacks? If so, how can a nonce be incorporated into the scheme to remove
this susceptibility?**
is appended to the HMAC, using a non-multiplicative number similar to endpoint authentication.

**R19 Suppose that Bob receives a PGP message from Alice. How does Bob know
for sure that Alice created the message (rather than, say, Trudy)? Does PGP
use a MAC for message integrity?**
Bob uses Alice's public key to verify the signature, obtains the hash value, and then compares it with the hash value obtained from the message content. If they are consistent, he can verify that Alice generated the message.
PGP does not use MAC, but uses digital signatures to verify integrity.

**R20 In the SSL record, there is a field for SSL sequence numbers. True or False?**
error, the serial number is only used to calculate the MAC and is not included in the message.

**R21 What is the purpose of the random nonces in the SSL handshake?**
The purpose is to defend against "connection replay" attacks.

**R22 Suppose an SSL session employs a block cipher with CBC. True or False:
The server sends to the client the IV in the clear?**
is wrong because the IV is obtained from the MS, the MS is obtained from the PMS, and the PMS is generated by the client, encrypted with the public key and sent to the server.

**R23 Suppose Bob initiates a TCP connection to Trudy who is pretending to be Alice. During the handshake, Trudy sends Bob Alice’s certificate. In what
step of the SSL handshake algorithm will Bob discover that he is not commu-
nicating with Alice?**
After it is sent to Trudy in step 3, the server cannot decrypt the PMS. Bob hasn't found out yet.
At step 4, Trudy fails to generate various keys.
At step 6, Trudy is unable to send the correct MAC and is thus discovered by Bob.

**R24 Consider sending a stream of packets from Host A to Host B using IPsec.
Typically, a new SA will be established for each packet sent in the stream.
True or False?**
error. If A to B, then at most two SAs.

**R25 Suppose that TCP is being run over IPsec between headquarters and the
branch office in Figure 8.28. If TCP retransmits the same packet, then the two
corresponding packets sent by R1 packets will have the same sequence num-
ber in the ESP header. True or False?**
error, because this is a new packet, it is not clear to IPsec whether it is a retransmission or not, and there is no need to know.

**R26 An IKE SA and an IPsec SA are the same thing. True or False?**
is not. IKE SA is the channel used to generate IPsec SA.

**R27 Consider WEP for 802.11. Suppose that the data is 10101100 and the
keystream is 1111000. What is the resulting ciphertext?**
01011100

**R28 In WEP, an IV is sent in the clear in every frame. True or False?**
is correct.

**R29 Stateful packet filters maintain two data structures. Name them and briefly
describe what they do.**
Connection Table:
Tracks all ongoing TCP connections.
Access Control Lists:
Implement firewall rules.

**R30 Consider a traditional (stateless) packet filter. This packet filter may filter
packets based on TCP flag bits as well as other header fields. True or False?**
correct.

**R31 In a traditional packet filter, each interface can have its own access control
list. True or False?**
is correct.

**R32 Why must an application gateway work in conjunction with a router filter to be effective?**
The application gateway can determine the connection at the application layer, while the packet filter is determined at the network layer and the transport layer.
Standard answer:
Without the packet filter, users within the organization's network can still connect directly to hosts outside the organization's network. The filter forces the user to connect to the application gateway first.

**R33 Signature-based IDSs and IPSs inspect into the payloads of TCP and UDP
segments. True or False?**
does not necessarily need to check the payload, it is related to the rules specified by the ruleset.

#### Chapter 9 Q/A

**R1 Why would a network manager benefit from having network management
tools? Describe five scenarios.**
administrator does not need to manually go to the remote device to directly control the device. The administrator can predict the failure or damage of a device in the network in advance. Administrators can detect abnormal network traffic and take appropriate action. Administrators can understand the usage of network resources and make appropriate judgments for network upgrades. Network administrators can find out if there is any illegal intrusion.

**R2 What are the five areas of network management defined by the ISO?**
performance management, fault management, configuration management, account management, security management

**R3 What is the difference between network management and service
management?**
service management is the management of computing/communication resources used to meet certain needs, and network management is only a part of service management. Network management is only responsible for the normal operation of the network, but is responsible for making the network meet the service requirements.

**R4 Define the following terms: managing entity, managed device, management
agent, MIB, network management protocol.**
Management Entity:
Performs network management activities and controls the collection, processing, analysis and display of network management information.
Managed device: A
managed device is a network device supervised by a managed entity.
Management Agent:
A process in a managed device that communicates with a management entity, under the command and control of the management entity.
MIB:
Information about managed objects, which can be used by managed entities.
Network Management Protocol:

**R5 What is the role of the SMI in network management?**
is a definition language for ensuring that the syntax and semantics of network management data are well-defined and unambiguous.

**R6 What is an important difference between a request-response message and a trap message in SNMP?**
request-response message is the message that the managed entity requests and then replies from the managed agent.
Trap messages are messages sent directly by the managed agent to the management entity.

**R7 What are the seven message types used in SNMP?**
GetRequest, GetNextRequest, GetBulkRequest, InformRequest, SetRequest, Response, SNMPv2-Trap

**R8 What is meant by an 'SNMP engine'?**
encapsulation processes, schedules and delivers messages.

**R9 What is the purpose of the ASN.1 object identifier tree?**
The object identity tree is described in Section 9.3.
Standardized identification of management information modules.

**R10 What is the role of ASN.1 in the ISO/OSI reference model's presentation layer?**
transfers and converts information from one machine-specific format to another machine-specific format.

**R11 Does the Internet have a presentation layer? If not, how are concerns about
differences in machine architectures—for example, the different representa-
tion of integers on different machines—addressed?**
does not, it is not clear how to achieve.

**R12 What is meant by TLV encoding?**
TLV encoding specifies how the defined objects are sent by the network.
