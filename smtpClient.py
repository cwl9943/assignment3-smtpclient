from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((port, mailserver))
    # Fill in end
    try:
        recv = clientSocket.recv(1024).decode()
        #print(recv) #You can use these print statement to validate return codes from the server.
        if recv[:3] != '220':
            raise Exception('220 reply not received from server.')
    except Exception as e:
        print(f"An error occurred: {e}")
        clientSocket.close()
        return

    try:
        # Send HELO command and print server response.
        heloCommand = 'HELO Alice\r\n'
        clientSocket.send(heloCommand.encode())
        recv1 = clientSocket.recv(1024).decode()
        
        print(recv1) 
        if recv1[:3] != '250':
            raise Exception('250 reply not received from server.')
    except Exception as e:
        print(f"An error occurred: {e}")
        clientSocket.close()
        return
        
    # Send MAIL FROM command and handle server response.
    # Fill in start
    try:
        mailCommand = 'MAIL FROM: <cwl9943@nyu.edu>\r\n'
        clientSocket.send(mailCommand.encode())
        recv1 = clientSocket.recv(1024).decode()
        
        print(recv1) 
        if recv1[:3] != '250':
            raise Exception('250 reply not received from server.')
    except Exception as e:
        print(f"An error occurred: {e}")
        clientSocket.close()
        return
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    try:
        rcptCommand = 'RCPT TO: <cwl9943@nyu.edu>\r\n'
        clientSocket.send(rcptCommand.encode())
        recv1 = clientSocket.recv(1024).decode()
        
        print(recv1) 
        if recv1[:3] != '250':
            print('250 reply not received from server.')
            raise Exception('220 reply not received from server.')
    except Exception as e:
        print(f"An error occurred: {e}")
        clientSocket.close()
        return
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    try:
        dataCommand = 'DATA\r\n'
        clientSocket.send(dataCommand.encode())
        recv1 = clientSocket.recv(1024).decode()
        
        print(recv1) 
        if recv1[:3] != '354':
            raise Exception('354 reply not received from server.')
    except Exception as e:
        print(f"An error occurred: {e}")
        clientSocket.close()
        return
    # Fill in end
    
    # Send message data.
    # Fill in start
    try:
        clientSocket.send(msg.encode())
    except Exception as e:
        print(f"An error occurred: {e}")
        clientSocket.close()
        return
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    try:
        clientSocket.send(endmsg.encode())
    # Fill in end
    except Exception as e:
        print(f"An error occurred: {e}")
        clientSocket.close()
        return
        
    # Send QUIT command and handle server response.
    # Fill in start
    try:
        quitCommand = 'QUIT\r\n'
        clientSocket.send(quitCommand.encode())
        recv1 = clientSocket.recv(1024).decode()
        
        print(recv1)
        if recv1[:3] != '221':
            print('221 reply not received from server.')
        # Fill in end
    except Exception as e:
        print(f"An error occurred: {e}")
        clientSocket.close()
        return
        
    try:
        clientSocket.close()
    except Exception as e:
        print(f"An error occurred: {e}")
        clientSocket.close()
        return
        
if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
