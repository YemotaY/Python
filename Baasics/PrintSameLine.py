Words = ["Hello","you","egg"]
Message_Queue = 0

for msg in Words:
    Message_Queue += 1
    print(msg + " MQ: " + str(Message_Queue) , end='\n')
 