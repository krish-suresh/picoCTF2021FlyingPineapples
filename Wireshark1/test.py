import pyshark

# Change FILENAME to your pcap file's name.
FILENAME = "shark1.pcapng"
# Change STREAM_NUMBER to the stream number you want to follow.
STREAM_NUMBER = 0

# open the pcap file, filtered for a single TCP stream 
cap = pyshark.FileCapture(
    FILENAME,
    display_filter='tcp.stream eq %d' % STREAM_NUMBER)

while True:
    try:
        p = cap.next()
    except StopIteration:  # Reached end of capture file.
        break
    try:
        # print data from the selected stream
        print(p.data.data.binary_value)
    except AttributeError:  # Skip the ACKs.
        pass