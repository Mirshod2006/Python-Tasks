import re
from collections import defaultdict

data = [
    {"Email": "user1@example.com", "File_name": "file1.txt", "Mac_address": "A1:B2:C3:D4:E5:F6"},
    {"Email": "user2@sample.com", "File_name": "file2.txt", "Mac_address": "A0:1B:2C:3D:4E:5F"},
    {"Email": "user3@testmail.com", "File_name": "document1.pdf", "Mac_address": "B2:C3:D4:E5:F6:A1"},
    {"Email": "user4@domain.com", "File_name": "image1.png", "Mac_address": "C3:D4:E5:F6:A1:B2"},
    {"Email": "user5@website.org", "File_name": "audio1.mp3", "Mac_address": "D4:E5:F6:A1:B2:C3"},
    {"Email": "user6@company.net", "File_name": "video1.mp4", "Mac_address": "E5:F6:A1:B2:C3:D4"},
    {"Email": "user7@example.co", "File_name": "file3.docx", "Mac_address": "F6:A1:B2:C3:D4:E5"},
    {"Email": "user8@sample.net", "File_name": "file4.xlsx", "Mac_address": "A1:C2:D3:E4:F5:A0"},
    {"Email": "user9@demo.com", "File_name": "file5.zip", "Mac_address": "B0:A1:C2:D3:E4:F5"},
    {"Email": "user10@service.org", "File_name": "file6.pptx", "Mac_address": "C1:B2:A3:D4:E5:F6"},
    {"Email": "user11@provider.com", "File_name": "file7.csv", "Mac_address": "D2:C3:B4:A5:F6:E1"},
    {"Email": "user12@samplemail.com", "File_name": "file8.html", "Mac_address": "E3:D4:C5:B6:A0:F1"},
    {"Email": "user13@test.net", "File_name": "file9.xml", "Mac_address": "F4:E5:D6:C7:B1:A2"},
    {"Email": "user14@myemail.com", "File_name": "file10.json", "Mac_address": "A5:F6:E7:D8:C2:B3"}
]

result=[]
for entry in data:
    mac = entry["Mac_address"]
    if ((i%2==0 and re.match(r'[A-F]',mac[i])) or (i%2==1 and re.match(r'[0-9]',mac[i])) for i in range(len(mac.replace('.','')))):
        result.append((entry["Email"],entry["File_name"]))
print("Email and File Names with Valid Mac Addresses:")
for email, file_name in result:
    print(f"Email: {email}, File Name: {file_name}")

domain_count=defaultdict(int)
for entry in data:
    domain = entry["Email"].split('@')[-1]
    domain_count[domain]+=1

print("\nEmail Domain Counts:")
for domain, count in domain_count.items():
    print(f"Domain: {domain}, Count: {count}")