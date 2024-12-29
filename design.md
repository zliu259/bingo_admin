# Bingo admin system design
## 1. Introduction

## 2. Workflow
1. Quotation: 
    - 1.1. Client request quotation
    - 1.2. Estimate work load and time
    - 1.3. Generate quotation document
    - 1.4. Send quotation to client
    - 1.5. Confirm quotation
2. Payment
    - 2.1. Send invoice to client
    - 2.2. Client make payment
    - 2.3. Confirm payment
3. Working
    - 3.1. Divide work into tasks
    - 3.2. Assign tasks to team members (including AI)
    - 3.3. Merge all completed tasks
    - 3.4. Generate draft document
4. Review
    - 4.1. Review draft document
    - 4.2. Make changes
    - 4.3. Generate final document
5. Documentation
    - 5.1. Generate documentation with stamp
    - 5.2. Generate job cover sheet
    - 5.3. Package all documents
    - 5.4. Generate task report (statistics) for internal analysis
6. Delivery
    - 6.1. Send documents to client via client's preferred method
    - 6.2. Confirm delivery

## 3. Work Type and Method
1. Translation (CHN<-->ENG)
    - ID Documents (Driver's License, National ID, etc.) **Full-automatic fetching and translating by Tencent OCR + Chatgpt Batch**
    - Pictures (WeChat Screenshot, etc.) **Semi-automatic fetching and translating by local OCR + Chatgpt Batch**
    - Formatted files or documents (html, etc.) **Fetching and translating by script + Chatgpt Batch**
    - Unformatted documents (txt, etc.) **Manual processing the content + Chatgpt Batch translation**
    - Audio files (mp3, etc.) **Fetching and translating by Whisper + Chatgpt Batch**
2. Interpretation
3. Certified Copy

## 4. System Design
1. Project
~~~python
import uuid
from datetime import datetime

class Project:
    # basic info
    job_id: uuid
    date: datetime
    job_type: int # 1 Translation, 2 Interpretation, 3 Certified Copy
    due_date: datetime
    
    # client info
    client: str
    client_id: uuid
    client_contact: str
    
    # progress info
    active: bool # True if the project is active (not completed)
    status: int # 1 Quotation, 2 Payment, 3 Working, 4 Review, 5 Documentation, 6 Delivery
    node: str # Current node responsible person
    
    # task info
    int_file = [str] # file path
    temp_file = [str] # file path
    out_file = [str] # file path
    
    
    # quotation info
    estimat: [dict] # [{task: file, load: int, time: int}]
    quotation: str # quotation file path
    amount: float
    gst: bool # True if GST needed
    currency: str # CNY, AUD, USD, etc.
    payment_status: bool # True if payment is completed
    payment_method: str # WeChat, Alipay, Bank Transfer, etc.
    
    #system info
    created_by: str
    created_time: datetime
    

~~~



